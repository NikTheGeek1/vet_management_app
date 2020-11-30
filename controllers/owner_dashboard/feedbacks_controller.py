from flask import Flask, render_template, request, redirect, Blueprint
from models.owner import Owner
from models.feedback import Feedback
from repositories.owner_rep import OwnerRep
from repositories.feedback_rep import FeedbackRep

owners_feedbacks_blueprint = Blueprint('owners_feedbacks', __name__)


# FEEDBACK ROUTES
@owners_feedbacks_blueprint.route('/owners/<id>/feedbacks')
def feedbacks_GET(id):
    owner = OwnerRep().select(id)
    feedbacks = OwnerRep().get_feedbacks(id)
    print(feedbacks)
    return render_template('/owners/dashboard/feedbacks.html', feedbacks = feedbacks, title = 'Owner', selected_page = 'update_owner', owner = owner, selected_dash_item = 'feedbacks')

@owners_feedbacks_blueprint.route('/owners/<id>/add-feedback', methods=['POST'])
def feedback_POST(id):
    qos = int(request.form.get('qos'))
    fs = int(request.form.get('fs'))
    cf = int(request.form.get('cf'))
    recommend = request.form.get('recommend')
    suggestions = request.form.get('suggestions')
    other_comment = request.form.get('other_comment')
    owner = OwnerRep().select(id)
    feedback = Feedback(qos, fs, cf, recommend, suggestions, other_comment, owner)
    FeedbackRep().save(feedback)
    return redirect('/owners/'+id+'/feedbacks')
