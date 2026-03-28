import random
rooms={"single_bedded":1000,"double_bedded":1700,"single_beddedd":500,"double_beddedds":1200,"with_food_AC":1800,"with_food_NON_AC":1500,"pods":100}
pod=[51,52,53,54]
p={"rooms_ACd":[101,102,103,104,105],"rooms_ACs":[1,2,3,4,5],"rooms_NON_ACd":[200,201,202,203,204],"rooms_NON_ACs":[300,301,302,303,304]}
morning_food={"1.SOUTH INDIAN TIFFENS":200,"2.NORTH INDIAN TIFFENS":250, "3.DIET TIFFENS":170}
lunch_food={"1.FULL MEALS":195,"2.NORTH INDIAN THALLI":300,"3.SOUTH INDIAN THALLI":275,"4.BIRYANI'S":350}
dinner_food={"1.NAAN WITH PANNER CURRY":255,"2.CURD RICE+TANDOORI ROTI+PANNER CURRY":290}
snacks={"1.gobi+french fries":190,"2.vada+mysore bonda+ponugulu":150,"3.pizza and burgers":400,"4.ice creams ":50}
morning_food_rates={"1":200,"2":250,"3":170}
lunch_food_rates={"1":195,"2":300,"3":275,"4":350}
dinner_food_rates={"1":255,"2":290}
snacks_rates={"1":190,"2":150,"3":400,"4":50}







