from app import app, render_template
import requests

@app.route('/')
@app.route('/home')
def home():
    # Slider product
    slider_product = None
    try:
        slider_res = requests.get('https://fakestoreapi.com/products/18')
        slider_res.raise_for_status()
        slider_product = slider_res.json()
    except (requests.exceptions.RequestException, ValueError) as e:
        print("Slider product fetch error:", e)

    # All products
    womens_clothing = []
    try:
        response = requests.get('https://fakestoreapi.com/products')
        response.raise_for_status()
        products = response.json()
        womens_clothing = [p for p in products if p['category'] == "women's clothing"][:3]
    except (requests.exceptions.RequestException, ValueError) as e:
        print("Products fetch error:", e)

    return render_template('index.html', products=womens_clothing, slider_product=slider_product)