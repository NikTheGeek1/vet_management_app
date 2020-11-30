from flask import Flask, render_template, request, redirect, Blueprint
from repositories.feedback_rep import FeedbackRep
from models.feedback import Feedback

feedbacks_blueprint = Blueprint('feedbacks', __name__)

@feedbacks_blueprint.route('/feedbacks')
def feedbacks():
    feedbacks = FeedbackRep().select_all()
    return render_template('/feedbacks.html', feedbacks = feedbacks, title = 'Feedbacks')