#run all 3 searches here
import importlib
from threading import Thread
from Search1 import main1
from Search2 import main2
from Search3 import main3
from datetime import datetime


counter = 0

if __name__ == '__main__'  and counter<5:
    Thread(target = main1).start()
    Thread(target = main2).start()
    Thread(target = main3).start()
    counter = counter+1
print("Up and running!")
