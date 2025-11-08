from app import app, render_template


@app.route('/blog')
def blog():  # put application's code here
    return render_template('blog.html')
