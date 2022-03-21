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