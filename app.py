from flask import Flask, jsonify, request, render_template
from extensions import db, migrate, cors
from models.product import Product
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Configure CORS to allow all origins
    CORS(app, resources={
        r"/api/*": {
            "origins": "*",
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })

    # Register routes
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/api/products', methods=['GET'])
    def get_products():
        products = Product.query.all()
        return jsonify([{
            'id': product.id,
            'name': product.name,
            'category': product.category,
            'price': product.price,
            'description': product.description,
            'quantity_in_stock': product.quantity_in_stock
        } for product in products])

    @app.route('/api/products/category/<category>', methods=['GET'])
    def get_products_by_category(category):
        products = Product.query.filter_by(category=category).all()
        return jsonify([{
            'id': product.id,
            'name': product.name,
            'category': product.category,
            'price': product.price,
            'description': product.description,
            'quantity_in_stock': product.quantity_in_stock
        } for product in products])

    @app.route('/api/products/search', methods=['GET'])
    def search_products():
        name = request.args.get('name', '')
        products = Product.query.filter(Product.name.ilike(f'%{name}%')).all()
        return jsonify([{
            'id': product.id,
            'name': product.name,
            'category': product.category,
            'price': product.price,
            'description': product.description,
            'quantity_in_stock': product.quantity_in_stock
        } for product in products])

    @app.route('/api/chat', methods=['POST'])
    def chat():
        user_input = request.json.get('message', '')
        response = f"You said: {user_input}"
        return jsonify({"response": response})

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
