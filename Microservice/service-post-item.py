from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
# import jwt
import data_item as us

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def add():
    # Get the information from the request
    category = request.form.get('category')
    name = request.form.get('name')
    price = request.form.get('price')
    instock = request.form.get('instock')

    us.add_item(category,name,price,instock)
    return jsonify({'message': 'Created successfully!'}), 202

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True) #127.0.0.1