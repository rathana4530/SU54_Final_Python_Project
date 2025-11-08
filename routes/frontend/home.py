from app import app, render_template
import requests

@app.route('/')
@app.route('/home')
def home():  # put application's code here
    response = requests.get('https://fakestoreapi.com/products/18')
    slider_product = response.json() if response.status_code == 200 else None

    # Get all products from Fake Store API
    response = requests.get('https://fakestoreapi.com/products')

    if response.status_code == 200:
        products = response.json()
        # Filter only "men's clothing"
        mens_clothing = [p for p in products if p['category'] == "women's clothing"]
        # Take only 3 items

        mens_clothing = mens_clothing[:3]
    else:
        mens_clothing = []

    return render_template('index.html', products=mens_clothing, slider_product=slider_product)
