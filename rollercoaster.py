print("Welcome to the rollercoaster")
height=int(input("What is your height in cm?\n"))
if height>=120:
    age=int(input("How old are you?\n"))
    if age<12 or age>45:
        print("You are not allowed to enter!")
    else:
        photo=input("Do you want to take a photo for additional $3?(Yes/No)\n").upper()
        if age >=12 and age<25: 
            bill=15
            if photo == "YES":
                bill+=3
                print(f"You should pay {bill}$")
            else:
                print(f"You should pay {bill}$")
        elif age>=25 and age<=45:
            bill=20
            if photo == "YES":
                bill+=3            
                print(f"You should pay {bill}$")
            else:
                print(f"You should pay ${bill}")
else:
    print("You are not tall enough to ride rollercoaster!")        