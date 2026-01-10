#-------------------------------------------------------------------------------
# Name:        CANdata2matcsv.py
# Author:      Nishina
#
# Created:     14/02/2022
# Copyright:   (c) 2022-2026 Nishina
# Licence:     Released under the MIT license.
#              * see https://opensource.org/licenses/MIT

# ver2.01 GitHub公開版: CAN_Extractor.pyを直接呼び出すように変更
# ver2.00 64bit版
# ver1.05en メッセージを英語に変更
# ver1.05 処理速度向上、IDごとの個別の時間軸設定を可能にした。
# ver1.04 アイコン設定、画面の小修整
# ver1.03 dbcによってはエラーがでる問題を解決。エラーメッセージの修正。
# ver1.02 ファイル名に.が入っていても動くようにした。
# ver1.01 エラーメッセージの修正。
# ver1.0  新規作成
#-------------------------------------------------------------------------------

import os
from datetime import date
from tkinter import messagebox as msgbox
from tkinter import filedialog
import tkinter as tk
import pandas as pd
import cantools.database as cantools_database
import scipy.io as sio
import numpy as np
import tkinter.ttk as ttk
import math
import time
import csv
import pickle
import sys
import webbrowser

# Import local modules
import CDW
from tool import CAN_Extractor


header_text = 'CAN data Converter'
ver_text = 'ver2.01 (GitHub)    ©2021-2025 niseng.biz'
url = 'https://niseng.biz/software'
fweb_open = False


def execute_convert():
    global fweb_open
    global url

    # open web
    if (fweb_open == True):
        webbrowser.open(url)
        fweb_open = False

    data_file_name = log_label['text']
    dbc_name = dbc_label['text']
    dataframe_converter(data_file_name, dbc_name)

    return



