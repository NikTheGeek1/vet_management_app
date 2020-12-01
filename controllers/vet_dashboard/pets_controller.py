from flask import Flask, render_template, request, redirect, Blueprint
from models.vet import Vet
from models.pet import Pet
from repositories.vet_rep import VetRep
from repositories.pet_rep import PetRep

from utils.diff_between_lists import list_diff

vets_pets_blueprint = Blueprint('vets_pets', __name__)

# PETS DASHBOARD
@vets_pets_blueprint.route('/vets/<id>/pets')
def edit_pets(id):
    pets = VetRep().get_pets(id)
    all_pets_suboptimal = PetRep().select_all()
    # getting only the pets that this vet doesn't have
    vet_pet_ids = [pet.id for pet in pets]
    all_pet_ids = [pet.id for pet in all_pets_suboptimal]
    
    unique_pet_ids = list_diff(vet_pet_ids, all_pet_ids)
    all_pets = []
    for unique_id in unique_pet_ids:
        all_pets.append(PetRep().select(unique_id))

    vet = VetRep().select(id)
    return render_template('/vets/dashboard/see-pets.html',all_pets = all_pets, pets = pets, title = 'Vet', vet=vet, selected_page = 'update_vet', selected_dash_item = 'pets')


@vets_pets_blueprint.route('/vets/<id>/select-pet', methods = ['POST'])
def select_pet(id):
    pet_id = request.form.get('pet')
    pet = PetRep().select(pet_id)
    pet.vet.id = id
    PetRep().update(pet)
    return redirect('/vets/'+id+'/pets')