import time
def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]
  
# start_time = time.time()
bubbleSort(arr)
# print("--- %s seconds ---" % (time.time() - start_time))

print ("Sorted: ", arr)

test1 = [2,0,2,1,1,0] 
test2 = [2,0,1] 
test3 = [0]
test4 = [1]
bubbleSort(test1)
bubbleSort(test2)
bubbleSort(test3)
bubbleSort(test4)
print ("Sorted: ", test1)
print ("Sorted: ", test2)
print ("Sorted: ", test3)
print ("Sorted: ", test4)