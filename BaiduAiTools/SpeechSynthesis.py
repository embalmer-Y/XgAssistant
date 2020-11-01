from aip import AipSpeech
from playsound import playsound

from BaiduAiTools.baiduaisettings import SETTINGS, SPEECH_SYN_SETTINGS


def speech_synthesis(media_id, path):
    client = AipSpeech(SETTINGS['APP_ID'], SETTINGS['API_KEY'], SETTINGS['SECRET_KEY'])

    result = client.synthesis('杨哥贼帅', 'zh', 1, SPEECH_SYN_SETTINGS)
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open(f'{path}\\Media\\{media_id}.mp3', 'wb') as f:
            f.write(result)
        try:
            playsound(f'{path}\\Media\\{media_id}.mp3')
        except IOError as error:
            print(f'play media file failure:{error}')
