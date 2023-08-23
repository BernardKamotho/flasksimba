from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return  render_template('index.html')

@app.route('/about')
def about():
    return('this is the about us page')

@app.route('/contact')
def contact():
    return('this is the contact us page')

if __name__ == '__main__':
    app.run(debug=True)