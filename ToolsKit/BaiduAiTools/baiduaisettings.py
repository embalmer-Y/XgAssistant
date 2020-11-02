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

CLIENT = AipSpeech(SETTINGS['APP_ID'], SETTINGS['API_KEY'], SETTINGS['SECRET_KEY'])
