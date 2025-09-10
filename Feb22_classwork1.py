#quick sort

import time as tm
import random

def quick_sort(arr):
    if len(arr) <= 1: # arr already sorted
        return arr

    pivot = arr[len(arr) // 2] #chocing middle elem as pivt
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)
    

random_list = [random.randint(10,9999) for _ in range(10)]
print("Orignal Array:", random_list)

start_time = tm.time()
sorted_arr = quick_sort(random_list)
end_time =  tm.time()

print(f"Sorted Random Array: {sorted_arr}")
print(f"Excution time: {end_time-start_time:.6f} seconds")

