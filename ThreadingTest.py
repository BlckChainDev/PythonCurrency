#ThreadingTest.py

import threading
import time
import random

def printA():
    print("A... . ...")
    return 89
def printB():
    print("B****")
def printAny(inarg):
    print(str(inarg))

t1 = threading.Thread(target=printA)

t2 = threading.Thread(target=printAny, args=(789,))

t1.start()
t2.start()

printB()

t1.join()
t2.join()

print("End Here")