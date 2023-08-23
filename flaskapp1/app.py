from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return 'Our first Flask website'
    
if __name__ == '__main__':
    app.run(debug=True)
