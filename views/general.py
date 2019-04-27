from flask import Blueprint, make_response, jsonify


main = Blueprint('main', __name__, url_prefix='')

@main.route('/')
def main_page():
    """ Writing first basic route """ 
    return make_response(jsonify({"message": "Welcome to NAB Book"}), 200)

@main.errorhandler(500)
def error():
    """ Hiding all 500 Error from user """ 
    return make_response(jsonify({"error": " Not Foudn"}), 404)