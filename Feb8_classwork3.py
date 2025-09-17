#Selection Sort Alogrithm
#Sorting Books


import time

def selection_sort(books):
    n = len(books)

    for i in range(n):
        minIndex = i
        for j in range(i+1,n):
            if books[j][1] < books[minIndex][1]:
                minIndex = j
        books[i], books[minIndex] = books[minIndex], books[i]
        
#take user input       

num_books = int(input("Enter number of books: "))
books = []

for i in range(num_books):
    name = input("Enter Book Title: ")
    year = int(input(f"Enter publication year of {name}: "))
    books.append((name,year))




start_time = time.time()
selection_sort(books)
end_time = time.time()

print("Sorted Book by Year", books)
print(f"Excution time: {end_time-start_time:.6f} seconds")
