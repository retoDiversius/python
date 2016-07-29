import threading
from threading import Timer

informacion = [200,199,198,199,200,201,200]
contador = 0

def printit():
  global contador
  threading.Timer(2.0, printit).start()
  print (informacion[contador])
  if (contador+1)==len(informacion):
    contador=0
  else:
    contador += 1

printit()