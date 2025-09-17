print("Classwork by Hien Tran")
#find max and min values
def find_max_value(L)->int:
    maxValue = L[0]
    for n in L[1:]:
        if n > maxValue:
            maxValue = n
    return maxValue

def find_min_value(L)->int:
    minValue = L[0]
    for n in L[1:]:
        if n < minValue:
            minValue = n
    return minValue

#factorial
def factorial(num)->int:
    result = 1
    for i in range(1,num+1):
        result = result * i

    return result

if __name__ == "__main__":
    #ask user to make a list
    user_input = input("Enter Number by spaces: ")
    L = list(map(int, user_input.split()))
    
    #ask user for highest or lowest
    choice = input("Type 'max' to find the highest or min to find the lowest: ").strip().lower()

    #Decision making based on user input
    if choice == 'max':#finding max
        result = find_max_value(L)
        print("The max value is: ", result)
    
    elif choice == 'min': #finding min 
        result = find_min_value(L)
        print("The min value is: ", result)
    else:
        print("Invalid Choice. Please type 'max' or 'min' only")
        
    n = 6
    result = factorial(n)
    print("The factorial is: ", result)

