


print("order shiping")

purchase_amount=float(input("purchase amount: "))
shiping_type=input("shiping_type(standard/express):  ")

standard = 50000 
express = 100000 
if   shiping_type =="standard":
    shipping_cost = standard

elif shiping_type == "express":
    shipping_cost = express

else:
    print("invalid shiping_type")

if    purchase_amount > 2000000 :
    shipping_cost = 0

elif    purchase_amount <= 2000000 :
    cost= purchase_amount+shipping_cost

    print("your total is" ,cost  )

