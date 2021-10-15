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



@app.route('/products')
def get_products():
  try:
    return jsonify({
      'status_code' : 200 ,
      'success' : True,
      'products' : [p.get_product_object() for p in Product.query.all()]
    })
  except :
    print('error while getting all products')
    return abort(500)