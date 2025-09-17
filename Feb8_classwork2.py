#Insertion Sort

import time

print("Classwork by Hien Tran")

def insertion_sort(cards):
    for i in range(1,len(cards)):
        key = cards[i]
        j = i-1
        while j >= 0 and key < cards[j]:
            cards[j+1] = cards[j]
            j -= 1
        cards[j+1] = key


#take user input
cards = list(map(int,input("Enter cards numbers separated by space: ").split()))

start_time = time.time()
insertion_sort(cards)
end_time = time.time()

print("Sorted cards: ", cards)
print(f"Excution time: {end_time-start_time:.6f} seconds")