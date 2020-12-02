from flask import Flask, render_template, request, redirect, Blueprint
from models.pet_treatment import PetTreatment
from repositories.pet_rep import PetRep
from repositories.treatment_rep import TreatmentRep
from repositories.treatment_pet import PetTreatmentsRep

pets_treatments_blueprint = Blueprint('pets_treatments', __name__)

# EDIT DETAILS DASHBOARD
@pets_treatments_blueprint.route('/pets/<id>/treatments')
def treatments(id):
    pet = PetRep().select(id)
    all_treatments = TreatmentRep().select_all()
    treatments = PetRep().get_treatments(id)
    return render_template('/pets/dashboard/treatments.html', pet = pet, treatments = treatments, all_treatments = all_treatments, title = 'Pet\'s treatments', selected_page = "update_pet", selected_dash_item = 'treatments')


@pets_treatments_blueprint.route('/pets/<id>/treatments/add', methods = ['POST'])
def add_treatment(id):
    treatment_id = request.form.get('treatment')
    treatment = TreatmentRep().select(treatment_id)
    pet = PetRep().select(id)
    petTreatment = PetTreatment(pet, treatment)
    PetTreatmentsRep().save(petTreatment)
    return redirect('/pets/'+id+'/treatments')