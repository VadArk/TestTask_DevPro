import pytest
from main import get_all_product_names, get_all_products_above_price

@pytest.fixture
def input_data():
    return {
        "products": [
            {"id": 1, "name": "Pizza", "category": "Italian", "price": 12.99},
            {"id": 2, "name": "Sushi", "category": "Japanese", "price": 24.99},
            {"id": 3, "name": "Burger", "category": "American", "price": 8.99},
            {"id": 4, "name": "Pad Thai", "category": "Thai", "price": 14.99}
        ]
    }

# Test 1 get_product_names function
def test_get_all_product_names(input_data):
    expected_names = ["Pizza", "Sushi", "Burger", "Pad Thai"]
    assert get_all_product_names(input_data) == expected_names

# Test 2 get_products_above_price function
def test_get_products_above_price(input_data):
    threshold_price = 14
    expected_products = [
        {"id": 2, "name": "Sushi", "category": "Japanese", "price": 24.99},
        {"id": 4, "name": "Pad Thai", "category": "Thai", "price": 14.99}
    ]
    assert get_all_products_above_price(input_data, threshold_price) == expected_products