

print("Bank acount balance")

balance=float(input("write your balance: "))
withdrawal=int(input("write your withdrawal: "))

if withdrawal>0: 
    if  withdrawal>= balance:
        balance -= withdrawal
        print("ok")
        print("your new balance: ",balance,"toman")
    if balance<100000:
        print("balance is not enough")

else:
    ("you cant withdrewal")