import base64
from flask import Flask, render_template, request, redirect, Blueprint
from models.owner import Owner
from models.pet import Pet
from repositories.owner_rep import OwnerRep
from repositories.pet_rep import PetRep
from repositories.vet_rep import VetRep

from utils.string_to_date import string_to_date
from utils.write_to_file import write_to_file

owners_pets_blueprint = Blueprint('owners_pets', __name__)


# PETS DASHBOARD
@owners_pets_blueprint.route('/owners/<id>/pets')
def edit_pets(id):
    owner = OwnerRep().select(id)
    pets = OwnerRep().get_pets(id)
    vets = VetRep().select_all()
    return render_template('/owners/dashboard/see-pets.html', pets = pets, title = 'Owner', vets=vets, selected_page = 'update_owner', owner = owner, selected_dash_item = 'pets')

# editing pre existing pet
@owners_pets_blueprint.route('/owners/<owner_id>/pets/<pet_id>', methods = ['POST'])
def edit_pets_POST(owner_id, pet_id):
    
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

    return redirect('/owners/'+owner_id+'/pets')

# creating pet form
@owners_pets_blueprint.route('/owners/<id>/add-pet')
def create_pet_GET(id):
    owner = OwnerRep().select(id)
    vets = VetRep().select_all()
    return render_template('/owners/dashboard/add-pet.html', vets = vets, title = 'Owner', selected_page = 'update_owner', owner = owner, selected_dash_item = 'pets')

# creating pet -- with pets
@owners_pets_blueprint.route('/owners/<owner_id>/add-pet', methods = ['POST'])
def create_pet_POST(owner_id):
    
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
        yo = False
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

    pet = Pet(name, dob, yo, type_s, owner, vet, new_image_string, new_image_type)
    PetRep().save(pet)

    # owner = OwnerRep().select(owner_id)
    # pets = OwnerRep().get_pets(owner_id)
    return redirect('/owners/'+owner_id+'/pets')
