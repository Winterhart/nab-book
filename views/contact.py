from flask import Blueprint, make_response, jsonify


class Contact():
    contact = Blueprint('contact', __name__, url_prefix='/api')

    @contact.route('/contacts', methods=['GET'])
    def get_contacts():
        return "contacts"
