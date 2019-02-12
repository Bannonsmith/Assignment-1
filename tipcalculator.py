total_amount = input("Enter the total amount")

tip_percentage_amount = input("Enter the tip percentage amount")

def calculate_tip_amount(amount,tip):
    tip_decimal = float(tip) / 100
    tip = float(amount) * tip_decimal
    return tip

print(calculate_tip_amount(total_amount,tip_percentage_amount))
