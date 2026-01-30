def india_tax(amount):
    return amount * 0.18 
def usa_tax(amount):
    return amount * 0.07  
def europe_tax(amount):
    return amount * 0.20
def generate_bill(amount, tax_rule):
    tax = tax_rule(amount)
    total = amount + tax
    return {
        "Base Amount": amount,
        "Tax": tax,
        "Total Amount": total
    }
def get_tax_rule(region):
    tax_rules = {
        "india": india_tax,
        "usa": usa_tax,
        "europe": europe_tax
    }
    return tax_rules.get(region.lower())
def main():
    print("=== Multi-Region Billing System ===")
    amount = float(input("Enter base amount: "))
    print("Available Regions: India, USA, Europe")
    region = input("Enter region: ")
    tax_rule = get_tax_rule(region)
    if tax_rule is None:
        print("Invalid region selected!")
        return
    bill = generate_bill(amount, tax_rule)
    print("\n--- Bill Details ---")
    for key, value in bill.items():
        print(f"{key}: {value:.2f}")
if __name__ == "__main__":
    main()