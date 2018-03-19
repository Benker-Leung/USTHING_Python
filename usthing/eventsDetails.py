from casLogin import CASLogin
from bs4 import BeautifulSoup
import re

class RecruitTalkEvents:

    def __init__(self, username, password, directlyGet=False):
        '''input username, password to get Events
        set directlyGet to true if immediately get the Jobs
        '''
        self.Jobs = {}
        self.title = []
        self.position = []
        self.eventDate = []
        self.time = []
        self.session = CASLogin(username, password)
        self.session = self.session.getCASCookie();
        if(directlyGet):
            self.getEvents();

    def __start(self):
        # get the html for the page
        res = self.session.get('https://career.ust.hk/web/on_campus_recruitment_talk.php')
        html = res.text
        # create soup for parsing the webpage
        soup = BeautifulSoup(html, features='lxml')
        # find all items in the page
        items = soup.find_all('tr', {'class':'event-item'})

        for item in items:

            # get job-title and append to title[]
            self.title.append(item.find('td',{'class':'detail-text large-view'}).find('a').get_text())

            # get Position offer
            tempPos= item.find('td',{'class':'detail-text large-view', 'style':'text-align:left; font-weight:400;color:#336C99'})\
            .get_text()
            # replace the \r\n \n space more than 2 to ''
            tempPos = str(tempPos)
            tempPos = tempPos.replace('\r\n', '')
            tempPos = tempPos.replace('\n', '')
            space = re.findall('\ {2,}', tempPos)
            for eachSpace in space:
                tempPos = tempPos.replace(eachSpace, '')
            self.position.append(tempPos)    # add to postion[]

            # get Event Date
            date = item.find_all('td', {'class':'detail-text large-view', 'style':'text-align:center; font-weight:400;color:#336C99'})[0]\
            .get_text()
            date = date.replace('\r\n', '')
            date = date.replace('\n', '')
            space = re.findall('\ {2,}', date)
            for eachSpace in space:
                date = date.replace(eachSpace, '')
            self.eventDate.append(date)      # add eventDate to eventDate[]

            # get Event time t
            t = item.find_all('td', {'class':'detail-text large-view', 'style':'text-align:center; font-weight:400;color:#336C99'})[1]\
            .get_text()
            t = t.replace('\r\n', '')
            t = t.replace('\n', '')
            space = re.findall('\ {2,}', t)
            for eachSpace in space:
                t = t.replace(eachSpace, '')
            self.time.append(t)   # add t to time[]

    def __getDetails(self):
        '''get the eventDetails in dictionary type in following
        title, position, eventDate and eventTime
        '''
        self.start()
        self.Jobs['title'] = self.title
        self.Jobs['position'] = self.position
        self.Jobs['eventDate'] = self.eventDate
        self.Jobs['eventTime'] = self.time

    def getEvents(self):
        '''this function return the Jobs dictionary for events if success
        have Jobs[types], types are: title, position, eventDate, eventTime
        it return nothing if fail to login or get details
        '''
        if(self.session):
            print('Getting details...')
            self.start();
            self.getDetails();
            print('Finished')
            return self.Jobs
