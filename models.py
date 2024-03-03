from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database"""
    db.app = app
    app.app_context().push()
    db.init_app(app)



"""Models for adopt database"""


class Pet(db.Model):
    
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key= True, nullable = False, autoincrement = True)
    
    name = db.Column(db.Text,
                     nullable = False)
    species = db.Column(db.Text,
                        nullable = False)
    photo_url = db.Column(db.Text,
                          nullable = True, default='https://www.dogster.com/wp-content/uploads/2013/09/australian-shepherd-dog-sitting-on-a-rock-in-the-park_ChocoPie_Shutterstock.jpg.webp')
    age = db.Column(db.Integer,
                    nullable = True)
    notes = db.Column(db.Text,
                      nullable = True)
    available = db.Column(db.Boolean,
                          nullable = False,
                          default = True)