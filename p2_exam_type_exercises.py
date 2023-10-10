def calculate_discount(category, units):
    base_discounts = {'A': 0.10, 'B': 0.05, 'C': 0.02}
    additional_discount = 0.05 if units > 10 else 0
    
    return base_discounts.get(category, 0) + additional_discount

def main():
    price = float(input("Enter the price of the product: "))
    category = input("Enter the category (A, B, or C): ").upper()
    units = int(input("Enter the number of units purchased: "))
    
    discount = calculate_discount(category, units)
    final_price = price - (price * discount)
    
    print(f"Price before discount: ${price:.2f}")
    print(f"Discount applied: {discount * 100:.0f}%")
    
    if units > 10:
        print("Additional discount applied (more than 10 units): 5%")
    
    print(f"Final price after discounts: ${final_price:.2f}")

if __name__ == "__main__":
    main()
