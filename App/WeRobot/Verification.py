import werobot
import requests
import json

from settings import SETTINGS
# from ToolsKit.BaiduAiTools.SpeechModel import speech_synthesis
from ToolsKit.TuringAiTools.GetMessage import get_message


appid = 'wxa72155afef177bf9'  # 换成自己的appId
secret = 'aacb6c8b5fd89e4ba234fc0b2c950655'  # 换成自己的secret
robot = werobot.WeRoBot(token='cjtest')
robot.config["APP_ID"] = appid
robot.config["APP_AECRET"] = secret
client = robot.client


def get_access_token(appid, secret):
    # '''获取access_token,100分钟刷新一次'''
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}'.format(appid,
                                                                                                           secret)
    r = requests.get(url)
    parse_json = json.loads(r.content.decode())
    token = parse_json['access_token']
    return token


def img_upload(media_type, name, app_id, secret):
    token = get_access_token(app_id, secret)
    print(token)
    url = "https://api.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=%s" % (token, media_type)
    # 以二进制的方式读取图片
    files = {'media': open('{}'.format(name), 'rb')}
    r = requests.post(url, files=files)
    parse_json = json.loads(r.content.decode())
    return parse_json['media_id']


@robot.text
def hello(message):
    openid = message.source
    msg = message.content.strip().lower()
    return get_message(msg, settings=SETTINGS)


# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()
