# Windows実行ファイルビルド手順

このドキュメントでは、CANdata2matcsv.pyをWindows実行ファイル(.exe)にビルドする方法を説明します。

## ビルド方法1: PyInstaller（推奨）

### 1. PyInstallerのインストール

```bash
pip install pyinstaller
```

### 2. ビルドコマンド

```bash
pyinstaller --onefile --noconsole --icon=ico/candata2matcsv.ico --add-data "ico;ico" --name CANdata2matcsv CANdata2matcsv.py
```

オプション説明：
- `--onefile`: 単一の実行ファイルを生成
- `--noconsole`: コンソールウィンドウを表示しない
- `--icon`: アイコンファイルを指定
- `--add-data`: アイコンフォルダを含める
- `--name`: 出力ファイル名

### 3. 出力場所

- `dist/CANdata2matcsv.exe` が生成されます

### 4. 配布用パッケージ作成

```bash
# distフォルダ内に移動
cd dist

# 必要なファイルをコピー
copy ..\LICENSE .
copy ..\README_BINARY.txt .
xcopy ..\ico ico\ /E /I

# フォルダ名を変更
cd ..
move dist CANdata2matcsv_v2.01_win64

# zipで圧縮（配布用）
# Windows標準機能またはPowerShellで圧縮
```

PowerShellで圧縮:
```powershell
Compress-Archive -Path CANdata2matcsv_v2.01_win64 -DestinationPath CANdata2matcsv_v2.01_win64.zip
```

## ビルド方法2: Nuitka（より高速）

### 1. Nuitkaのインストール

```bash
pip install nuitka
```

### 2. ビルドコマンド

```bash
python -m nuitka --onefile --windows-disable-console --windows-icon-from-ico=ico/candata2matcsv.ico --include-data-dir=ico=ico --output-filename=CANdata2matcsv.exe CANdata2matcsv.py
```

### 3. 出力場所

- `CANdata2matcsv.exe` がカレントディレクトリに生成されます

## ビルド前チェックリスト

- [ ] すべての依存パッケージがインストールされている
- [ ] tool/__init__.py が存在する
- [ ] CDW.py が存在する
- [ ] tool/CAN_Extractor.py が存在する
- [ ] tool/CDW.py が存在する
- [ ] ico/candata2matcsv.ico が存在する
- [ ] テストデータで動作確認済み

## ビルド後のテスト

1. 実行ファイルをダブルクリックして起動確認
2. サンプルのBLFまたはASCファイルで変換テスト
3. CSV出力とMAT出力の両方をテスト
4. 各リサンプリングオプションをテスト

## トラブルシューティング

### ImportError: No module named 'tool'

tool/__init__.py が存在することを確認してください。

### アイコンが表示されない

--add-data または --include-data-dir オプションでicoフォルダを含めてください。

### 実行ファイルサイズが大きい

これは正常です。すべての依存ライブラリが含まれるため、50MB以上になることがあります。

## 配布用ファイルリスト

最終的な配布パッケージには以下を含めます：

```
CANdata2matcsv_v2.01_win64.zip
├── CANdata2matcsv.exe
├── README_BINARY.txt
├── LICENSE
└── ico/
    └── candata2matcsv.ico
```

## ライセンス表示の確認

README_BINARY.txt に以下が含まれていることを確認：
- ソースコードの入手先（GitHubリポジトリURL）
- MITライセンスとLGPL v3の両方の記載
- 著作権表示

これにより、LGPL v3の要件（ソースコード入手方法の明記）を満たします。
