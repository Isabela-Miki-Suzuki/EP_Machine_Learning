import numpy as np
from math import *
#------------------------------------------------------------------
#def funcao( lista ):
#    for x in range(0,5):
#        lista[x]=0
#------------------------------------------------------------------
def main():
    w = np.loadtxt("teste.txt", dtype=int)
    
    print(type(w[0,0]))
#------------------------------------------------------------------
if __name__ == "__main__":
    main()
'''

$ python3 teste.py 
Traceback (most recent call last):
  File "teste.py", line 14, in <module>
    main()
  File "teste.py", line 9, in main
    w = np.loadtxt("teste.txt", dtype=int)
  File "/usr/lib/python3/dist-packages/numpy/lib/npyio.py", line 1146, in loadtxt
    for x in read_data(_loadtxt_chunksize):
  File "/usr/lib/python3/dist-packages/numpy/lib/npyio.py", line 1074, in read_data
    items = [conv(val) for (conv, val) in zip(converters, vals)]
  File "/usr/lib/python3/dist-packages/numpy/lib/npyio.py", line 1074, in <listcomp>
    items = [conv(val) for (conv, val) in zip(converters, vals)]
ValueError: invalid literal for int() with base 10: '1.005'