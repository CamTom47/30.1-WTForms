from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'SecretSecrets'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_TRACK_ECHO'] = True

app.debug = True
toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def home_page():
    """ Shows landing page for site"""

    pets = Pet.query.all()
    return render_template('homepage.html', pets = pets)


@app.route('/add', methods = ['GET', 'POST'])
def create_pet_form():

    """Show initial pet form and handle upon sending post request. Redirect homepage upon success or render same form in validation fails"""

    form = PetForm()
    
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)
        db.session.add(pet)
        db.session.commit()

        return redirect('/')

    else:
        return render_template('create_pet_form.html', form = form)
        



@app.route('/<int:id>')
def pet_page(id):
    """Show pet information"""
    pet = Pet.query.get(id)

    return render_template('/pet_details.html', pet = pet)
    
@app.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit_pet_form(id):
    """Render pet form and handle submission. If successful redirect to pet details. If failure, re-render pet edit form """

    pet = Pet.query.get(id)
    form = PetForm(obj = pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()

        return redirect(f'/{pet.id}')
    
    else:
        return render_template('/edit_pet_form.html', form = form, pet = pet)