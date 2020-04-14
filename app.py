from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    r = requests.get(url='http://localhost:5000/hello')
    r = r.json()
    print(r['s'])
    return r['s']

@app.route('/hello')
def another_hello_world():
    return {'s': 'hello'}