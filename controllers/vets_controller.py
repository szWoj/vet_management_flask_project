from unicodedata import name
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

@vets_blueprint.route('/vets/<id>/delete', methods = ["POST"])
def delete_vet(id):
    vet_repository.delete(id)
    return redirect('/vets/vets_all')

@vets_blueprint.route('/vets/new')
def new_vet_form():

    return render_template('vets/new.html')

@vets_blueprint.route('/vets', methods = ["POST"])
def create_vet():
    name = request.form["vet-name"]
    contact = request.form["contact"]
    status = request.form["status"]

    vet = Vet(name, contact, status)
    vet_repository.save(vet)

    return redirect('/vets/vets_all')

@vets_blueprint.route("/vets/<id>/edit", methods = ["GET"])
def edit_vet(id):
    vet = vet_repository.select(id)
    
    return render_template("vets/edit.html", vet = vet)

@vets_blueprint.route("/vets/<id>", methods = ["POST"])
def update_vet(id):
    name = request.form["name"]
    contact = request.form["contact"]
    status = request.form["status"]

    vet = Vet(name, contact, status, id)
    vet_repository.update(vet)
    return redirect('/vets/vets_all')
