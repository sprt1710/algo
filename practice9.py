

print("food order")

food = input("enter your food type (pitza/burger/sandwich): ")
quantity = int(input("enter your quantity: "))

pitza = 250000
burger = 180000
sandwich = 120000

if food == "pitza":
    total = pitza * quantity

elif food == "burger":
    total = burger * quantity

elif food == "sandwich":
    total = sandwich * quantity

else:
    print("we haven't this food")
    total = 0

if total > 0:
    print("your cost:", total)

    if total > 500000:
        print("drink is free")
