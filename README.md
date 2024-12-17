# E-Commerce API

A Flask-based RESTful API for an e-commerce platform with product management and chatbot features.

## Features

- Product Management (CRUD operations)
- Category-based filtering
- Product search functionality
- Mock data generation
- CORS enabled for cross-origin requests

## API Endpoints

- `GET /api/products`: Get all products
- `GET /api/products/category/<category>`: Get products by category
- `GET /api/products/search?name=<search_term>`: Search products by name
- `POST /api/chat`: Chatbot endpoint

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/nishantsevak11/EcommerceApi.git
cd EcommerceApi
```

2. Create and activate virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize database:
```bash
python create_db.py
python add_mock_data.py
```

5. Run the server:
```bash
python run.py
```

The server will start at `http://localhost:5000`

## Testing

Use Postman or any HTTP client to test the API endpoints:

1. Get all products:
   - GET `http://localhost:5000/api/products`

2. Search products:
   - GET `http://localhost:5000/api/products/search?name=Samsung`

3. Get products by category:
   - GET `http://localhost:5000/api/products/category/electronics`

## Technologies Used

- Flask
- SQLAlchemy
- Flask-CORS
- SQLite
