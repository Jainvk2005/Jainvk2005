##first API
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    name = "This is the route."
    return name

@app.route('/hello')
def hello():
    name = "Let us Reach 200 CEs together"
    return name

if __name__ == "__main__":
    app.run()
