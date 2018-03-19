import requests
import re

class CASLogin:
    username = ''
    password = ''
    session = ''

    def __init__(self, ac, pw):
        self.username = ac
        self.password = pw
        self.session = requests.Session();


    def getCASCookie(self):
        '''this function help to get the cookie for CAS Login
        and return a session object if success, or None if not success
        '''
        try:
            url = 'https://cas.ust.hk/cas/login'
            res = self.session.post(url)
            ex = re.findall(r'<input type="hidden" name="execution" value="([0-9a-zA-Z\_\-]+?)"', res.text)
            login_data = dict(username=self.username, password=self.password, execution=ex, _eventId='submit')
            res = self.session.post(url, data=login_data)
            if res.status_code==200:
                print('Success Login')
                return self.session
            else:
                print('Fail Login')
                return None
        except Exception as e:
            print(e)
            print('\nFail Login')
            return None;
#
