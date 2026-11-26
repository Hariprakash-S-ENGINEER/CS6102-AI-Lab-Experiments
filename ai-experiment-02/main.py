# Electricity billing with progressive unit slabs
def calculate_bill(units):
    if units < 0:
        raise ValueError("Units cannot be negative")
    remaining = units
    bill = min(remaining, 100) * 1.50
    remaining = max(remaining - 100, 0)
    bill += min(remaining, 100) * 2.50
    remaining = max(remaining - 100, 0)
    bill += min(remaining, 300) * 4.00
    remaining = max(remaining - 300, 0)
    bill += remaining * 6.00
    return bill

customers = [("Arun", 350)]
for index, (name, units) in enumerate(customers, start=1):
    print(f"\nCustomer {index}")
    print("Customer Name :", name)
    print("Units         :", float(units))
    print("Bill Amount   : Rs.", round(calculate_bill(units), 2))
