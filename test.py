def percentage_amount(total, percentage):

    return total * percentage

def calc_total_bill(charge_amount, tax_rate, tip_percentage):

    bill_with_tax = charge_amount + percentage_amount(charge_amount, tax_rate)
    bill_with_tip = bill_with_tax + percentage_amount(bill_with_tax, tip_percentage)

    return bill_with_tax
    return bill_with_tip


x, y = calc_total_bill(100, 0.10, 0.10)
with_tax = x
with_tip = y
print with_tax, with_tip
