from flask import Flask, render_template, Blueprint
from repositories.treatment_rep import TreatmentRep
from repositories.treatment_pet import PetTreatmentsRep
from repositories.pet_rep import PetRep
from models.pet_treatment import PetTreatment

treatments_blueprint = Blueprint('treatments', __name__)

@treatments_blueprint.route('/treatments')
def treatments():
    treatments = TreatmentRep().select_all()
    treatmentPets = PetTreatmentsRep().select_all()
    # creating a dictionary of all treatments as keys 
    # and pets as values. Each treatment could have 
    # none or more pets
    treat_dic = {}
    for treatment in treatments:
        treat_dic[treatment.title] = []
        for treatmentPet in treatmentPets:
            if treatmentPet.treatment.id == treatment.id:
                treat_dic[treatment.title].append(treatmentPet.pet)
    return render_template('/treatments/treatments.html', treat_dic = treat_dic, treatments = treatments, title = 'Treatments')