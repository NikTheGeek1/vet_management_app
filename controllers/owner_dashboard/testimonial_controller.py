from flask import Flask, render_template, request, redirect, Blueprint
from models.testimonial import Testimonial
from repositories.owner_rep import OwnerRep
from repositories.testimonial_rep import TestimonialRep

owners_testimonial_blueprint = Blueprint('owners_testimonial', __name__)


# testimonial ROUTES
@owners_testimonial_blueprint.route('/owners/<id>/testimonial')
def testimonial_GET(id):
    owner = OwnerRep().select(id)
    testimonial = OwnerRep().get_testimonial(id)
    print(testimonial)
    return render_template('/owners/dashboard/testimonial.html', testimonial = testimonial, title = 'Owner', selected_page = 'update_owner', owner = owner, selected_dash_item = 'testimonial')

@owners_testimonial_blueprint.route('/owners/<id>/add-testimonial', methods=['POST'])
def testimonial_POST(id):
    owner = OwnerRep().select(id)
    testimonial = request.form.get('testimonial')
    testimonial = Testimonial(testimonial, owner)
    TestimonialRep().save(testimonial)
    return redirect('/owners/'+id+'/testimonial')


@owners_testimonial_blueprint.route('/owners/<owner_id>/remove-testimonial/<testimonial_id>', methods = ['POST'])
def remove_testimonial(owner_id, testimonial_id):
    TestimonialRep().delete(testimonial_id)
    return redirect('/owners/'+owner_id+'/testimonial')