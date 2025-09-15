from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def start_page():
    return render_template('index.html')

@app.route('/blog')
def show_blog():
    return render_template('blog.html')

@app.route('/contacts')
def show_contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run()
