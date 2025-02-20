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

def calculate_monthly_pay(wk_1_hours, wk_2_hours, wk_3_hours, wk_4_hours, pay_per_hour):
    week1_pay = calculate_pay(wk_1_hours, pay_per_hour)
    week2_pay = calculate_pay(wk_2_hours, pay_per_hour)
    week3_pay = calculate_pay(wk_3_hours, pay_per_hour)
    week4_pay = calculate_pay(wk_4_hours, pay_per_hour)
    return week1_pay + week2_pay + week3_pay + week4_pay

print(calculate_monthly_pay(40,50,35,40,50))