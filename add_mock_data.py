from app import create_app
from models.product import Product
from extensions import db
import random

# Product data categories and options
categories = [
    'electronics', 'accessories', 'home appliances', 'furniture', 'toys', 'clothing', 'books',
    'beauty & personal care', 'sports & outdoors', 'automotive', 'food & beverages', 'pet supplies',
    'baby products', 'health & wellness', 'office supplies', 'gardening', 'jewelry & watches',
    'art & crafts'
]

names = [
    # Electronics
    'Smartphone', 'Laptop', 'Smart TV', 'Tablet', 'Bluetooth Speaker', 'Headphones', 'Smartwatch',
    # Accessories
    'Backpack', 'Sunglasses', 'Wallet', 'Handbag', 'Watch', 'Hat', 'Scarf',
    # Clothing
    'T-Shirt', 'Jeans', 'Jacket', 'Dress', 'Sweater', 'Shoes', 'Socks',
    # Food & Beverages
    'Chocolate Bar', 'Coffee', 'Tea', 'Energy Drink', 'Chips', 'Cookies', 'Cooking Oil',
    # Home Appliances
    'Washing Machine', 'Microwave Oven', 'Refrigerator', 'Toaster', 'Iron', 'Dishwasher',
    # Furniture
    'Sofa', 'Dining Table', 'Bed', 'Chair', 'Bookshelf', 'Desk', 'Wardrobe',
    # Toys
    'Action Figure', 'Puzzle', 'Doll', 'Building Blocks', 'Toy Car', 'Board Game',
    # Beauty & Personal Care
    'Shampoo', 'Face Cream', 'Lipstick', 'Perfume', 'Soap', 'Hair Dryer', 'Nail Polish',
    # Sports & Outdoors
    'Bicycle', 'Tennis Racket', 'Yoga Mat', 'Camping Tent', 'Dumbbells', 'Treadmill',
    # Automotive
    'Car Cover', 'Air Freshener', 'Jump Starter', 'Motorcycle Helmet', 'Car Vacuum',
    # Baby Products
    'Baby Bottle', 'Diapers', 'Crib', 'Stroller', 'Baby Monitor', 'Baby Clothes',
    # Gardening
    'Plant Pots', 'Garden Hose', 'Pruning Shears', 'Lawn Mower', 'Fertilizer',
    # Art & Crafts
    'Paint Set', 'Sketchbook', 'Easel', 'Craft Glue', 'Beads', 'Yarn',
    # Office Supplies
    'Notebook', 'Pen Set', 'Stapler', 'Desk Lamp', 'Filing Cabinet', 'Printer'
]

brands = [
    # Electronics & Appliances
    'Apple', 'Samsung', 'Sony', 'LG', 'Panasonic', 'Dell', 'HP', 'Lenovo', 'Microsoft',
    # Clothing & Accessories
    'Nike', 'Adidas', 'Puma', 'H&M', 'Zara', 'Levi\'s', 'Ray-Ban', 'Rolex',
    # Food & Beverages
    'Nestle', 'Cadbury', 'Pepsi', 'Coca-Cola', 'Lipton', 'Oreo', 'Domino\'s',
    # Beauty & Personal Care
    'Dove', 'L\'Oreal', 'Maybelline', 'Nivea', 'Himalaya', 'MAC', 'Revlon',
    # Sports & Outdoors
    'Decathlon', 'Reebok', 'Wilson', 'Yonex', 'Spalding', 'Under Armour',
    # Automotive
    'Bosch', 'Michelin', 'Bridgestone', 'Goodyear',
    # Baby Products
    'Pampers', 'Huggies', 'Fisher-Price', 'Graco',
    # Gardening
    'Gardena', 'Scotts', 'Fiskars', 'Ortho',
    # Office Supplies
    'Pilot', 'Staedtler', '3M', 'Post-it', 'Brother'
]

colors = [
    'Black', 'White', 'Silver', 'Gold', 'Rose Gold', 'Blue', 'Red', 'Green', 'Yellow', 'Orange',
    'Pink', 'Purple', 'Beige', 'Brown', 'Gray'
]

features = [
    # Electronics & Appliances
    'Wireless', 'Bluetooth', 'Touch Screen', '4K', 'HD', 'Smart', 'Portable', 'Energy Efficient',
    # Clothing
    'Cotton', 'Waterproof', 'Breathable', 'Lightweight',
    # Sports & Outdoors
    'Ergonomic Design', 'Weather Resistant', 'Shockproof', 'Adjustable',
    # Food & Beverages
    'Organic', 'Sugar-Free', 'Gluten-Free', 'High Protein',
    # Office & Art Supplies
    'Refillable', 'Eco-Friendly', 'Durable', 'Compact',
    # Gardening
    'Rustproof', 'UV Resistant', 'Heavy Duty'
]

descriptions = [
    'Latest technology with advanced features',
    'High performance and reliability',
    'Premium quality with elegant design',
    'Best-in-class performance',
    'Innovative design with cutting-edge technology',
    'Perfect for professionals and enthusiasts',
    'Enhanced user experience with smart features',
    'Superior quality with advanced functionality',
    'Next-generation technology integration',
    'Exceptional performance and durability',
    'Comfortable and stylish for everyday use',
    'Eco-friendly and sustainable design',
    'Lightweight and easy to use',
    'Affordable and high value for the price',
    'Made with premium materials'
]

def generate_mock_products(num_products=150):
    products = []
    for i in range(num_products):
        brand = random.choice(brands)
        base_name = random.choice(names)
        feature = random.choice(features)
        color = random.choice(colors)
        model_year = random.randint(2022, 2024)

        # Create a more detailed product name
        name = f'{brand} {base_name} {feature} {color} {model_year}'

        # Generate a more detailed description
        base_description = random.choice(descriptions)
        additional_info = f'Features {feature} technology, available in {color}'
        description = f'{base_description}. {additional_info}'

        product = {
            'name': name,
            'category': random.choice(categories),
            'price': round(random.uniform(99.99, 2999.99), 2),
            'description': description,
            'quantity_in_stock': random.randint(5, 500)
        }
        products.append(product)
    return products

def add_mock_data():
    app = create_app()
    with app.app_context():
        # Clear existing products
        Product.query.delete()
        
        # Generate and add new products
        products = generate_mock_products()
        for product_data in products:
            product = Product(
                name=product_data['name'],
                category=product_data['category'],
                price=product_data['price'],
                description=product_data['description'],
                quantity_in_stock=product_data['quantity_in_stock']
            )
            db.session.add(product)
        
        # Commit the changes
        db.session.commit()
        print("Successfully added 150 mock products to the database!")

if __name__ == '__main__':
    add_mock_data()
