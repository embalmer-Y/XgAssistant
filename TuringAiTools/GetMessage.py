import json
import random

import requests


def get_message(msg, settings):
    api_url = "http://openapi.tuling123.com/openapi/api/v2"
    data = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": msg
            },
            "selfInfo": {
                "location": {
                    "city": settings['city'],
                    "province": settings['province'],
                    "street": settings['street']
                }
            }
        },
        "userInfo": {
            "apiKey": settings["apiKey"],
            "userId": settings["userId"]
        }
    }
    data_json = json.dumps(data).encode('utf-8')
    r = requests.post(api_url, data=data_json)
    msg_json = r.content.decode('utf-8')
    res = json.loads(msg_json)['results'][0]['values']['text']
    ai_msg = f'{settings["str_ywz"][random.randint(0,5)]}：'+res
    print(f'\033[1;{settings["font_color"]};{settings["background_color"]}m{ai_msg}\033')
    return ai_msg
