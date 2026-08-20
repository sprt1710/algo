


print("food order")

food= input("enter your food type(pitza/burger/sandwich): ")
quantity= int(input("enter your quantity: "))

pitza= 250000
burger= 180000
sandwich= 120000


total= food * quantity

if   food == pitza or food==burger or food==sandwich:
    print("your cost",total )

else:
    print("we havent this food")

if  total > 500000:
    print("drink is free")