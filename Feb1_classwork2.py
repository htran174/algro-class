import time





print("Classwork by Hien Tran")
#Write an alogro for linear search where will find target element T from given list
def linear_search_all(L, Target):

    indices = []
    
    for i in range(len(L)):
        if L[i] == Target:
            indices.append(i)
    return indices

#Taking user input for the list elements
user_input = input("Enter list elements separated by spaces: ")
L = list(map(int, user_input.split()))

#Taking user input for target element
Target = int(input("Enter the target element to search: "))

#Call linear search
start_time = time.time()
result = linear_search_all(L, Target)
end_time = time.time()

#Display
if result:
    print(f"Element {Target} found at indexes: {result}")
    print(f"Excution time: {end_time-start_time:.6f} seconds")
else:
    print(f"Element {Target} not found in list")
    print(f"Excution time: {end_time-start_time:.6f} seconds")
