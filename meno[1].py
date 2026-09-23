

print("wolcome")


factor_restoran=[]

while True:
    menu= input("1.pitza 900  2.cake 400 3.drink 200 4.exit")    
    while True:
        match menu:
            case "1":
                num_pitza=int(input("number of pitza: "))
                price_pitza=num_pitza*900
                print("price pitza:",price_pitza) 
                factor_restoran.append[price_pitza]   
                break

            case "2": 
                num_cake=int(input("number of cake: "))
                price_cake=num_cake*400
                print("price cake:",price_cake)
                factor_restoran.append[price_cake]
                break

            case "3":
                num_drink=int(input("number of drink: "))
                price_drink=num_cake*200
                print("price drink",price_drink)
                factor_restoran.append[price_drink]
            case "4":
                final_price = sum(factor_restoran)
                if final_price >= 5000:
                    final_price_tax = round(final_price * 1.1)
                    takhfif = final_price_tax * 0.05
                    pardakht = final_price_tax - takhfif
                    print("sod shoma:",takhfif)
                    print("mablagh ghabel pardakht:",pardakht)
                else:
                    final_price_tax = round(final_price * 1.1)
                    print("mablagh ghabel pardakht:",final_price_tax)



    
 


