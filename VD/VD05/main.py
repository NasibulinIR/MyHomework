from flask import Flask, render_template
import os

app = Flask(__name__,
            template_folder=os.path.join(os.path.dirname(__file__), 'templates'))

@app.route('/')
def start_page():
    return render_template('home.html')

@app.route('/blog')
def show_blog():
    return render_template('blog.html')

@app.route('/contacts')
def show_contacts():
    return render_template('contacts.html')

@app.route('/about')
def show_about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
