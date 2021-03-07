from flask import Flask

app = Flask(__name__)

@app.route('/')     #home route
def home():
    return "Hello World"

#POST /store creating store
@app.route('/store', methods=['POST'])
def create_store():
    pass

#GET /store/:name getting store
@app.route('/store/<string:name>')
def get_store(name):
    pass

#GET /store getting all stores
@app.route('/store')
def get_stores():
    pass

#POST creating item in store
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass

#GET /store/:name/item getting item from store
@app.route('/store/<string:name>/item')
def get_items_in_stores(name):
    pass

app.run(port=9001)