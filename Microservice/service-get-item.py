from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
# import jwt
import data_item as us

app = Flask(__name__)

@app.route('/item', methods=['GET'])
def item():
    _item = us.item_name()
    return jsonify(_item), 201

@app.route('/item/<id>', methods=['GET'])
def item_f(id):
    _item = us.find_item(id)
    return jsonify(_item), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True) #127.0.0.1