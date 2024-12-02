from flask import Blueprint, request, jsonify
from app.models import db, Patient

patient_blueprint = Blueprint('patients', __name__)

@patient_blueprint.route('/patients', methods=['POST'])
def add_patient():
    data = request.get_json()
    new_patient = Patient(
        name=data['name'],
        age=data['age'],
        medical_history=data.get('medical_history'),
        prescriptions=data.get('prescriptions'),
        lab_results=data.get('lab_results')
    )
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({'message': 'Patient added successfully'}), 201

@patient_blueprint.route('/patients/<int:id>', methods=['GET'])
def get_patient(id):
    patient = Patient.query.get_or_404(id)
    return jsonify({
        'id': patient.id,
        'name': patient.name,
        'age': patient.age,
        'medical_history': patient.medical_history,
        'prescriptions': patient.prescriptions,
        'lab_results': patient.lab_results
    })
