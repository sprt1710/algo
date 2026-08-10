

print("calculate electricity bill")

usage= int(input("enter usage: "))

if  usage <=100 :
    bill=usage * 1000
    print("your bill:",bill,"toman")

elif usage>101 or usage<200 :
    bill=usage * 1500
    print("your bill:",bill,"toman")

elif usage>=200 :
    bill=usage * 2500
    print("your bill:",bill,"toman")

