from flask import Flask, render_template, request, redirect, Blueprint
from models.vet import Vet
from models.pet import Pet
from repositories.vet_rep import VetRep
from repositories.pet_rep import PetRep


vets_blueprint = Blueprint('vets', __name__)

@vets_blueprint.route('/vets')
def vets():
    return render_template('/vets/index.html', selected_page = 'info', title = 'Vets')


@vets_blueprint.route('/vets/add')
def add_vet():
    return render_template('/vets/add-vet.html', title = 'Add', selected_page = 'add_vet')

@vets_blueprint.route('/vets/add', methods=['POST'])
def add_owner_POST():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    vet = Vet(first_name, last_name)
    VetRep().save(vet)
    return redirect('/vets/all')

@vets_blueprint.route('/vets/all')
def see_all_vets():
    vets = VetRep().select_all(True)
    return render_template('/vets/see-all.html', title = 'Vets', selected_page = "see_vets", vets = vets)


@vets_blueprint.route('/vets/<id>/delete')
def delete_vet(id):
    VetRep().delete(id)
    return redirect('/vets/all')
