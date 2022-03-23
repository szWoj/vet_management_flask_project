from flask import Flask, render_template
from controllers.animals_controller import animals_blueprint
from controllers.vets_controller import vets_blueprint
from controllers.appointments_controller import appointments_blueprint
from repositories import animal_repository, appointment_repository, vet_repository

app = Flask(__name__)

app.register_blueprint(animals_blueprint)
app.register_blueprint(vets_blueprint)
app.register_blueprint(appointments_blueprint)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    animals=animal_repository.select_all()
    vets=vet_repository.select_all()
    return render_template('about.html', animals=animals, vets=vets)

if __name__ == "__main__":
    app.run(debug=True)