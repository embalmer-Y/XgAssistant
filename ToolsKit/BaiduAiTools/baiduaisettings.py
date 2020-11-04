from aip import AipSpeech


SETTINGS = {
    'APP_ID': '',
    'API_KEY': '',
    'SECRET_KEY': ''
}

SPEECH_SYN_SETTINGS = {
    'spd': 5,
    'pit': 5,
    'vol': 5,
    'per': 4
}

# dev_pid:1537-普通话(纯中文识别), 1737-英语, 1637-粤语, 1837-四川话, 1936-普通话远场
SPEECH_CON_SETTINGS = {
    'cuid': '000000000001',
    'dev_pid': 1537
}

CLIENT = AipSpeech(SETTINGS['APP_ID'], SETTINGS['API_KEY'], SETTINGS['SECRET_KEY'])
