input_data = {
    "products": [
        {"id": 1, "name": "Pizza", "category": "Italian", "price": 12.99},
        {"id": 2, "name": "Sushi", "category": "Japanese", "price": 24.99},
        {"id": 3, "name": "Burger", "category": "American", "price": 8.99},
        {"id": 4, "name": "Pad Thai", "category": "Thai", "price": 14.99}
    ]
}

# 1. Write a function that takes the JSON data as input and returns a list of names of all products.
def get_all_product_names(data):
    return [product['name'] for product in data['products']]

# 2. Write a function that takes the JSON data as input and a price threshold, and returns a list of products which price is greater than or equal to the threshold.
def get_all_products_above_price(data, threshold):
    return [product for product in data['products'] if product['price'] >= threshold]

# Task 1
all_product_names = get_all_product_names(input_data)
print("Task 1. Names of all products:", all_product_names)

# Task 2
threshold_price = 14
products_above_threshold = get_all_products_above_price(input_data, threshold_price)
print(f"Task 2. Products with price greater than or equal to ${threshold_price}:")
for product in products_above_threshold:
    print(product)
