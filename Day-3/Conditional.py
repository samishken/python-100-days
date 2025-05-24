print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What's your age?\n"))
    if age < 12:
        bill = 5
        print("Please pay $5")
    elif age <= 18:
        bill = 7
        print("Please pay $7")
    #elif age >= 45 and age <= 55:
    elif 45 <= age <= 55:
        print("Everything is going to be ok.  is free")
    else:
        bill = 7
        print("Please pay $12")

    want_photo = input("Do you want to have a photo taken? Type y for Yes and n for No. ")
    if want_photo == "y":
        #Add $3 to their bill
        bill += 3
    print(f"Your final bill is {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")


