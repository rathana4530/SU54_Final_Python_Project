from app import app, render_template


@app.route('/cart')
def cart():  # put application's code here
    return render_template('cart.html')