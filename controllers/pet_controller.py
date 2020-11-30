from flask import Flask, render_template, request, redirect, Blueprint
from models.pet import Pet
from repositories.pet_rep import PetRep


pets_blueprint = Blueprint('pets', __name__)

@pets_blueprint.route('/pets')
def pets():
    return render_template('/pets/index.html', selected_page = 'info', title = 'Pets')