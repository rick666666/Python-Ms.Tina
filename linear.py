
from typing import List
import time

def search(list,x):
    f = False
    for index, i in enumerate(list):
        if i == x:
            print("Found at:",index)
            f = True
        
    if f == False:
        print("none founded")


list = [10,9,1,7,6,5,4,3,2,1,74896485]
start_time = time.time()
search(list,1)
print("--- %s seconds ---" % (time.time() - start_time))