def dataframe_converter(data_file_name, dbc_name):
    try:
        ext_index_db = dbc_name.rfind('.')
        ext_dbc = dbc_name[ext_index_db:]
    except:
        msgbox.showwarning('error', 'Unknown CAN data base format.' )
        return

    try:
        ext_index = data_file_name.rfind('.')
        ext = data_file_name[ext_index:]
    except:
        msgbox.showwarning('error', 'Unknown log data file format.' )
        return

    if ext_dbc == '.dbc':
        dbc_can = cantools_database.load_file(dbc_name)
    else:
        msgbox.showwarning('error', 'Unknown CAN data base format.'  )
        return


    # information
    canvas1.create_text(55,pos_y_button + 110, text="Converting ...",tag='S')
    progressbar.configure(value=0)
    progressbar.update()


    #output settings
    indivisual_flag = 0

    if var.get() == 0:
        sample_time_step = 0.01
        add_text = '_resampling_0.01s'
    elif var.get() == 1:
        sample_time_step = 0.1
        add_text = '_resampling_0.1s'
    elif var.get() == 2:
        sample_time_step = 1
        add_text = '_resampling_1s'
    else:
        sample_time_step = 1
        indivisual_flag = 1
        add_text = '_original_sampling'

    fill_na = 1
    fcsv = var2.get()

    if fcsv == 1:
        write_file_name = data_file_name[:ext_index] + add_text  +'.csv'
    else:
        write_file_name = data_file_name[:ext_index] + add_text +'.mat'

    # CAN dbcからIDを抽出
    target_ID_list = []
    for i in range(len(dbc_can.messages)):
        target_ID_list.append(hex(dbc_can.messages[i].frame_id))


    #Config file 作成
    config_file_name = 'Configuration.cfg'
    with open(config_file_name, 'w') as f:
        f.write(data_file_name + '\n')

    # CAN_Extractor.pyを直接呼び出し
    try:
        extraction_state = CAN_Extractor.main()
        if extraction_state != 'finish':
            msgbox.showwarning('error', 'CAN data extraction failed.')
            return
    except Exception as e:
        msgbox.showwarning('error', f'CAN data extraction error: {str(e)}')
        return
    finally:
        if os.path.exists(config_file_name):
            os.remove(config_file_name)

    # read CAN Data .pkl
    can_data_file_name = 'CAN_Data.pkl'
    try:
        with open(can_data_file_name, 'rb') as f:
            CANDatas = pickle.load(f)
    except Exception as e:
        msgbox.showwarning('error', f'Failed to load CAN data: {str(e)}')
        return
    
    max_data_count = CANDatas.DataCount
    file_time_start = CANDatas.StartTime
    file_time_end = CANDatas.EndTime
    can_data = CANDatas.Contents
    
    if os.path.exists(can_data_file_name):
        os.remove(can_data_file_name)



    data_time_length = int((file_time_end - file_time_start)/sample_time_step ) #[per10msec]
    #時間軸を作る
    time_axis = np.arange(0,data_time_length).astype(int) #[per10msec]
    time_axis1 = time_axis.reshape((len(time_axis),1)) * sample_time_step #[per10msec]

    if indivisual_flag == 0:
        #dataframeに時間軸を作る
        can_data_frame = pd.DataFrame(time_axis1, index = time_axis)
        can_data_frame.columns = (['time'])
    else:
        can_data_frame = pd.DataFrame()

    counter = 0
    first_frame_time = 999999999999
    last_frame_time = 0

    #集合に対してinのほうが判定が速いとのこと
    #数値に変換
    target_ID_list = [int(s,16) for s in target_ID_list]
    s_target_ID_list = set(target_ID_list)

    prog_val_old = 0

    signal_counter = 0
    signal_dict = {}
    signal_list = []

    if indivisual_flag == 0:
        counter_gain = 150
    else:
        counter_gain = 200

    for msg in can_data:
        if msg.arbitration_id in s_target_ID_list:
            target_ID = msg.arbitration_id
            df_msg = dbc_can.get_message_by_frame_id(target_ID).decode(msg.data,decode_choices=False, scaling=True)
            msg_time = int((msg.timestamp - file_time_start)*10000) #per0.1ms

            if first_frame_time > msg_time:
                first_frame_time = msg_time

            if last_frame_time < msg_time:
                last_frame_time = msg_time

            id_time_key = '0x'+str(format(target_ID, 'X')) + '_time'
            if id_time_key in signal_dict:
                signal_list[signal_dict[id_time_key]].append(msg_time)
            else:
                signal_dict[id_time_key] = signal_counter
                signal_counter = signal_counter + 1
                signal_list.append([])
                signal_list[signal_dict[id_time_key]].append(msg_time)

            for df_name in df_msg:
                index_name = '0x'+str(format(target_ID, 'X')) + '_' + df_name
                if index_name in signal_dict:
                    signal_list[signal_dict[index_name]].append(df_msg[df_name])
                else:
                    signal_dict[index_name] = signal_counter
                    signal_counter = signal_counter + 1
                    signal_list.append([])
                    signal_list[signal_dict[index_name]].append(df_msg[df_name])

        counter = counter +1
        prog_val = int(counter/max_data_count * counter_gain)

        if prog_val != prog_val_old:
            progressbar.configure(value=prog_val)
            progressbar.update()
            prog_val_old = prog_val


    write_dict = {}
    sub_dict = {}
    id_for_dict_pre = 'XXXXXXX'
    max_name_length = 31
    max_data_count = len(signal_dict.items())
    prog_val_save = prog_val
    counter = 0

    counter_gain2_div = 0.8
    counter_gain2 = (200 - counter_gain) * (counter_gain2_div)
    counter_gain3 = (200 - counter_gain) * (1 - counter_gain2_div)

    can_data_frame_list = []

    if fcsv == 1:
        i = 0
        for key, val in signal_dict.items():
            sig_split_index = key.find('_')
            id_for_dict = 'ID_' + key[:sig_split_index]
            signalname_for_dict = key[sig_split_index + 1:]

            if indivisual_flag == 0:
                if signalname_for_dict == 'time':
                    time_list = [int(x / sample_time_step/10000 ) for x in signal_list[val]]
                else:
                    temp_s = pd.Series(signal_list[val], index = time_list)
                    temp_s = temp_s[~temp_s.index.duplicated()] # '~' means reverse
                    can_data_frame[key] = temp_s
            else:
                can_data_frame_list.append([])
                can_data_frame_list[i].append(key)
                if signalname_for_dict == 'time':
                    can_data_frame_list[i].extend([x / 10000 for x in signal_list[val]]) # [0.1ms] to [sec]
                else:
                    can_data_frame_list[i].extend(signal_list[val])
                i = i + 1

            # progress bar
            counter = counter +1
            prog_val = int(counter/max_data_count * counter_gain2) + prog_val_save
            if prog_val != prog_val_old:
                progressbar.configure(value=prog_val)
                progressbar.update()
                prog_val_old = prog_val

        if indivisual_flag == 0:
            erase_pos1 = int(first_frame_time/sample_time_step/10000 )
            erase_pos2 = int(last_frame_time/sample_time_step/10000 )

            can_data_frame = can_data_frame[:][erase_pos1:erase_pos2]
            can_data_frame['time'] = can_data_frame['time'] - (erase_pos1) * sample_time_step

            can_data_frame = can_data_frame.fillna(method = 'ffill')

    else:
        for key, val in signal_dict.items():
            sig_split_index = key.find('_')
            id_for_dict = 'ID_' + key[:sig_split_index]
            signalname_for_dict = key[sig_split_index + 1:]

            if indivisual_flag == 0:
                if signalname_for_dict == 'time':
                    time_list = [int(x / sample_time_step/10000 ) for x in signal_list[val]]
                else:
                    temp_s = pd.Series(signal_list[val], index = time_list)
                    temp_s = temp_s[~temp_s.index.duplicated()] # '~' means reverse
                    can_data_frame[key] = temp_s

            # progress bar
            counter = counter +1
            prog_val = int(counter/max_data_count * counter_gain2) + prog_val_save
            if prog_val != prog_val_old:
                progressbar.configure(value=prog_val)
                progressbar.update()
                prog_val_old = prog_val
            else:
                if len(signalname_for_dict) > max_name_length:
                    signalname_for_dict = signalname_for_dict[:max_name_length]

                if id_for_dict != id_for_dict_pre:
                    if id_for_dict_pre != 'XXXXXXX':
                        write_dict[id_for_dict_pre] = sub_dict
                        sub_dict = {}

                if signalname_for_dict == 'time':
                    sub_dict[signalname_for_dict] = [x / 10000 for x in signal_list[val]]
                else:
                    sub_dict[signalname_for_dict] = signal_list[val]
                id_for_dict_pre = id_for_dict

        if indivisual_flag == 0:
            max_data_count = len(can_data_frame.columns)
            prog_val_save = prog_val
            counter = 0
            can_data_frame = can_data_frame.fillna(method = 'ffill')
            can_data_frame = can_data_frame.fillna(0)
            for i in range(len(can_data_frame.columns)):
                str_col = can_data_frame.columns.values[i]
                if str_col == 'time':
                    time_col = can_data_frame.iloc[:,i].tolist()
                    continue
                else:
                    sig_split_index = str_col.find('_')
                    id_for_dict = 'ID_' + str_col[:sig_split_index]
                    signalname_for_dict = str_col[sig_split_index + 1:]

                if len(signalname_for_dict) > max_name_length:
                    signalname_for_dict = signalname_for_dict[:max_name_length]

                if id_for_dict != id_for_dict_pre:
                    if id_for_dict_pre != 'XXXXXXX':
                        sub_dict['time'] = time_col
                        write_dict[id_for_dict_pre] = sub_dict
                        sub_dict = {}

                sub_dict[signalname_for_dict] = can_data_frame.iloc[:,i].tolist()
                id_for_dict_pre = id_for_dict

                # progress bar
                counter = counter +1
                prog_val = int(counter/max_data_count * counter_gain3) + prog_val_save
                if prog_val != prog_val_old:
                    progressbar.configure(value=prog_val)
                    progressbar.update()
                    prog_val_old = prog_val

            # 最後のIDだけ追加されていないはず
            sub_dict['time'] = time_col
            write_dict[id_for_dict_pre] = sub_dict

        else:
            # 最後のIDだけ追加されていないはず
            write_dict[id_for_dict_pre] = sub_dict



    for i in range(3):  # 最大3回実行
        try:
            if fcsv == 1:
                if indivisual_flag == 0:
                    can_data_frame.to_csv(write_file_name, index=False )
                else:
                    with open(write_file_name, "w", encoding='utf-8') as f: # 文字コードをutf-8に指定
                        writer = csv.writer(f, lineterminator="\n") # writerオブジェクトの作成 改行記号で行を区切る
                        writer.writerows(can_data_frame_list)

                    df = pd.read_csv(write_file_name)
                    df.T.to_csv(write_file_name, header=False )
            else:
                sio.savemat(write_file_name, write_dict)

            msgbox.showinfo('information', 'done.' )
        except Exception as e:
            if i > 0:
                time.sleep(2)
            if i < 2:
                msgbox.showwarning('error','writing error is occured. \n Please confirm same named file is closed. ')
        else:
            break  # 失敗しなかった時はループを抜ける
    else:
        # リトライが全部失敗した時の処理
        msgbox.showwarning('error','failed to save output file.')
        import traceback
        msgbox.showwarning('error',traceback.format_exc())

    canvas1.delete('S')
    progressbar.configure(value=0)
    progressbar.update()



