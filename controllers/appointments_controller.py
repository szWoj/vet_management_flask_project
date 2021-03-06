from flask import Flask, render_template, request, redirect, Blueprint
from models.appointment import Appointment
from repositories import vet_repository, animal_repository, appointment_repository
from models.vet import Vet
from models.animal import Animal

appointments_blueprint = Blueprint("appointments", __name__)

@appointments_blueprint.route('/appointments/new')
def new_appointment_form():
    vets= vet_repository.select_all()
    animals = animal_repository.select_all()
    return render_template('appointments/new.html', vets=vets, animals=animals)

@appointments_blueprint.route('/appointments/appointments_all')
def appointments_all():
    appointments = appointment_repository.select_all()
    return render_template('appointments/appointments_all.html', appointments=appointments)

@appointments_blueprint.route('/appointments', methods = ["POST"])
def create_appointment():
    date = request.form["date"]
    time = request.form["time"]
    animal_id = request.form["animal_id"]
    vet_id = request.form["vet_id"]
    animal = animal_repository.select(animal_id)
    vet = vet_repository.select(vet_id)
    appointment = Appointment(date, time, vet, animal)
    appointment_repository.save(appointment)

    return redirect('/appointments/appointments_all')

@appointments_blueprint.route('/appointments/<id>/check_in', methods = ["POST"])
def check_in_appointment(id):
    appointment = appointment_repository.select(id)
    appointment.checked_in = True

    appointment_repository.check_in(appointment)
    return redirect('/appointments/appointments_all')

@appointments_blueprint.route('/appointments/delete_all')
def delete_all_appointments():
    appointment_repository.delete_all()
    return redirect('/')