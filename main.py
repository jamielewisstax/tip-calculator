print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $ "))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
people_count = int(input("How many people to split the bill? "))

split = total_bill / people_count * ( tip_percentage / 100 + 1)
final_split = round(split, 2)
print(f"Each person should pay: $ {final_split}")