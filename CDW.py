#-------------------------------------------------------------------------------
# Name:        CDW
# Author:      Nishina
# Created:     18/07/2022
# Copyright:   (c) 2022-2026 Nishina
# Licence:     Released under the MIT license.
#              * see https://opensource.org/licenses/MIT
#-------------------------------------------------------------------------------

class CANDataWrapper:
    def __init__(self, DataCount = '', StartTime = '', EndTime = '', Contents = ''):
        self.DataCount = DataCount
        self.StartTime = StartTime
        self.EndTime = EndTime
        self.Contents = Contents

    def show_attributes(self):
        print('DataCount: ', self.DataCount)
        print('StartTime: ', self.StartTime)
        print('EndTime: ', self.EndTime)
        print('Contents Num: ', len(self.Contents))