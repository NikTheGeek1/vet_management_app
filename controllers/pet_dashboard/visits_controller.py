from flask import Flask, render_template, request, redirect, Blueprint
from models.visit import Visit
from repositories.pet_rep import PetRep
from repositories.visit_rep import VisitRep

pets_visits_blueprint = Blueprint('pets_visits', __name__)

# EDIT DETAILS DASHBOARD
@pets_visits_blueprint.route('/pets/<id>/visits')
def see_visits(id):
    visits = PetRep().get_visits(id)
    pet = PetRep().select(id)
    return render_template('/pets/dashboard/see-visits.html', pet = pet, visits = visits, title = 'Pet\'s visits', selected_page = "update_pet", selected_dash_item = 'visits')

@pets_visits_blueprint.route('/pets/<id>/check-in', methods = ['POST'])
def check_in(id):
    check_in = request.form.get('check_in')
    check_out = request.form.get('check_out')
    description = request.form.get('description')
    visit = Visit(id, check_in, check_out, description)
    VisitRep().save(visit)
    return redirect('/pets/'+id+'/visits')