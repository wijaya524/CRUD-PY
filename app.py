from flask import Flask, render_template, request, redirect, url_for 
from models import db, Item 

# Initialize the Flask application
app = Flask(__name__) 

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/tugas4' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app) 

# Create the database
with app.app_context():    
   
 try:
  db.create_all()
 except Exception as e:
  print(f"Error creating database: {e}")

# Define the routes for rendering templates index.html
@app.route('/') 
def index():  
     items = Item.query.all() 
     return render_template('index.html', items=items) 

# Define the routes for handling form submissions in create.html
@app.route('/create', methods=['GET', 'POST'])
def create():   
      if request.method == 'POST':  
               new_item = Item(name=request.form['name'], description=request.form['description']) 
               db.session.add(new_item) 
               db.session.commit()   
               return redirect(url_for('index'))     
      return render_template('create.html') 

# Define the routes for handling form submissions in edit.html
@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit(item_id):    
      item = Item.query.get(item_id)     
      if request.method == 'POST': 
                item.name = request.form['name']    
                item.description = request.form['description']
                db.session.commit()   
                return redirect(url_for('index'))     
      return render_template('edit.html', item=item) 

# Define the routes for handling form submissions in delete.html
@app.route('/delete/<int:item_id>') 
def delete(item_id):   
      item = Item.query.get(item_id)  
      db.session.delete(item)
      db.session.commit()   
      return redirect(url_for('index'))

# Run the Flask application
if __name__ == '__main__': 
       app.run(debug=True) 