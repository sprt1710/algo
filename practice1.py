
print("calculate the taxi fare")

distance= float(input("enter the distance: "))

fare= (distance*8000)+30000

if    distance > 20:
    fare = (fare/100)*95
    print(" your taxifare is:",fare,"toman")
else:
    print("your taxifare is",fare,"toman")
