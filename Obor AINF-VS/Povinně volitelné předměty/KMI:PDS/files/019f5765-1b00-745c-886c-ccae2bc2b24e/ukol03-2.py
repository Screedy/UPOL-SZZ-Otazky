
import time
import random
from threading import Thread, Semaphore, Lock

agent = Semaphore(1)
tobacco = Semaphore(0)
paper = Semaphore(0)
match = Semaphore(0)

isTobacco = False
isPaper = False
isMatch = False
tobaccoSem = Semaphore(0)
paperSem = Semaphore(0)
matchSem = Semaphore(0)
lock = Lock()

def agent_A():
    while True:
        agent.acquire()
        tobacco.release()
        paper.release()

def agent_B():
    while True:
        agent.acquire()
        paper.release()
        match.release()

def agent_C():
    while True:
        agent.acquire()
        tobacco.release()
        match.release()


def pusher_A():
    global isPaper
    global isMatch
    global isTobacco

    while True:
        tobacco.acquire()
        lock.acquire()
        if isPaper:
            isPaper = False
            matchSem.release()
        elif isMatch:
            isMatch = False
            paperSem.release()
        else:
            isTobacco = True
        lock.release()

def pusher_B():
    global isPaper
    global isMatch
    global isTobacco

    while True:
        paper.acquire()
        lock.acquire()
        if isMatch:
            isMatch = False
            tobaccoSem.release()
        elif isTobacco:
            isTobacco = False
            matchSem.release()
        else:
            isPaper = True
        lock.release()

def pusher_C():
    global isPaper
    global isMatch
    global isTobacco

    while True:
        match.acquire()
        lock.acquire()
        if isTobacco:
            isTobacco = False
            paperSem.release()
        elif isPaper:
            isPaper = False
            tobaccoSem.release()
        else:
            isMatch = True
        lock.release()


def smoker_M():
    while True:
        matchSem.acquire()
        print(f"smoker_M make take a cigaret")
        agent.release()

def smoker_T():
    while True:
        tobaccoSem.acquire()
        print(f"smoker_T make take a cigaret")
        agent.release()

def smoker_P():
    while True:
        paperSem.acquire()
        print(f"smoker_P make take a cigaret")
        agent.release()

if __name__ == "__main__":
    
    threads = [
        Thread(target=agent_A),
        Thread(target=agent_B),
        Thread(target=agent_C),
        Thread(target=smoker_M),
        Thread(target=smoker_T),
        Thread(target=smoker_P),
        Thread(target=pusher_A),
        Thread(target=pusher_B),
        Thread(target=pusher_C)
        ]
    
    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()