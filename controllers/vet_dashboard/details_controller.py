from flask import Flask, render_template, request, Blueprint
from models.vet import Vet
from repositories.vet_rep import VetRep


vets_details_blueprint = Blueprint('vets_details', __name__)

# EDIT DETAILS DASHBOARD
@vets_details_blueprint.route('/vets/<id>/edit')
def edit_vet(id):
    vet = VetRep().select(id)
    return render_template('/vets/dashboard/details.html', title = 'Edit Vet', selected_page = "update_vet", vet = vet, selected_dash_item = 'details')

@vets_details_blueprint.route('/vets/<id>/edit', methods = ['POST'])
def edit_vet_POST(id):
    fist_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    VetRep().update(fist_name, last_name, id)
    vet = VetRep().select(id)
    return render_template('/vets/dashboard/details.html', title = 'Edit Vet', selected_page = "update_vet", vet = vet, selected_dash_item = 'details')
