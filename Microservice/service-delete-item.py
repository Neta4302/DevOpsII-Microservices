from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
# import jwt
import data_item as us

app = Flask(__name__)

@app.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    _item = us.delete_item(id)
    return jsonify(_item), 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True) #127.0.0.1