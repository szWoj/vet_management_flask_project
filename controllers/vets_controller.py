from flask import Flask, render_template, request, redirect, Blueprint
from repositories import vet_repository, animal_repository
from models.vet import Vet
from models.animal import Animal

vets_blueprint = Blueprint("vets", __name__)

@vets_blueprint.route('/vets')
def vets_menu():
    return render_template('vets/index.html')

@vets_blueprint.route('/vets/vets_all')
def vets_all():
    vets = vet_repository.select_all()
    return render_template('vets/all_vets.html', vets=vets)

@vets_blueprint.route('/vets/delete_all')
def delete_all_vets():
    vet_repository.delete_all()
    return redirect('/')

@vets_blueprint.route('/vets/<id>')
def display_a_vet(id):
    vet =vet_repository.select(id)
    return render_template('vets/a_vet.html', vet=vet)