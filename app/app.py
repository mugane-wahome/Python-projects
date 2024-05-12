from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World! This is my first website using Flask.'

if __name__ == '__main__':
    app.run(debug=True)
