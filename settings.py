"""
XgAssistant settings
"""

from urllib.request import urlopen
import random

import IPy
import requests


SETTINGS = {
    'str_ywz': [' (°ー°〃)', '(#`O′)', '╰(*°▽°*)╯', '(＠_＠;)', '( =•ω•= )m', '(*/ω＼*)', '( ﹁ ﹁ ) ~→'],
    'city': '',
    'province': '',
    'street': '',
    "apiKey": "",
    "userId": "584181",
    'font_color': '36',
    'background_color': '40',
    'flag_voice': 'N'
}


WELCOME_LIST = [
    ' ˙Ⱉ˙ฅ 嘻嘻你终于来找我玩啦 ',
    ' (/= _ =)/~┴┴ 哼怎么现在才来找我  ',
    '  ┬＿┬ 你再不来人家要单相思了  ',
    '(*/ω＼*) 让我看看是哪个小可爱来啦',
]


def setting_menu():
    global SETTINGS
    print('='*39)
    print('%配置文件%'.center(39))
    print('-'*39)
    for key, value in SETTINGS.items():
        print(f'{key}->{value}')
    print('-'*39)
    print('输入对应变量名并键入值进行修改')
    print('输入exit退出菜单')
    print('='*39)
    while True:
        msg_set = input('>')
        if msg_set == 'exit':
            break
        elif msg_set in SETTINGS.keys():
            if msg_set == 'str_ywz':
                ywz = input('请输入要添加的表情:')
                SETTINGS[msg_set].append(ywz)
            SETTINGS[msg_set] = input('请输入value:')
        else:
            print('输入有误重新输入！')


def get_location(ip):
    url = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?co=&resource_id=6006&t=1529895387942&ie=utf8&oe=' \
          'gbk&cb=op_aladdin_callback&format=json&tn=baidu&cb=jQuery110203920624944751099_1529894588086&_=' \
          '1529894588088&query=%s' % ip
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    html = r.text
    c1 = html.split('location":"')[1]
    c2 = c1.split('","')[0]
    return c2


def check_ip(ip):
    try:
        IPy.IP(ip)
        return True
    except Exception as e:
        print(e)
        return False


def get_address():
    my_ip = urlopen('http://ip.42.pl/raw').read()
    ip = str(my_ip).strip('b')
    ip = eval(ip)
    print(ip)
    if check_ip(ip):
        msg = get_location(ip).split(' ')
        if '省' in msg[0] and '市' in msg[0]:
            city_index = msg[0].find('市')
            province_index = msg[0].find('省')
            SETTINGS['city'] = msg[0][province_index+1:city_index+1]
            SETTINGS['province'] = msg[0][:province_index+1]
            print('初始化成功,IP位置为：', get_location(ip))
        else:
            print('地址初始化失败，请使用setting手动设置!')


def welcome_menu():
    print(f'\033[1;{SETTINGS["font_color"]};{SETTINGS["background_color"]}m{random.choice(WELCOME_LIST)}\033')


def help_menu():
    str_space = ' '
    width = 39
    print('=' * width)
    print('雪糕v0.1'.center(width))
    print('author:\N{Cat}Emb'.center(width))
    print('-' * width)
    print(f'help:{str_space * 28}帮助菜单')
    print(f'setting:{str_space * 28}设置')
    print(f'滚:{str_space * 30}退出程序')
    print('=' * width)
