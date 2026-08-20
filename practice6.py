


print("order shiping")

purchase_amount=float(input("purchase amount: "))
shiping_type=input("shiping_type(standard/express):  ")

standard = 50000 
express = 100000 


if    purchase_amount > 2000000 and shiping_type==standard/express:
    cost= purchase_amount = shiping_type
    print( "your total is" ,cost, )

elif    purchase_amount <= 2000000 and shiping_type==standard/express:
    cost= purchase_amount+shiping_type
    print("your total is" ,cost,  )


elif    shiping_type != standard or express:
    print("invalid shiping_type")

else :
    print("good bye")
