from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.66,
            }
        ]
    }
]

@app.route('/')     #home route
def home():
    return "Hello World"

#POST /store creating store
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name':request_data['name'],
        'items':[]
    }
    store.append(new_store)
    return jsonify(new_store)

#GET /store/:name getting store
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'store':store})
    return jsonify({'message': 'Store not found'})

#GET /store getting all stores
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})

#POST creating item in store
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                name: request_data['name'],
                price: request_data['price']
            }
            store['item'].append(new_item)
            return jsonify({'item': new_item})
    return jsonify({'message': 'Store not found'})

#GET /store/:name/item getting item from store
@app.route('/store/<string:name>/item')
def get_items_in_stores(name):
    for store in stores:
        if(store['name'] == name):
            return jsonify({'items': store['items']})
    return jsonify({'message': 'Store not found'})

app.run(port=9001)