from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
# import jwt
import data_item as us

app = Flask(__name__)

item = us.item_name()

@app.route('/delete/<category>', methods=['DELETE'])
def delete(category):
    us.delete_item(category)
    return jsonify({'message': 'Delete successfully!'}), 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True) #127.0.0.1