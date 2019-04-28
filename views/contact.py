from flask import Blueprint, make_response, jsonify, request
from datasource.database import db
from models.contact import Contact
from util.data_to_json import row2dict
from util.uuid_generator import UuidGenerator


class ContactView:
    contact = Blueprint('contact', __name__, url_prefix='/api')

    @contact.route('/contacts', methods=['GET'])
    def get_contacts():
        try:
            contacts = Contact.query.all()
            db.session.close()
            json_data = [row2dict(c) for c in contacts]
            return make_response(jsonify({"contacts":json_data}), 200)
        except Exception as error:
            db.session.rollback()
            db.session.close()
            print(error)
            return make_response(jsonify({"error": "Not Found"}), 404)


    @contact.route('/contacts/submit', methods=['POST'])
    def create_contact():
        """ Creating a contact and saving in storage """
        try:
            content = request.get_json()

            name = content['name']
            phone = None
            address = None
            email = None
            # If phone is not null take it
            if 'phone' in content:
                phone = content['phone']

            if 'address' in content:
                address = content['address']

            if 'email' in content:
                email = content['email']

            # If name is empty cancel transaction
            if not name:
                raise Exception("Pre-requisite not respected")

            # Any other fields can be empty
            uid = UuidGenerator().generate_uuid()
            new_contact = Contact(id=uid, name=name, phone=phone, address=address, email=email)
            db.session.add(new_contact)
            db.session.commit()

            return make_response(jsonify({"message": "Successful handling."}), 200)
            
        except Exception as error:
            db.session.rollback()
            db.session.close()
            print(error)
            return make_response(jsonify({"error": "Not Found"}), 404)
