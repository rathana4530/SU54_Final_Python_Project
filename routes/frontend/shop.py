from app import app, render_template
import requests

@app.route('/shop')
def shop():  # put application's code here
    response = requests.get('https://fakestoreapi.com/products')
    data = response.json()
    products = data
    return render_template('shop.html', products=products)
