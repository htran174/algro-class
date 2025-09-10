#Radix Sort

#import time as tm
import random

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count  = [0] * 10

    #Count occurence of each digit at the exp place value
    for i in range(n):
        index =  (arr[i] // exp) % 10
        count[index] += 1

        #Convert count[i] to be actual position in the index in our output
    for i in range(1,10):
        count[i] += count[i-1]
    
    #build array
    for i in range(n-1, -1, -1):
        index = (arr[i] // exp) %10
        output[count[index]-1] = arr[i]
        count[index] -= 1

    #copy stored values from output[] into orignal array
    for i in range(n):
        arr[i] = output[i]

def lsd_radix_sort(arr):
    max_num = max(arr)
    exp = 1

    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *=10

    return arr
def msd_radix_sort(arr):
    max_num = max(arr)
    max_digit = len(str(max_num))

    def msd_radix_helper(arr, digit_place):
        if len(arr) <= 1 or digit_place < 0:
            return arr

        #Create 10 buckets for digits 0-9
        buckets = [[] for _ in range(10)]

        for num in arr:
            digit = ((num // 10 ** digit_place)) % 10
            buckets[digit].append(num)

        sorted_arr = []
        for bucket in buckets:
            sorted_arr.extend(msd_radix_helper(bucket, digit_place -1))
        return sorted_arr
    
    return msd_radix_helper(arr, max_digit -1)

#Main 
if __name__ == "__main__":
    num_elements = int(input("Enter the number of elements: "))
    random_list = [random.randint(10,9999) for _ in range(num_elements)]
    print("\nOringal Array: ", random_list)

    #Perform LSD Radix Sort
    lsd_sorted = random_list.copy()
    lsd_sorted = lsd_radix_sort(lsd_sorted)
    print("\Sorted using LSD Radix Sort: ", lsd_sorted)

    #Perform MSD Radix Sort
    msd_sorted = random_list.copy()
    msd_sorted = msd_radix_sort(msd_sorted)
    print("\Sorted using MSD Radix Sort: ", msd_sorted)