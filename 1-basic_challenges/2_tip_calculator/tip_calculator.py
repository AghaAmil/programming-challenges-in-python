# challenge intro
print("=============================")
print("Welcome to the Tip Calculator")
print("=============================\n")

# getting user's input
bill = float(input("Enter the total Bill: $"))
tip_percentage = float(input("Enter the tip in percentage (like 10%, 15%, 20%): "))
people = int(input("Enter the number of people to split the bill: "))

# calculation
total_bill = bill + (bill * tip_percentage / 100)
separate_bill = total_bill / people

# output
print(f"Each person should pay ${round(separate_bill, 2)}")
