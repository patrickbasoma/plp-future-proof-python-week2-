
# Simple Bill Calculator
# This program calculates the total cost of items.

print("Simple Bill Calculator")

# Ask the user to enter the price and quantity
price = float(input("Enter the price of one item: "))
quantity = int(input("Enter the quantity: "))

# Calculate the total bill
total = price * quantity

# Display the bill summary using an f-string
print("\n----- Bill Summary -----")
print(f"{quantity} items at {price:.2f} each = {total:.2f}")
