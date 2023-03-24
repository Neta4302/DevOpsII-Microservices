from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
# import jwt
import data_item as us

app = Flask(__name__)

@app.route('/put/<id>', methods=['PUT'])
def update(id):
    # Get the information from the request
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    _item = us.update_item(id,category,name,price,instock)
    return jsonify(_item), 203

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True) #127.0.0.1