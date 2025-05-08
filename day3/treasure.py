#Treasure Hunt
print("Welcome to the Treasure Hunt!")
direction = input("Which direction do you want to go? (left/right) ").lower()   
if direction=="right":
    print("You fell into a hole. Game over.")
else:
    print("You can proceed to the next step.")
    action=input("what do you want to do ? (swim/wait)").lower()
    if action =="swim":
        print("You were eaten by a shark,GameOver")
    else:
        print("You can proceed to the next step.")
        door=input("Which door do you want to open? (red/blue/yellow)").lower()
        if door=="red":
            print("You were burned by fire,GameOver")
        elif door=="blue":
            print("You were eaten by a beast,GameOver")
        elif door=="yellow":
            print("You found the treasure! You win!")
        else:
            print("Game Over. You chose a door that doesn't exist.")