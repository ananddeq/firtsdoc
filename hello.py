from flask import Flask, request, jsonify
app = Flask(__name__)
stores = [
    {
        'name': 'beautiful store',
        'items': [
            {
                'name': 'flowers',
                'price': 100
            }
        ]
    },
    {
        'name': 'beautiful store 2',
        'item': [
            {
                'name': 'books',
                'price': 100
            }
        ]
    }
]


@app.route('/')
def home():
    return "hey"


@app.route('/store')
def get_all_store_name():
    return jsonify({'stores': stores})


@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['name'])
    return jsonify({'message': 'Store not found'})


@app.route('/store/<string:name>/item')
def get_store_items(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
    return jsonify({'message': 'Item not found'})


@app.route('/store', methods=['POST'])
def create_store():
    req_data = request.get_json()
    new_store = {
        'name': req_data['name'],
        'item': []
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_item(name):
    for store in stores:
        if store['name'] == name:
            req_data =request.get_json()
            new_item = {
                'name': req_data['name'],
                'price': req_data['price']
            }
            store['item'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'Item not found'})


