import requests
from bs4 import BeautifulSoup as bs
import time
from datetime import datetime
from twilio.rest import Client


def main3():
    print("main3 has been started")
    account_sid = 'AC0a4967cd787a6ff9d833d778af5a82f2'
    auth_token = '4ca2e51948b023457d9dec3c3bad830c'
    client = Client(account_sid, auth_token)
    crnNumber = None
    allSeats = []
    round1 = []
    round2 = []
    starttime = time.time()

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
        payload = {"validterm": '201920 - S62',
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
        classNames = []
        #print(list)
        #print(list)


        for i in range(len(list)):
            if len(list[i])>4:
                if list[i][3] == "-" or list[i][4] == "-" and list[i][1]!=":" and list[i][2]!=":":
                    classNames.append(list[i])
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
                                    if counter2%2==0:
                                        result = int(round1[i]) - int(round2[i])
                                    else:
                                        result = int(round2[i]) - int(round1[i])
                                    if result == 1:
                                        print("dropped spot")
                                        print(str(datetime.now().time().strftime('%I:%M %p'))+ " " + classNames[i] + "(" + crnNumbers[i] + ") has just opened up with " + seatsAvailable[i] + " available space(s)")
                                        message = client.messages \
                                                        .create(
                                                             body=(str(datetime.now().time().strftime('%I:%M %p'))+ " " + classNames[i] + "(" + crnNumbers[i] + ") has just opened up with " + seatsAvailable[i] + " available space(s)"),
                                                             from_='+19497993437',
                                                             to='+19713257738'
                                                         )
                                    else:
                                        print(str(datetime.now().time().strftime('%I:%M %p'))+ " " + classNames[i] + "(" + crnNumbers[i] + ") has taken a spot, there are " + seatsAvailable[i] + " available space(s)")


        #print(list)
        #print(len(classNames))
        #print(classNames)
        #print(len(seatsAvailable))
        #print(seatsAvailable)
        counter2 = counter2+1
        #print("checkpoint")
    #print(allNumbers)
