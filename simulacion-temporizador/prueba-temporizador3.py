import random
import threading
from threading import Timer

def printit():
  threading.Timer(2.0, printit).start()
  print (random.randint(175, 290))

printit()