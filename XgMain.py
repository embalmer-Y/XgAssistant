import threading
import os
import time

from settings import SETTINGS, setting_menu, get_address, help_menu, welcome_menu
from ToolsKit.BaiduAiTools.SpeechModel import speech_synthesis
from ToolsKit.TuringAiTools.GetMessage import get_message
from ToolsKit.ProgressModel import process_bar
from ToolsKit.RecordModel import recording

if __name__ == '__main__':
    print('耐心点哦~我在路上了~')
    path = os.getcwd()
    t1 = threading.Thread(target=get_address, name='startThread')
    t1.start()
    process_bar()
    print("我是雪糕，请多关照~(不想和我说话了就打个‘滚’吧)")
    welcome_menu()
    while True:
        if SETTINGS['flag_voice'] == 'Y':
            msg_in = recording(media_id=str(int(time.time())), path_name=path)
        else:
            msg_in = input('>>>')
        if msg_in == '滚':
            break
        elif '不会用' in msg_in:
            help_menu()
        elif '调教' in msg_in:
            setting_menu()
        else:
            if SETTINGS['flag_voice'] == 'Y':
                reply_msg = get_message(msg_in, SETTINGS)
                speech_synthesis(str(int(time.time())), path, reply_msg)
            else:
                reply_msg = get_message(msg_in, SETTINGS)
