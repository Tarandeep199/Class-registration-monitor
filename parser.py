import requests
from bs4 import BeautifulSoup as bs
import time

crnNumber = None
allSeats = []
programRunning = True
counter = 0
termChosen = input("Wich term would you like:(F6/S6/L8) ")
crnNumber = input("Enter crn: ")
if(termChosen == 'F6'):
    term = '201920 - S6'
if(termChosen == 'S6'):
    term = '201920 - S62'
if(termChosen == 'L8'):
    term = '201920 - S8'


def pullInfo(crnNumber):
    term2Chosen.clear()
    for i in range(len(list)):
        if(list[i] == crnNumber):
            for a in range(13):
                term2Chosen.append(list[i+a])


while programRunning == True:
    endpoint = "https://mystudentrecord.ucmerced.edu/pls/PROD/xhwschedule.P_ViewSchedule"
    payload = {"validterm": term,
    "subjcode": "ALL",
    "openclasses": "Y"}
    r = requests.post(endpoint, data = payload)
    #print(r.status_code)
    soup = bs(r.text,"html.parser")
    list = []

    #print(soup)

    for hit in soup.findAll(attrs={'class' : 'dddefault'}):
        list.append(hit.text)

    term2Chosen = []

    #print(list)
    #print(list)


    for i in range(len(list)):
        if(list[i] == crnNumber):
            for a in range(13):
                term2Chosen.append(list[i+a])

    if r.status_code == 200:
        print("Monitoring the class: " + term2Chosen[2])

    print("Available seats left in class #" + term2Chosen[0] + " is : " + term2Chosen[12])
    allSeats.append(term2Chosen[12])
    time.sleep(1)

    counter = counter+1
