

list_jadid=[]

while True:
   
    list=input("1.sign up 2.sign in")
    match list:
   
        case "1":
            print("fill the forum")

            first_name=input("enter your name: ").capitalize()
            last_name=input("enter your last name: ").capitalize().title()
            phone_number=input("phone number")
            name_karbari=input("name karbari: ")
            ramz_vorod=input("ramze vorood: ").casefold()
            list_jadid.append(first_name)
            list_jadid.append(last_name)
            list_jadid.append[phone_number]

            jensiat=input("1.male 2.female 3.other")
            match jensiat:
                case "1":
                        list_jadid.append["MR"]
                case "2":
                        list_jadid.append["MS"]
                case "3":
                        list_jadid.append[" "]
            print("list_jadid")

        case "2":
            username=input("enter username:")
            password=input("enter password: ").casefold

            if username== name_karbari and password== ramz_vorod:
                print("login")
            else:
                print("try again")           
            continue      
            
            
                  
            
                




username=input("enter usernam: ").capitalize()
            password=input("enter passwor: ").casefold()
            
            
            print("sign in succsessful")
            break