from app import app, render_template
import requests

@app.route('/shop')
@app.route('/shop')
def shop():

    response = requests.get('https://fakestoreapi.com/products')
    response.raise_for_status()
    data = response.json()

    return render_template('shop.html', products=data)
