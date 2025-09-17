#Bubble Sort Alorithm
#Execution Time

import time

print("Classwork by Hien Tran")

def bubble_sort(students):
    n = len(students)
    
    for i in range(n):
        for j in range(0,n-i-1):
            if students[j]> students[j+1]:
                students[j], students[j+1] = students[j+1], students[j]


#main
if __name__ == "__main__":
    #take user input
    num_students = int(input("Enter number of students: "))
    students = []
    for i in range(num_students):
        name = input("Enter student name: ")
        score = int(input(f"Enter {name}'s score: "))
        students.append((name,score))

    #measure execution time

    start_time =  time.time()
    bubble_sort(students)
    end_time =  time.time()

    print("Sorted students by score: ", students)
    print(f"Excution time: {end_time-start_time:.6f} seconds")