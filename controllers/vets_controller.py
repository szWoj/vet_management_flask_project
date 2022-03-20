from flask import Flask, render_template, request, redirect, Blueprint
from repositories import vet_repository, animal_repository
from models.vet import Vet
from models.animal import Animal

vets_blueprint = Blueprint("vets", __name__)

@vets_blueprint.route('/vets')
def vets_menu():
    return render_template('vets/index.html')