# A simple dict made by crawler, supporting Chiners->English and English->Chinese
import requests
import re
from bs4 import BeautifulSoup

browser = requests.Session()


def build_url():
    a = 0
    mesg = input("PLease input:")
    if re.search('^[A-Za-z].*', mesg):
        a = 1
    mesg = mesg.encode()
    mesg = (str(mesg).replace(r'\x', '%'))[2:-1]
    return mesg, a


def CH_EN(addr):
    # browser=requests.Session()
    # http://dict.cn/%E8%8B%B9%E6%9E%9C  apple
    # http://dict.cn/%E6%B0%B4%E6%9E%9C  fruit
    url = 'http://dict.cn/' + addr
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Geck    o) '
                      'Chrome/70.0.3538.77 Safari/537.36'
    }

    response = browser.get(url, headers=headers)

    dic = BeautifulSoup(response.text.replace('<br>', '').replace('<br/>', ''), 'html.parser')

    ch_label = dic.find('h1', class_='keyword')  # 中文标签
    print(ch_label.get_text())

    # 基本释义
    en_meaning = dic.find_all('a', href=re.compile(r'http://dict.cn/[a-z]'))
    print('------------')
    print("基本释义")
    for mean in en_meaning:
        # print(mean['href'])
        result = re.search('/dir/', mean['href'])
        result2 = re.search('/jp/', mean['href'])
        result3 = re.search('/de/', mean['href'])
        result4 = re.search('/fr/', mean['href'])
        result5 = re.search('/kr/', mean['href'])
        result6 = re.search('/es/', mean['href'])
        result7 = re.search('/it/', mean['href'])
        result8 = re.search('/ru/', mean['href'])
        result9 = re.search('/list/yinbiao', mean['href'])
        # print(result)
        if result or result2 or result3 or result4 or result5 or result6 or result7 or result8 or result9:
            continue
        else:
            print((mean.get_text()).strip())

    # 例句
    print('------------')
    print("例句")
    sentence = dic.find_all('ol', slider='2')
    for each in sentence:
        each_2 = each.find_all('li')
        for each_3 in each_2:
            response = each_3.string
            key = re.findall('(?<=\t\t\t\t\t)(.*)(?=\t\t\t\t\t)', response)
            for i in key:
                print(i)

    return


def EN_CH(addr):
    # browser=requests.Session()
    # http://dict.cn/%E8%8B%B9%E6%9E%9C  apple
    # http://dict.cn/%E6%B0%B4%E6%9E%9C  fruit
    url = 'http://dict.cn/' + addr
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Geck    o) '
                      'Chrome/70.0.3538.77 Safari/537    .36'
    }

    response = browser.get(url, headers=headers)
    dic = BeautifulSoup(response.text.replace('<br>', '').replace('<br/>', ''), 'html.parser')

    en_label = dic.find('h1', class_='keyword')  # 英文标签
    print(en_label.get_text())

    # 释义
    print('------------')
    print("释义")
    mean = dic.find_all('li')
    for each in mean:
        each_2 = each.find('span')
        each_3 = each.find('strong')
        if not each_2:
            break
        else:
            print(each_2.get_text() + '\t' + each_3.get_text())

    # 例句
    print('------------')
    print("例句")
    mean = dic.find_all('ol', slider='2')
    for each in mean:
        if not each.string:
            each_2 = each.find_all('li')
            for each_3 in each_2:
                if not each_3.find('strong'):
                    if re.search('^[A-Za-z].*', each_3.string):
                        print(each_3.string + '\n')


# main
url_addr, flag = build_url()

if flag == 1:
    EN_CH(url_addr)
else:
    CH_EN(url_addr)
