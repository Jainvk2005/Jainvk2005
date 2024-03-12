## First API 
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Let us Reach 200 CEs together.'
