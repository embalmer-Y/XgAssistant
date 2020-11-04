from playsound import playsound

from ToolsKit.BaiduAiTools.baiduaisettings import CLIENT, SPEECH_SYN_SETTINGS, SPEECH_CON_SETTINGS


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


def get_file_content(file_path):
    with open(file_path, 'rb') as fp:
        return fp.read()


def speech_recognition(media_id, path):
    result = CLIENT.asr(get_file_content(f'{path}\\Media\\UploadAudio\\{media_id}.wav'), 'wav', 16000,
                        SPEECH_CON_SETTINGS)
    if result['err_no'] == 0:
        return result['result'][0]
    else:
        print(result['err_msg'])
        return None