def dbc_file_select():
    typ=[('CAN database', '*.dbc')]
    fle = filedialog.askopenfilename(filetypes = typ)
    dbc_label['text'] = fle
    return fle


def log_file_select():
    typ=[('can data format', '*.blf *.asc')]
    fle = filedialog.askopenfilename(filetypes = typ)
    log_label['text'] = fle
    return fle

def temp_path(relative_path):
    try:
        #Retrieve Temp Path
        base_path = sys._MEIPASS
    except Exception:
        #Retrieve Current Path Then Error
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

#画面作成
root= tk.Tk()

# アイコン設定（存在する場合のみ）
try:
    logo=temp_path('ico/candata2matcsv.ico')
    if os.path.exists(logo):
        root.iconbitmap(default=logo)
except:
    pass

bg_color = 'gray97'
font1 = ('helvetica', 11)
font2 = ('helvetica', 10)
font3 = ('helvetica', 11, 'bold')
font4 = ('helvetica', 8)

cv_height = 420
canvas1 = tk.Canvas(root, width = 450, height = cv_height, bg = bg_color)
root.title(header_text)
canvas1.pack()

var = tk.IntVar()  # ラジオボタン変数
var.set(3)    # value=0のラジオボタンにチェックを入れる

var2 = tk.IntVar()  # ラジオボタン変数
var2.set(1)

