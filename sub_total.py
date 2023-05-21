def calculate_total():
    products = {
        "Product A": 20,
        "Product B": 40,
        "Product C": 50
    }

    quantities = {}
    wrapped_products = {}


    for product in products:
        quantity = int(input(f"Enter the quantity of {product}: "))
        wrapped = input(f"Is {product} wrapped as a gift? (yes/no): ").lower() == "yes"

        quantities[product] = quantity
        wrapped_products[product] = wrapped


    subtotal = 0
    for product, quantity in quantities.items():
        subtotal += products[product] * quantity

    # Apply discount rules
    discount_name = ""
    discount_amount = 0

    # Check for "flat_10_discount"
    if subtotal > 200:
        discount_name = "flat_10_discount"
        discount_amount = 10

    # Check for "bulk_5_discount"
    for product, quantity in quantities.items():
        if quantity > 10:
            discount_name = "bulk_5_discount"
            discount_amount = products[product] * quantity * 0.05
            break

    # Check for "bulk_10_discount"
    total_quantity = sum(quantities.values())
    if total_quantity > 20:
        discount_name = "bulk_10_discount"
        discount_amount = subtotal * 0.1

    # Check for "tiered_50_discount"
    if total_quantity > 30:
        for product, quantity in quantities.items():
            if quantity > 15:
                discount_name = "tiered_50_discount"
                discount_amount = products[product] * (quantity - 15) * 0.5
                break

    # Calculate shipping fee and gift wrap fee
    shipping_fee = (total_quantity // 10) * 5
    gift_wrap_fee = sum(quantities.values())

    # Calculate total
    total = subtotal - discount_amount + shipping_fee + gift_wrap_fee

    # Output the details
    print("Product Details:")
    for product, quantity in quantities.items():
        print(f"{product}: Quantity: {quantity}, Total Amount: ${products[product] * quantity}")

    print("Subtotal: $", subtotal)

    if discount_name:
        print(f"Discount Applied: {discount_name}, Discount Amount: ${discount_amount}")

    print("Shipping Fee: $", shipping_fee)
    print("Gift Wrap Fee: $", gift_wrap_fee)
    print("Total: $", total)


calculate_total()




