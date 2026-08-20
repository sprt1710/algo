

print("cinema ticket")

age= int(input("enter your age: "))
day= input("what day is it?"  )

ticket_cost = 200000

if age<12 :
    total=(ticket_cost/100)*50
    print("your cost is",total)

elif age>= 60:
    total=(ticket_cost/100)*30
    print("your cost is",total)

elif day== "tuesday":
    total=(ticket_cost/100)*20
    print("your cost is",total)
 