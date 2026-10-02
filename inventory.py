def calculate_total(price, quantity):
    return price * quantity

products = [{"name": "cake", "price": 1000.00, "quantity": 10}, 
            {"name": "yogurt", "price": 2500.00, "quantity": 15}, 
            {"name": "fishrolls", "price": 1000.00, "quantity": 20},
            {"name": "lemonade", "price": 3000.00, "quantity": 25}
            ]

total_value = 0
final_total = 0

for product in products:
    total_value = calculate_total (product['price'], product['quantity'])
    final_total = final_total + total_value
    print(f"{product['name']}: {product['quantity']} units at ₦{product['price']} = ₦{total_value}")

    if product['quantity'] <= 5:
        print("Low stock")

print(f"Total value = {final_total}")




# def greetings(name):
#      print(f"Hello! {name}")

# greetings("Nuur")
# greetings("Layl")
# greetings("Aden")


# # def add_numbers(a, b):
# #      return a + b

# # result = add_numbers(3, 5)
# # print(result)


# def add_number2(a, b):
#     print(a + b)

# result = add_number2(3, 5)
# print(result)