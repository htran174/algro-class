'''
Hien Tran
Classwork3
Greedy algo for 0/1 knapsack problem
'''


capacity = int(input("Enter the weight capacity of bag (kg): "))
num_items = int(input("Enter the number of items avaiable: "))

items = []

for i in range(num_items):
    item_name = input(f"\nEnter name of items {i+1}: ")

    weight = int(input(f'Enter weight of {item_name}(kg): ' ))
    value =  int(input(f"Enter the value of {item_name}($): "))
    ratio = value / weight
    items.append((item_name, weight, value, ratio))

items.sort(key= lambda x:x[3], reverse=True)

total_weight = 0
total_value = 0
secected_items = []

#greedily choose items based on highest ratio
for item_name, weight, value, ratio in items:
    if total_weight + weight <= capacity:
        secected_items.append(item_name)
        total_weight += weight
        total_value += value

#show the selected items
print("\nGreedy selection (Based on highest value to weight ratio): ")
print(f"Selected items: {secected_items}")
print(f"Total Weight: {total_weight} kg")
print(f"Total Value: ${total_value}")

print("\nNote: Greedy algorithm may not always provid the optimal solution for 0/1 Knapsack problem")
