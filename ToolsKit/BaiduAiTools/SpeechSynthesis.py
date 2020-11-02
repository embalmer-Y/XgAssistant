from playsound import playsound

from ToolsKit.BaiduAiTools.baiduaisettings import CLIENT, SPEECH_SYN_SETTINGS


def speech_synthesis(media_id, path, reply_msg):
    result = CLIENT.synthesis(reply_msg, 'zh', 1, SPEECH_SYN_SETTINGS)
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open(f'{path}\\Media\\DownloadAudio\\{media_id}.mp3', 'wb') as f:
            f.write(result)
        try:
            playsound(f'{path}\\Media\\DownloadAudio\\{media_id}.mp3')
        except IOError as error:
            print(f'play media file failure:{error}')
