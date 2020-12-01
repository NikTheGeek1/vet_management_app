from flask import Flask, render_template, request, redirect, Blueprint
from models.pet import Pet
from repositories.pet_rep import PetRep

pets_blueprint = Blueprint('pets', __name__)

@pets_blueprint.route('/pets')
def pets():
    return render_template('/pets/index.html', selected_page = 'info', title = 'Pets')

@pets_blueprint.route('/pets/checked-in')
def see_checked_in_pets():
    pets = PetRep().select_currently_in_pets()
    return render_template('/pets/see-checked-in.html', title = 'pets', selected_page = "checked_in_pets", pets = pets)


@pets_blueprint.route('/pets/all')
def see_all_pets():
    pets = PetRep().select_all()
    return render_template('/pets/see-all.html', title = 'pets', selected_page = "see_pets", pets = pets)

@pets_blueprint.route('/pets/<id>/delete')
def delete_pet(id):
    PetRep().delete(id)
    return redirect('/pets/all')
