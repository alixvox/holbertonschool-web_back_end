#!/usr/bin/env python3
"""
Flask App.
"""
from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def welcome():
    """GET / route
    Returns:
        JSON payload: {"message": "Bienvenue"}
    """
    return jsonify({"message": "Bienvenue"}), 200


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token():
    """POST /reset_password route
    Returns a reset password token
    """
    email = request.form.get('email')

    try:
        reset_token = AUTH.get_reset_password_token(email)
    except ValueError:
        abort(403)

    return jsonify({"email": email, "reset_token": reset_token}), 200


@app.route('/sessions', methods=['POST'])
def login():
    """POST /sessions route
    Logs in a user and returns a JSON payload
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = make_response(
            jsonify({"email": email, "message": "logged in"}), 200
        )
        response.set_cookie("session_id", session_id)
        return response
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'])
def logout():
    """DELETE /sessions route
    Logs out a user
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)
    else:
        AUTH.destroy_session(user.id)
        return redirect('/')


@app.route('/profile', methods=['GET'])
def profile():
    """GET /profile route
    Returns a user profile
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)
    else:
        return jsonify({"email": user.email}), 200


@app.route('/reset_password', methods=['PUT'])
def update_password():
    """PUT /reset_password route
    Updates a user's password
    """
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')

    try:
        AUTH.update_password(reset_token, new_password)
    except ValueError:
        abort(403)

    return jsonify({"email": email, "message": "Password updated"}), 200


@app.route('/users', methods=['POST'])
def users():
    """POST /users route
    Registers a new user and returns a JSON payload
    """
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
