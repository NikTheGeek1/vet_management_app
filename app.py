from flask import Flask, render_template
from controllers.owner_controller import owners_blueprint

app = Flask(__name__)
app.register_blueprint(owners_blueprint)

@app.route('/')
def index():
    return render_template('index.html', title = 'Welcome')

if __name__ == '__main__':
    app.run(debug=True)