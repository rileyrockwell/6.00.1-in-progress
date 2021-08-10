#User input
annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the portion of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))

#State variables
portion_down_payment = 0.25
annual_return = 0.04
down_payment = total_cost * portion_down_payment
monthly_income = annual_salary/12
monthly_income_saved = monthly_income * portion_saved
months = 0
current_savings = 0

#Number of months required for down payment
while down_payment > current_savings:
    current_savings += monthly_income_saved + current_savings * (0.04 / 12)
    months += 1

print("Number of months: ", months)