while True:
    print("=======WELCOME TO HOTEL BOOKING SYSTEM=======")
    print("1.VIEW ROOMS ")
    print("2.BOOK ROOMS")
    print("3.EXTEND STAY(only after booking)")
    print("4.CHECKOUT ROOM")
    print("5.EXIT")
    try:
        Selection=int(input("Enter the choice from above options"))
    except ValueError:
        print("please the number entered is invaild")
        Selection=int(input("Enter the choice from above options"))


    if Selection==1:
        print("1.AC ROOMS")
        print("2.NON-AC ROOMS")
        print("3.AC Rooms with Food Facilty")
        print("4.Pods")
        print("5.EXIT")
        while True:
            while True:
                try:
                    r=int(input("enter your choice number  "))
                    break
                except ValueError:
                    print("INVALID LITERAL PLEASE ENTER CORRECT ONES")
            if r==1:
                print("AC room is 1000rs for single bedded" )
                print("AC room is Rs1700 for double bedded ")
                break
            elif r==2:
                print("NON-AC room is 500rs for single bedded")
                print("NON-AC room is 1200rs for double bedded")
                break
            elif r==3:
                print("No room service food available for single bedded")
                print("The cost of this room with food availability(AC)is 1800rs in double bedded")
                print("The cost of this room with food availability(NON-AC) is 1500rs in double bedded ")
                break
            elif r==4:
                print("100rs per hour (only single)")
                print("180rs for 3hrs(only single bedded)")
                print("350rs for 6hrs (only single bedded)")
                break
            elif r==5:
                break
                
                



    if Selection==2:
        while True:
            print("which type of rooom do u need?")
            print("1.Single Bedded")
            print("2.Double bedded")
            print("3.Double Bedded with Food")
            print("4.Pods(AC)")
            print("5.EXIT")
            while True:
                try:
                    room_type=int(input("ENTER THE OPTION OF THE TYPE YOU NEED "))
                    break
                except ValueError:
                    print("INVALID LITERAL PLEASE ENTER CORRECT ONES")
            if room_type==5:
                break
            else:
                while True:
                    while True:
                        try:
                            name=input("Enter Your Name (only in alphabets(abcdefghijklmnopqrstuvwxyz))")   
                            PAID=int(input("enter no of days of stay if rooms . ELSE enter no of hours for pods"))
                            y=int(input("enter your aadhar card no"))
                            if len(str(y))==12 and name.isalpha()==True:
                                pass
                                break
                            else:
                                print("INVALID LITERAL PLEASE ENTER CORRECT ONCE")
                        except ValueError:
                            print("invalid literal please enter correct one ")

                        
                    if room_type==1:
                        while True:
                            while True:
                                try:
                                    z=int(input("AC(1) or NON-AC(2)"))
                                    break
                                except ValueError:
                                    print("invalid please re input ")
                            if int(z)==1:
                                room_number=random.choice(p["rooms_ACs"])
                                total_amount=PAID*rooms["single_bedded"]
                                room_rate="single_bedded"
                            elif int(z)==2:
                                room_number=random.choice(p["rooms_NON_ACs"])
                                total_amount=PAID*rooms["single_beddedd"]
                                room_rate="single_beddedd"
                            try:
                                F=int(input("DO YOU NEED ANY EXTRA BEDS [yes=1,no=0]"))
                                if F==1:
                                    extra=int(input("NO. OF BEDS YOU TOOK"))
                                    per_hour=30
                                    extra_hours=int(input("no of hours"))
                                    d=per_hour*extra_hours*extra
                                    break
                                elif F==0:
                                    d=0
                                    break

                            except ValueError:
                                print("invaild inputs please input correct value")
                        
                

                    elif room_type==2:
                        while True:
                            try:
                                name_2=input("ENTER NAME OF SECOND PERSON")
                                z=int(input("AC(1) or NON-AC(2)"))
                            except ValueError:
                                print("INVALID LITERAL SO PLEASE ENTER VALID ONES")
                            if int(z)==1:
                                room_number=random.choice(p["rooms_ACd"])
                                total_amount=PAID*rooms["double_bedded"]
                                room_rate="double_bedded"
                            elif int(z)==2:
                                room_number=random.choice(p["rooms_NON_ACd"])
                                total_amount=PAID*rooms["double_beddedds"]
                                room_rate="double_beddedds"
                            try:
                                F=int(input("DO YOU NEED ANY EXTRA BEDS [yes=1,no=0]"))
                                if F==1:
                                    extra=int(input("NO. OF BEDS YOU TOOK"))
                                    per_hour=30
                                    extra_hours=int(input("no of hours"))
                                    d=per_hour*extra_hours*extra
                                    break
                                elif F==0:
                                    d=0
                                    break

                            except ValueError:
                                print("invaild inputs please input correct value")
                    elif room_type==3:
                            while True:
                                try:
                                    name_2=input("ENTER NAME OF SECOND PERSON")
                                    z=int(input("AC(1) or NON-AC(2)"))
                                    if z!=1 or z!=2:
                                        print("please enter correct option AC OR NON-AC")
                                    else:
                                        break
                                except ValueError:
                                    print("INVALID LITERAL SO PLEASE ENTER VALID ONES")

                            while True:
                                try:
                                    print(morning_food)
                                    choice1=int(input("enter your option for tiffen"))
                                    print(lunch_food)
                                    choice2=int(input("enter your option for lunch"))
                                    print(snacks)
                                    choice3=int(input("enter your option for lunch"))
                                    print(dinner_food)
                                    choice4=int(input("enter your option for dinner"))
                                    break
                                except ValueError:
                                    print("IN UPPER OPTION YOU HAVE ENTERED INVALID LITERAL IN SOME OPTION PLEASE CORRECT AND FILL IT")
                            while True:
                                try:
                                    F=int(input("DO YOU NEED ANY EXTRA BEDS [yes=1,no=0]"))
                                    if F==1:
                                        extra=int(input("NO. OF BEDS YOU TOOK"))
                                        per_hour=30
                                        extra_hours=int(input("no of hours"))
                                        d=per_hour*extra_hours*extra
                                        break
                                    elif F==0:
                                        d=0
                                        break

                                except ValueError:
                                    print("invaild inputs please input correct value")
                            if z==1:
                                total_amount=1800+morning_food_rates[str(choice1)]+lunch_food_rates[str(choice2)]+snacks_rates[str(choice3)]+dinner_food_rates[str(choice4)]
                                room_number=random.choice(p["rooms_ACd"])
                                room_rate="with_food_AC"
                                
                            elif z==2:
                                total_amount=1500+morning_food_rates[str(choice1)]+lunch_food_rates[str(choice2)]+snacks_rates[str(choice3)]+dinner_food_rates[str(choice4)]
                                room_number=random.choice(p["rooms_NON_ACd"])
                                room_rate="with_food_NON_AC"
                            

                        
                                
                    elif room_type==4:
                        while True:
                            while True:
                                try:
                                    PAID=int(input("Enter No.of hours "))
                                    break
                                except ValueError:
                                    print("INVALID OUTPUT")
                            if PAID==3:
                                total_amount=180
                                break
                            elif PAID==6:
                                total_amount=275
                                break
                            elif PAID>12:
                                total_amount=90*PAID
                                break
                        room_number=random.choice(pod)
                        room_rate="pods"
                    elif room_type==5:
                        break
                    

                    intial=total_amount+d
                    GST=intial*(5/100)
                    total_amount=GST+intial
                
                    print(f"amount need to be paid in advance should be {(total_amount+d)*0.5} ")
                    advance_pay=total_amount*0.5
                    remaining_pay=total_amount-advance_pay
                    while True:
                        try:
                            PAID=int(input("Enter 1(IF PAID ADVANCE AMOUNT) OR Enter 0"))
                            if PAID==1:
                                print(f"your balance payment is {remaining_pay}")
                                break
                            else:
                                print("PLEASE PAY AMOUNT AND ENTER 1")
                        except ValueError:
                            print("INVALID. PLEASE RE ENTER CORRECT ONES")
                    print(" CONGRATULATIONS!!! your room has been booked ")
                    print(f"YOUR ROOM NUMBER IS {room_number}")
                    ROOM_DETAILS={"NAME":name,"ADHAAR_NO":y,"ROOM_NO":room_number,"ROOM_TYPE":room_type,"TOTAL_AMOUNT":total_amount,"AMOUNT_PAID":advance_pay,"BALANCE":remaining_pay}
                    print(ROOM_DETAILS)
                    break
    elif Selection==3:
        while True:
            print("1.CONTINUE")
            print("2.EXIT")
            f=True
            while True:
                try:
                    option1=int(input("PLEASE INPUT YOUR OPTION"))
                    break
                except ValueError:
                    print("please enter valid input ")
            if option1==1:
                while True:
                    f=True
                    while True:
                        try:
                            W=int(input("IF YOU BOOKED PREVIOUSLY ENTER 1 or ENTER 0"))
                            if W==1:
                                extend=int(input("Please enter days of extention if room . if pods enter hours of extention"))
                                room_number_extended=int(input("please enter your previous room number "))
                                break
                            else:
                                print("PLEASE BOOK THE ROOM TO EXTEND ") 
                                f=False

                                break
                        except ValueError:
                            print("ENTER VALID LITERAL")
                    if f==False:
                        break
                    if room_number_extended==ROOM_DETAILS["ROOM_NO"]:
                        new_amount=extend*rooms[room_rate]
                        print(new_amount)
                    else:
                        print("SORRY! YOUR ROOM NUMBER IS NOT FOUND .EXTENSION ALLOWED ONLY AFTER BOOKING.")
                        break
                    while True:
                        try:
                            P=int(input("IF AMOUNT PAID ENTER 1")) 
                            if P==1:
                                print("YOUR STAY IS SUCCESSFULLY EXTENDED!!!")
                                break  
                                
                            else:
                                print("PLEASE PAY THE AMOUNT TO PROCEED")     
                        except ValueError:
                            print("INVALID LITERAL")
                    if f==True:
                        break
            elif option1==2:
                break

    elif Selection==4:
        while True:
            print("1.CHECKOUT")
            print("2.EXIT")
            while True:
                try:
                    option=int(input("Please enter your option :"))
                    break
                except ValueError:
                    print("please enter valid input")
            if option==1:
                    while True:
                        try:
                            a=int(input("PLEASE ENTER YOUR ROOM NUMBER :"))
                            if a==ROOM_DETAILS["ROOM_NO"]:
                                print("====BILL====")
                                for values,items in ROOM_DETAILS.items():
                                    print(values,"=",items)
                                print(f"YOUR REMAINING AMOUNT IS {remaining_pay}")
                            else:
                                print("you haven't booked any room please book room")
                        except ValueError:
                            print("please enter valid input")
                        while True:
                            try:
                                PAID=int(input("IF YOU HAD PAID ENTER [1]"))
                                if PAID==1:
                                    print("PLEASE VISIT AGAIN . THANK FOR COMING")
                                    break
                                else:
                                    print("please pay remaining amount")
                            except ValueError:
                                print("please enter valid input")
                        break
                    
            elif option==2:
                break
                    
    elif Selection==5:
        print("BYE, HAVE A NICE DAY")
        break
        
        

       

            




                
                
                    

                



                        

                

                


                