#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    # do NOT include test users here when you push your code
    # e.g. "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}

}

@app.route("/")
def home():
    return f"Welcome to the Flask API!"

@app.route("/data", methods=['GET'])
def return_json():
    usernames = list(users.keys())
    return jsonify(usernames)

@app.route("/status", methods=['GET'])
def return_status():
    return f'OK'

@app.route("/users/<username>", methods=['GET'])
def return_user(username):
    user = users.get(username)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    # Merge username into the response payload
    response = {'username': username, **user}
    return jsonify(response), 200

@app.route("/add_user", methods=['POST'])
def add_user():
    data = request.get_json(force=True)
    username = data.get('username')
    if not username:
        return jsonify({'error': 'Username is required'}), 400

    user_record = {
            'name': data.get('name'),
            'age': data.get('age'),
            'city': data.get('city'),
        }

    users[username] = user_record

    return jsonify({
        'message': f'user "{username}" added.',
        'user': user_record
        }), 201


if __name__ == "__main__": app.run()
