from flask import Flask, render_template
from controllers.owner_controller import owners_blueprint
from controllers.owner_dashboard.pets_controller import owners_pets_blueprint
from controllers.owner_dashboard.feedbacks_controller import owners_feedbacks_blueprint
from controllers.owner_dashboard.testimonial_controller import owners_testimonial_blueprint

from controllers.vet_controller import vets_blueprint
from controllers.vet_dashboard.details_controller import vets_details_blueprint
from controllers.vet_dashboard.pets_controller import vets_pets_blueprint

app = Flask(__name__)

app.register_blueprint(owners_blueprint)
app.register_blueprint(owners_pets_blueprint)
app.register_blueprint(owners_feedbacks_blueprint)
app.register_blueprint(owners_testimonial_blueprint)

app.register_blueprint(vets_blueprint)
app.register_blueprint(vets_details_blueprint)
app.register_blueprint(vets_pets_blueprint)

@app.route('/')
def index():
    return render_template('index.html', title = 'Welcome')

if __name__ == '__main__':
    app.run(debug=True)