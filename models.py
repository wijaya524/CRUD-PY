from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()

# Create the database model
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Item {self.name}>'
