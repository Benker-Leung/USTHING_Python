from casLogin import getCASCookie
from bs4 import BeautifulSoup
import re

Jobs = {}
title = []
position = []
eventDate = []
time = []
def start():
    # get the cookie in cas for login
    session = getCASCookie('lyleungad')

    # get the html for the page
    res = session.get('https://career.ust.hk/web/on_campus_recruitment_talk.php')
    html = res.text
    # create soup for parsing the webpage
    soup = BeautifulSoup(html, features='lxml')
    # find all items in the page
    items = soup.find_all('tr', {'class':'event-item'})

    for item in items:

        # get job-title and append to title[]
        title.append(item.find('td',{'class':'detail-text large-view'}).find('a').get_text())

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
        position.append(tempPos)    # add to postion[]

        # get Event Date
        date = item.find_all('td', {'class':'detail-text large-view', 'style':'text-align:center; font-weight:400;color:#336C99'})[0]\
        .get_text()
        date = date.replace('\r\n', '')
        date = date.replace('\n', '')
        space = re.findall('\ {2,}', date)
        for eachSpace in space:
            date = date.replace(eachSpace, '')
        eventDate.append(date)

        # get Event time t
        t = item.find_all('td', {'class':'detail-text large-view', 'style':'text-align:center; font-weight:400;color:#336C99'})[1]\
        .get_text()
        t = t.replace('\r\n', '')
        t = t.replace('\n', '')
        space = re.findall('\ {2,}', t)
        for eachSpace in space:
            t = t.replace(eachSpace, '')
        time.append(t)

def getDetails():
    '''get the eventDetails in dictionary type in following
    title, position, eventDate and eventTime
    '''
    start()
    Jobs['title'] = title
    Jobs['position'] = position
    Jobs['eventDate'] = eventDate
    Jobs['eventTime'] = time
    return Jobs
