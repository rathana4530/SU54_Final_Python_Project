from app import app, render_template


@app.route('/checkout')
def checkout():  # put application's code here
    return render_template('checkout.html')