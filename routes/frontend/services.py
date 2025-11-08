from app import app, render_template


@app.route('/services')
def services():  # put application's code here
    return render_template('services.html')
