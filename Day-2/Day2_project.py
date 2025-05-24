print("Welcome to the tip calculator!")
total_bill = int(input("What was the total bill? "))
tip_percentage = int(input("How much tip would you like to give? 10 , 12, or 15? "))
number_of_people = int(input("How many people to split the bills? "))

total_tip = total_bill * tip_percentage/100
print(total_tip)
total_amount = total_bill + total_tip
print(total_amount)

total = total_amount / number_of_people
print(f"Each person should pay {total}")
print("Each person should pay: " + str(round(total, 2)))