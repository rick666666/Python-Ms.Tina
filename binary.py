import time
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1
        else:
            print("Found at:",mid)
            return
    print("Not found")
 
list = [10,9,1,7,6,5,4,3,2,1,74896485]

start_time = time.time()
binary_search(list, 1)
print("--- %s seconds ---" % (time.time() - start_time))