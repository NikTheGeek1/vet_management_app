from flask import Flask, render_template, request, redirect, Blueprint
from models.owner import Owner
from models.pet import Pet
from repositories.owner_rep import OwnerRep
from repositories.pet_rep import PetRep


owners_blueprint = Blueprint('owners', __name__)

@owners_blueprint.route('/owners')
def owners():
    return render_template('/owners/index.html', selected_page = 'info', title = 'Owners')

@owners_blueprint.route('/owners/add')
def add_owner():
    return render_template('/owners/add-owner.html', title = 'Add', selected_page = 'add_owner')

@owners_blueprint.route('/owners/add', methods=['POST'])
def add_owner_POST():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    register = request.form.get('register')
    owner = Owner(first_name, last_name, email, phone, register)
    OwnerRep().save(owner)
    return redirect('/owners/all')

@owners_blueprint.route('/owners/all')
def see_all_owners():
    owners = OwnerRep().select_all(True)
    return render_template('/owners/see-all.html', title = 'Owners', selected_page = "see_owners", owners = owners)

@owners_blueprint.route('/owners/<id>/delete')
def delete_owner(id):
    OwnerRep().delete(id)
    return redirect('/owners/all')

# EDIT DETAILS DASHBOARD
@owners_blueprint.route('/owners/<id>/edit')
def edit_owner(id):
    owner = OwnerRep().select(id)
    return render_template('/owners/dashboard/edit.html', title = 'Edit Owner', selected_page = "update_owner", owner = owner, selected_dash_item = 'details')

@owners_blueprint.route('/owners/<id>/edit', methods = ['POST'])
def edit_owner_POST(id):
    email = request.form.get('email')
    phone = request.form.get('phone')
    registered = request.form.get('register')
    OwnerRep().update(email, phone, registered, id)
    owner = OwnerRep().select(id)
    return render_template('/owners/dashboard/edit.html', title = 'Edit Owner', selected_page = "update_owner", owner = owner, selected_dash_item = 'details')


