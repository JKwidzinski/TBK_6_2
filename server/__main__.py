from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "eShop Sample Application"

@app.route('/catalog')
def catalog():
    list = [
        { "id": 1, "name": "Mountanbike Driftwood 24\"", "unitPrice": 199 },
        { "id": 2, "name": "Tribal 100 Flat Bar Cycle Touring Road Bike", "unitPrice": 300 },
        { "id": 3, "name": "Siech Cycles Bike (58 cm)", "unitPrice": 459 }
    ]
    return json.dumps(list)

@app.route('/checkout')
def checkout():
    return "Starting checkout of your shopping cart..."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)