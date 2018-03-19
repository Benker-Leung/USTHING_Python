import requests
import re
# import sys
# us = ''
# pw = ''
# try:
#     us = sys.argv[1]
#     pw = sys.argv[2]
# except Exception as e:
#     us = 'lyleungad'
#     pw = 'password'
#
# url = 'https://cas.ust.hk/cas/login'
#
# with requests.Session() as c:
#     USERNAME=us
#     PASSWORD=pw
#     res = c.post(url)
#     ex = re.findall(r'<input type="hidden" name="execution" value="([0-9a-zA-Z\_\-]+?)"', res.text)
#     login_data = dict(username='lyleungad', password=PASSWORD, execution=ex, _eventId='submit')
#     res = c.post(url, data=login_data)
#     print(res.text)

def getCASCookie(USERNAME, PASSWORD='llyjldh-25793260'):
    try:
        session = requests.Session()
        url = 'https://cas.ust.hk/cas/login'
        res = session.post(url)
        ex = re.findall(r'<input type="hidden" name="execution" value="([0-9a-zA-Z\_\-]+?)"', res.text)
        login_data = dict(username='lyleungad', password=PASSWORD, execution=ex, _eventId='submit')
        res = session.post(url, data=login_data)
        print('Success Login')
        return session
    except Exception as e:
        print('Fail Login')
        return None






















#
