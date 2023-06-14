treasure = input("You are at a crossroad. Where do you want to go? Type 'left' or 'right': ")

if treasure == "left" or treasure == "Left":
    lake = input("You came to a lake. There is an island in the middle of the lake. Do you need a boat or swim? Type 'boat' or 'swim': ")

    if lake == "wait" or lake == "Wait":
        door = input("There are 3 colored doors - red, blue, and yellow. Which one do you choose? Type the color: ")

        if door == "red" or door == "Red":
            print("Congratulations! You win!")
        elif door == "blue" or door == "Blue":
            print("GAME OVER")
        else:
            print("GAME OVER")

    else:
        print("GAME OVER")

else:
    print("GAME OVER")