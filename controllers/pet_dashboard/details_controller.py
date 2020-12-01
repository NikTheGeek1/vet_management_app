import base64
from flask import Flask, render_template, request, redirect, Blueprint
from models.vet import Vet
from models.pet import Pet
from models.owner import Owner
from repositories.vet_rep import VetRep
from repositories.pet_rep import PetRep
from repositories.owner_rep import OwnerRep
from utils.string_to_date import string_to_date

pets_details_blueprint = Blueprint('pets_details', __name__)

# EDIT DETAILS DASHBOARD
@pets_details_blueprint.route('/pets/<id>/edit')
def edit_pet(id):
    pet = PetRep().select(id)
    vets = VetRep().select_all()
    return render_template('/pets/dashboard/details.html', vets = vets, title = 'Edit pet', selected_page = "update_pet", pet = pet, selected_dash_item = 'details')

@pets_details_blueprint.route('/pets/<pet_id>/owner<owner_id>/edit', methods = ['POST'])
def edit_pets_POST(pet_id, owner_id):
    # getting form data
    name = request.form.get('name')
    dob_string = request.form.get('dob')
    yo_string = request.form.get('yo')
    type_s = request.form.get('type')
    vet_id = request.form.get('vet')
    image = request.files['image']

    vet = VetRep().select(vet_id)
    owner = OwnerRep().select(owner_id)
    # date time logic
    if dob_string != '':
        dob = string_to_date(dob_string)
    else: 
        dob = False
    try:
        yo = float(yo_string.replace(',', '.'))
    except ValueError:
        yo = False
        

    # image logic
    new_image_string = False
    new_image_type = image.content_type
    if image.filename != '': # image was given
        new_image_string = base64.b64encode(image.read()).decode('utf-8')
        # write_to_file(new_image_string, new_image_type) 

    # if pet already has an image and an image was not given
    pet = PetRep().select(pet_id)
    if pet.image64 != '' and image.filename == '':
        new_image_string = pet.image64
        new_image_type = pet.image_type

    # if a new date was given in the form of yo and this is not a dash
    if yo and float(pet.yo) != float(yo):
        dob = False
    pet = Pet(name, dob, yo, type_s, owner, vet, new_image_string, new_image_type, pet_id)
    PetRep().update(pet)

    # owner = OwnerRep().select(owner_id)
    # pets = OwnerRep().get_pets(owner_id)
    return redirect('/pets/'+pet_id+'/edit')
