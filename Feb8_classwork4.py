#Merge Sort

import time as tm
import random as rd

#list of int that need to be sorted
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) //2
        left_half = arr[:mid]
        right_half = arr[mid:]
        #Recursively apply merge sort on both halfs

        merge_sort(left_half)
        merge_sort(right_half)

        #Merge the two sorted halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] =  left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] =  right_half[j]
            j += 1
            k += 1

#Take user input to get random numbers
num_elemts =  int(input("Enter the number of elements to be generated in the array: "))

#Get random numbers 1-100
arr = [rd.randint(1,100) for _ in range(num_elemts)]
print(f"\nGenerated random array: {arr}")

#ask user if they want to run merge sort on the given array
user_response = input("\nDo you want to run Merge Sort Now? (yes/no): ").strip().lower()

if user_response == 'yes':
    start_time = tm.time()
    merge_sort(arr)
    end_time =  tm.time()
    print(f"Sorted Random Array: {arr}")
    print(f"Excution time: {end_time-start_time:.6f} seconds")




