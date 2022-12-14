from flask import Blueprint, jsonify, request

bpMain = Blueprint('bpMain', __name__)

@bpMain.route('/')
def main():
    return jsonify({
        "message": "Welcome to JM STAR WARS REST API"
    }), 200