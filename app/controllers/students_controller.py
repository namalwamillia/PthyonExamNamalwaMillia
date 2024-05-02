from flask import Blueprint, request, jsonify
from app.models.students import Student
from extensions import db, Bcrypt
import logging
from app.status_codes import (
    HTTP_400_BAD_REQUEST,
    HTTP_409_CONFLICT,
    HTTP_201_CREATED,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_401_UNAUTHORIZED,
    HTTP_200_OK,
)
from email_validator import validate_email, EmailNotValidError
from flask_jwt_extended import create_access_token
import logging
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity




student= Blueprint('student', __name__, url_prefix='/api/v2/student')


# User registration
@student.route('/register', methods=['POST'])
def register_students():
    try:
        data = request.get_json()

       

        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        contact = data.get('contact')
        

        # Check for existing user with the same email
        existing_student = student.query.filter_by(email=email).first()
        if existing_student:
            return jsonify({'error': 'Email already exists'}), 409

    

        # Create a new student instance
        new_student = student(
            first_name=first_name,
            last_name=last_name,
            email=email,
            contact=contact,
            
        )

        # Add the user to the database
        db.session.add(new_student)
        db.session.commit()

        return jsonify({'message': 'Student created successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500