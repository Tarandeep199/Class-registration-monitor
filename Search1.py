import requests
from bs4 import BeautifulSoup as bs
import time
import urllib.request
import threading
import _thread
from datetime import datetime


def main1():
    crnNumber = None
    allSeats = []
    round1 = []
    round2 = []

    programRunning = True
    counter = 0
    counter2 = 0

    def pullInfo(crnNumber):
        term2Chosen.clear()
        for i in range(len(list)):
            if(list[i] == crnNumber):
                for a in range(13):
                    term2Chosen.append(list[i+a])



    while programRunning == True:
        endpoint = "https://mystudentrecord.ucmerced.edu/pls/PROD/xhwschedule.P_ViewSchedule"
        payload = {"validterm": '201920 - S6',
        "subjcode": "ALL",
        "openclasses": "Y"}
        r = requests.post(endpoint, data = payload)
        #print(r.status_code)
        soup = bs(r.text,"html.parser")
        list = []

        #print(soup)

        for hit in soup.findAll(attrs={'class' : 'dddefault'}):
            list.append(hit.text)

        allNumbers = []
        crnNumbers = []
        seatsAvailable = []
        #print(list)
        #print(list)


        for i in range(len(list)):
            if list[i].isdigit()==True:
                if int(list[i]) < 500:
                    allNumbers.append(list[i])
                if len(list[i])==5 and list[i]!="Staff":
                    crnNumbers.append(list[i])

        for j in range(len(allNumbers)):
            if j%4==3 and j>2:
                seatsAvailable.append(allNumbers[j])


        if counter == 0:
            round1 = seatsAvailable.copy()
            #print(counter)
            counter = 1
        else:
            round2 = seatsAvailable.copy()
            #print(counter)
            counter = 0
        time.sleep(1)

        if round1 != round2:
            if counter2>1:
                for i in range(len(round1)):
                    if(round1[i]!=round2[i]):
                        print(str(datetime.now().time().strftime('%I:%M %p')) + " The number of seats for class number #" + crnNumbers[i] + " has changed by " + str(int(round1[i])-int(round2[i])))
        counter2 = counter2+1
        #print("checkpoint")
    #print(allNumbers)
