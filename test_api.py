import requests
import json

def test_api():
    base_url = 'http://localhost:5000'
    
    print("\n=== Testing Chatbot API ===\n")
    
    # Test 1: Chat endpoint with product query
    print("Test 1: Chat about products")
    chat_response = requests.post(
        f'{base_url}/api/chat',
        json={"message": "Tell me about your products"}
    )
    print(f"Status Code: {chat_response.status_code}")
    print(f"Response: {chat_response.json()}\n")

    # Test 2: Chat endpoint with price query
    print("Test 2: Chat about prices")
    chat_response = requests.post(
        f'{base_url}/api/chat',
        json={"message": "What are your prices?"}
    )
    print(f"Status Code: {chat_response.status_code}")
    print(f"Response: {chat_response.json()}\n")

    # Test 3: Get all products
    print("Test 3: Get all products")
    products_response = requests.get(f'{base_url}/api/products')
    print(f"Status Code: {products_response.status_code}")
    print(f"Response: {products_response.json()}\n")

    # Test 4: Get products by category
    print("Test 4: Get products by category")
    category_response = requests.get(f'{base_url}/api/products/category/electronics')
    print(f"Status Code: {category_response.status_code}")
    print(f"Response: {category_response.json()}\n")

if __name__ == '__main__':
    try:
        test_api()
        print("✅ All tests completed!")
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to the server. Make sure the Flask app is running on http://localhost:5000")