# text
line_pos_y = cv_height-15

canvas1.create_rectangle(0,0,460,35,fill='gold2',outline='')
canvas1.create_text(20,20,text = "BLF, ASC Converter to CSV, MAT", font=font3, fill = 'gray10', anchor='w')

canvas1.create_rectangle(0,line_pos_y,460,line_pos_y+50,fill='gray92',outline='')
canvas1.create_text(220,line_pos_y+10,text = ver_text, font=font4, fill = 'gray30')

# ラジオボタン作成
rdo_text1 = 'Resampling : period 10msec'
rdo_text2 = 'Resampling : period 100msec'
rdo_text3 = 'Resampling : period 1sec'
rdo_text4 = 'Original : individual time axis for each Message'


rdo1 = tk.Radiobutton(root, value=0, variable=var, text=rdo_text1, bg = bg_color, font=font1)
rdo2 = tk.Radiobutton(root, value=1, variable=var, text=rdo_text2, bg = bg_color, font=font1)
rdo3 = tk.Radiobutton(root, value=2, variable=var, text=rdo_text3, bg = bg_color, font=font1)
rdo6 = tk.Radiobutton(root, value=3, variable=var, text=rdo_text4, bg = bg_color, font=font1)

rdo4 = tk.Radiobutton(root, value=1, variable=var2, text='csv', bg = bg_color, font=font1)
rdo5 = tk.Radiobutton(root, value=0, variable=var2, text='mat', bg = bg_color, font=font1)


text1_for_canvas = "# Please select the time axis of output"
content_pos_y = 60
canvas1.create_text(20,content_pos_y,text = text1_for_canvas, font=font1, anchor='w')

stp_x1 = 40
stp_y1 = content_pos_y + 27
rdo6.place(x=stp_x1, y=stp_y1, anchor='w')
rdo1.place(x=stp_x1, y=stp_y1+23, anchor='w')
rdo2.place(x=stp_x1, y=stp_y1+46, anchor='w')
rdo3.place(x=stp_x1, y=stp_y1+69, anchor='w')

text2_for_canvas = "# Please select the output format"
canvas1.create_text(20,content_pos_y + 128, text = text2_for_canvas, font=font1, anchor='w')
stp_x2 = 40
stp_y2 = content_pos_y + 153
rdo4.place(x=stp_x2, y=stp_y2, anchor='w')
rdo5.place(x=stp_x2+75, y=stp_y2, anchor='w')


line_pos_y = content_pos_y + 177,
line_trim_x = 20
canvas1.create_line(line_trim_x, line_pos_y, 450-line_trim_x, line_pos_y, fill = 'gray60')

pos_y_button = content_pos_y + 215

#dbcファイルの選択
Button_dbc = tk.Button(text='Select CANdbc', command=dbc_file_select, bg='honeydew3', fg='black', font=font1)
canvas1.create_window(320, pos_y_button, window=Button_dbc, width = 120, anchor='w')

#ラベルの作成
dbc_label = tk.Message(root, text="CAN dbc file name", font=font2, width=280, bg = bg_color)
dbc_label.place(x=30, y=pos_y_button, anchor='w')

#logファイルの選択
Button_log = tk.Button(text='Select Log file', command=log_file_select, bg='honeydew3', fg='black', font=font1)
canvas1.create_window(320, pos_y_button+ 45, window=Button_log, width = 120, anchor='w')

#ラベルの作成
log_label = tk.Message(root, text="CAN log file name", font=font2, width=280, bg = bg_color)
log_label.place(x=30, y=pos_y_button + 45, anchor='w')

# 押しボタン作成
Button_convert = tk.Button(text='Convert !', command=execute_convert, bg='cornflower blue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(320, pos_y_button + 90, window=Button_convert, width = 120, anchor='w')

#プログレスバー
progressbar=ttk.Progressbar(root,orient="horizontal",length=280,mode="determinate")
progressbar.place(x=20, y=pos_y_button + 90, anchor='w')
maximum_bar=200
value_bar=0
progressbar.configure(maximum=maximum_bar,value=value_bar)
progress_label = canvas1.create_text(245,pos_y_button + 110, text="Progress %",tag='Y', anchor='w')


if __name__ == '__main__':
    root.mainloop()
