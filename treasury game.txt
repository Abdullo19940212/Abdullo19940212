print("Welcome to Treasure Island Your mission is to find the treasure!")
side=input("Which side do you go? (left or right)\n").lower()
if side=="right":
    print("Game over")
elif side=="left":
    move=input("Do you swim or wait the boat?\n").lower()
    if move=="swim":
        print("Game over")
    elif move=="wait":
        door=input("Which door do you want to choose\n").lower()
        if door=="red" or door== "blue":
            print("Game over")
        elif door=="yellow":
            print("You have reached the treasure!")
        else:
            print("You have enter wrong option!")
    else:
        print("You have enter wrong option!")
else:
    print("You have enter wrong option!")