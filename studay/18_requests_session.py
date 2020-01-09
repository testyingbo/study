#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import json

url1 = 'https://ecrf.linklab.com/usercenter/login'
url2 = 'https://ecrf.linklab.com/management/reports/coreNumber/522142540358426624'
user = '18211143643'
psw = '1234qwer'
datas = {
    'username': user,
    'password': psw
}

data2 = {
            'projectId': '522142540358426624'
        }

# r = requests.Session()
# r.post(url, {'username': user, 'password': psw})
# sessinon_id = r.cookies['usercenter.session.id']
# r.headers["Cookie"] = ''+'usercenter.session.id'.format(sessinon_id)
# print r.headers


def login_by_session(url, username, password):
    r = requests.Session()   #获取Session
    r.post(url, {'username': username, 'password': password})
    session_id = r.cookies['usercenter.session.id']
    r.headers['Cookie'] = '' + 'usercenter.session.id={};'.format(session_id)
    return r


a = login_by_session(url1, user, psw)
r = a.post(url2, params=data2)
print a.headers
print r.text