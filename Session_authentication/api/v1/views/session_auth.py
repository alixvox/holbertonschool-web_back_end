#!/usr/bin/env python3
"""
SessionAuth view
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from api.v1.app import auth
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """
    Handles the POST /auth_session/login route.
    Retrieves email and password parameters from the request form.
    Returns a JSON response with an error message and status code 400
    if either parameter is missing.
    Retrieves the User instance based on the email.
    Returns a JSON response with an error message and status code 404
    if no User is found.
    Checks if the password is correct.
    Returns a JSON response with an error message and status code 401
    if the password is not correct.
    Otherwise, creates a Session ID for the User ID, sets the cookie
    to the response, and returns the dictionary representation of the User.
    """

    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400

    users = User.search({'email': email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user.id)
    response = jsonify(user.to_json())
    response.set_cookie(getenv('SESSION_NAME'), session_id)
    return response
