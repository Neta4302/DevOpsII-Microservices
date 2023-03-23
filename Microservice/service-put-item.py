from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
# import jwt
import data_item as us

app = Flask(__name__)

@app.route('/put/<category>', methods=['PUT'])
def update(category):
    # Get the information from the request
    name = request.form.get('name')
    price = request.form.get('price')
    instock = request.form.get('instock')

    us.update_item(category,name,price,instock)
    return jsonify({'message': 'Updated successfully!'}), 203

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True) #127.0.0.1