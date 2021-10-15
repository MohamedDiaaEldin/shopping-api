from flask import Flask , jsonify , abort , request
import models 
from flask_migrate import Migrate
from flask_cors import CORS
from models import Product , Category,  CartItem , Customer

app= Flask(__name__)
CORS(app)
db = models.setup_db(app)
migrate  = Migrate(app=app, db=db)

@app.route('/')
def index():
  return 'From Index'