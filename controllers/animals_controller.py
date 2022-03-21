from logging import NOTSET
from flask import Flask, render_template, request, redirect, Blueprint
from repositories import vet_repository, animal_repository
from models.vet import Vet
from models.animal import Animal

animals_blueprint = Blueprint("animals", __name__)

@animals_blueprint.route('/animals')
def animals_menu():
    return render_template('animals/index.html')

@animals_blueprint.route('/animals/animals_all')
def animals_all():
    animals = animal_repository.select_all()
    return render_template('animals/all_animals.html', animals=animals)

@animals_blueprint.route('/animals/delete_all')
def delete_all_animals():
    animal_repository.delete_all()
    return redirect('/')

@animals_blueprint.route('/animals/<id>')
def display_an_animal(id):
    animal =animal_repository.select(id)
    
    return render_template('animals/an_animal.html', animal=animal)

@animals_blueprint.route('/animals/<id>/delete', methods = ["POST"])
def delete_animal(id):
    animal_repository.delete(id)
    return redirect('/animals/animals_all')

@animals_blueprint.route('/animals/new')
def new_animal_form():
    vets= vet_repository.select_all()
    return render_template('animals/new.html', vets=vets) #, vets=vets

@animals_blueprint.route('/animals', methods = ["POST"])
def create_animal():
    name = request.form["pet-name"]
    dob = request.form["dob"]
    type = request.form["type"]
    vet_id = request.form["vet_id"]
    contact = request.form["contact"]
    notes = request.form["notes"]
    vet = vet_repository.select(vet_id)
    animal = Animal(name, dob, type, contact, notes, vet)
    animal_repository.save(animal)

    return redirect('/animals/animals_all')

@animals_blueprint.route("/animals/<id>/edit", methods = ["GET"])
def edit_animal(id):
    animal = animal_repository.select(id)
    vets = vet_repository.select_all()
    return render_template("animals/edit.html", animal = animal, vets=vets)

@animals_blueprint.route("/animals/<id>", methods = ["POST"])
def update_animal(id):
    name = request.form["pet-name"]
    dob = request.form["dob"]
    type = request.form["type"]
    contact = request.form["contact"]
    notes = request.form["notes"]
    vet_id = request.form["vet_id"]
    vet = vet_repository.select(vet_id)
    animal = Animal(name,dob, type, contact, notes, vet, id)
    animal_repository.update(animal)
    return redirect('/animals/animals_all')