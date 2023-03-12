import threading
import time
from random import randint





numberOfElf = 6
numberAllowed = 3
elfNumberCounter = 0
semaphore = threading.Semaphore(1)

reindeerCounter = 0
numberOfReindeer = 0
reindeerSemaphore = threading.Semaphore(1)

santaSemaphore = threading.Semaphore()
santaState = threading.Lock()
santaCounter = 0



def prepareSleigh():
    print('\nSanta is preparing his sleigh for christmas')
    print('\nSanta has gone for christmas\n')
    print('\nSanta is back from christmas and is continuing with the remaining elves')

def getHitched():
            print('\nReindeer are getting hitched\n')

def getMoreElves():
    global numberAllowed, elfNumberCounter, numberOfElf
    # time.sleep(randint(1, 3))
    print('\nSanta has gotten another set of elves\n')
    print('\nReducing number of elves at the door\n')

    numberOfElf -= 3
    numberAllowed = 3
    elfNumberCounter += 1 

def getHelp():
    print('\nSanta is assisting the elf\n')
    time.sleep(randint(1, 3))

def elfCodeChecker(number):
    global numberAllowed, numberOfElf
    for _ in range(numberAllowed):

        semaphore.acquire()
        if numberAllowed <= 0:
            getMoreElves()
        print('\nElf ', number, ' is opening Santa\'s door\n')
        getHelp()
        numberAllowed -= 1
        print('\nElf number ',number,'Is getting help from santa\n')
        number += 1
        print('\n Santa has helped so is going back to sleep\n')
        semaphore.release()
        print('\n------ Santa is done ------\n')


def reindeerArrived():
    
    global reindeerCounter, numberOfReindeer

    while numberOfReindeer != 9 :

        reindeerSemaphore.acquire()
        print('\nNumber of reindeer is ',numberOfReindeer  ,'  \n')
        time.sleep(randint(1, 2))
        numberOfReindeer += 1
        reindeerSemaphore.release()


    else:
        santaState.acquire()
        print('\nNumber of reindeer is ',numberOfReindeer  ,'  \n')
        print('---all reindeer are ready!---')
        print('\nReindeer calling get hitched')
        getHitched()
        reindeerCounter += 1
        santaState.release()
        
        

def Santa(number):

    print('\nSanta is sleeping\n')

    for _ in range(number):
        santaSemaphore.acquire()
        reindeerArrived()
        prepareSleigh()
        santaSemaphore.release()
        
  
thread = threading.Thread(target=Santa, args=(1,))
thread.start()


threads = []
numb = numberOfElf//3
for i in range(numb):
    threads.append(threading.Thread(target=elfCodeChecker, args=(i+1,)))
    threads[-1].start()
 

