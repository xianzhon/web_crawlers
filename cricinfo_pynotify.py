#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import pynotify
from time import sleep

def sendmessage(title, message):
    pynotify.init("Test")
    notice = pynotify.Notification(title, message)
    notice.show()
    return

print 'Live Cricket Matches:'
print '='*len('Live Cricket Matches:')
url = "http://static.cricinfo.com/rss/livescores.xml"
sc = requests.get(url)
soup = BeautifulSoup(sc.text,'lxml')
i = 1
for data in soup.findAll('item'):
    print str(i)+'. '+data.find('description').text
    i += 1

list_links = []    
for link in soup.findAll('item'):
    list_links.append(link.find('guid').text)

while True:
    try:
        user_input = int(input('Enter match no: '))
    except ValueError:
        print ('Enter correct input')
        continue
    if user_input < 1 or user_input > 30:
        print ('Enter correct input')
        continue
    else:
        break
  
while True:      
    url = list_links[user_input - 1]
    sc = requests.get(url)
    soup = BeautifulSoup(sc.text,'lxml')
    for score in soup.findAll('title'): 
        sendmessage('Live Score',score.text)
        sleep (60)

