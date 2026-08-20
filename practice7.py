

print("BMI")

weight= float(input("enter your weight:  ,kg"))
height= int(input("enter your height:   ,cm"))

bmi= weight/(height**2)

if    weight and height <= 0:
    print("invalid")
    
if    bmi < 18.5:
    print("you are underweight")

elif    bmi >=18.5 and bmi <25:
    print("you have a normal weight")

elif    bmi >= 25 and bmi <30:
    print("you are over weight")

elif    bmi>=30:
    print("you are obese")



