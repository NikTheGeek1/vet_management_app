from flask import Flask, render_template, Blueprint
from models.visit import Visit
import repositories.visit_rep as visit_rep

visits_bp = Blueprint('visits', __name__)

@visits_bp.route('/<pet_id>/visits')
def visits(pet_id):
    pass
