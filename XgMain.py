import threading
import os

from settings import SETTINGS, setting_menu, get_address, help_menu, welcome_menu
from BaiduAiTools.SpeechSynthesis import speech_synthesis
from TuringAiTools.GetMessage import get_message
from ToolsKit.ProgressModel import process_bar


if __name__ == '__main__':
    print('耐心点哦~我在路上了~')
    path = os.getcwd()
    t1 = threading.Thread(target=get_address, name='startThread')
    t1.start()
    process_bar()
    print("我是雪糕，请多关照~(不想和我说话了就打个‘滚’吧)")
    welcome_menu()
    while True:
        msg_in = input('>>>')
        if msg_in == '滚':
            break
        elif msg_in == 'help':
            help_menu()
        elif msg_in == 'setting':
            setting_menu()
        else:
            get_message(msg_in, SETTINGS)
            speech_synthesis('111', path)
