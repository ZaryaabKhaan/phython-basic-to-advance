print("=========================================")
print("      EMPLOYEE PAYROLL REPORT")
print("=========================================")

# Input
employee_id = input("Enter Employee ID: ")
employee_name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: "))
overtime_hours = float(input("Enter Overtime Hours: "))
overtime_rate = float(input("Enter Overtime Rate: "))
performance_score = int(input("Enter Performance Score: "))
tax_percentage = float(input("Enter Tax Percentage: "))

# Arithmetic Operators
overtime_pay = overtime_hours * overtime_rate
gross_salary = basic_salary + overtime_pay
tax_amount = gross_salary * tax_percentage / 100
net_salary = gross_salary - tax_amount

# Assignment Operators
net_salary += 0
net_salary -= 0
net_salary *= 1
monthly_salary = net_salary
monthly_salary /= 12
monthly_salary //= 1
monthly_salary %= 100000

# Ternary Operator
status = "Eligible for Bonus" if performance_score >= 80 else "Not Eligible"

# Output
print("\n=========================================")
print("      EMPLOYEE PAYROLL REPORT")
print("=========================================")

print(f"Employee ID        : {employee_id}")
print(f"Employee Name      : {employee_name}\n")

print(f"Basic Salary       : ${basic_salary:.2f}")
print(f"Overtime Pay       : ${overtime_pay:.2f}")
print(f"Gross Salary       : ${gross_salary:.2f}")
print(f"Tax Amount         : ${tax_amount:.2f}")
print(f"Net Salary         : ${net_salary:.2f}\n")

print(f"Performance Score  : {performance_score}")
print(f"Performance Status : {status}\n")

print(f"Monthly Salary     : ${net_salary/12:.2f}")

print("=========================================")