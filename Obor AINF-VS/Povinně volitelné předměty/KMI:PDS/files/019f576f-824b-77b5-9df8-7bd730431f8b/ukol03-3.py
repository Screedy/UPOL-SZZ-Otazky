import time
import random
from threading import Thread, Semaphore, Lock

NUM_SAVAGES = 5
NUM_MISSIONARY = 10

need_cook = Semaphore(1)
taking_portions = Semaphore(0)
PORTIONS = 0


def eat(i: int):
    print(f"savage {i}: start eat a portion")
    time.sleep(random.randint(1, 10) / 100)
    print(f"savage {i}: stop eat a portion")


def savage(i: int):
    global PORTIONS
    global need_cook
    global taking_portions

    while True:
        time.sleep(1)
        taking_portions.acquire()
        PORTIONS -= 1
        if PORTIONS == 0:
            need_cook.release()
            eat(i)
        else:
            taking_portions.release()
            eat(i)


def cooker(i: int):
    global PORTIONS
    global need_cook
    global taking_portions

    while True:
        need_cook.acquire()
        PORTIONS = NUM_MISSIONARY
        print(f"Bon Appétit")
        taking_portions.release()


if __name__ == "__main__":

    savages = [Thread(target=savage, args=(i,)) for i in range(NUM_SAVAGES)]
    cookers = [Thread(target=cooker, args=(0,))]

    for t in savages + cookers:
        t.start()

    for t in savages + cookers:
        t.join()
