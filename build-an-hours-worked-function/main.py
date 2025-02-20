# Write function here
def calculate_pay(hours_worked, pay_per_hour):
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_pay = 40 * pay_per_hour
        overtime_pay = overtime_hours * pay_per_hour * 2
        return regular_pay + overtime_pay
    return hours_worked * pay_per_hour

# Worked 36 hours at $18 an hour
print(calculate_pay(36,18))
# Worked 60 hours at $25 an hour
print(calculate_pay(60,25))
# Worked 20 hours at $8 an hour
print(calculate_pay(20,8))
