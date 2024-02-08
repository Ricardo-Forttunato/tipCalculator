print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $ " ))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip = bill * (percentage / 100)
total_bill = bill + tip
final_amount = total_bill / people

print(f"Each person should pay: ${final_amount:.2f}")