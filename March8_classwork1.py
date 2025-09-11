#class work 1 
#Hien Tran
#Define demonination of coins/bills  i.e a greedy algo
demoninations = [100,50,20,10,5,1]

change = int(input("Enter the change amount to be returned $: "))

change_given = {}

for coin in demoninations:
    if change >= coin:
        num_of_coins = change // coin
        change_given[coin] = num_of_coins

        change = change % coin

#result display

print("\nCHange given using the fewest bills: ")
for coin, count in change_given.items():
    print(f"${coin}: {count}")
