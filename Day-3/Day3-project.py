
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
turn = input('You\re at a cross road.  Where do you want to go?\n Type "left" or "right"\n')
if turn.casefold() == "left":
    lake = input('You\ve come to a lake. There is an island in the middle of the lake.\n Type "wait" to wait for a boat.  Type "swim"" to swim across\n')
    if lake.casefold() == "wait":
        door = input('Which door do you want to enter?\n Type "Red"" or "Yellow" or "Blue".\n')
        if door.casefold() == "yellow":
            print("You Win!")
        elif door.casefold() == "Red" or "Blue":
            print("Game Over")
        else:
            print("Wrong selection")
    else:
        print("Game over")
else:
    print("You fell in to a hole. Game over!!!")