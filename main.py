from flask import Flask , jsonify , abort  , request
from flask_migrate import Migrate
from flask_cors import CORS
from models import Product , Category,  CartItem , Customer , setup_db


app= Flask(__name__)
from error_handler import *
CORS(app)
db = setup_db(app)
migrate  = Migrate(app=app, db=db)

@app.route('/')
def index():
  return 'From Index'


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'error' : 404 ,
        'message' :'Not Found'
    }), 404

@app.route('/products')
def get_products():
  try:
    products = Product.query.all()
    if len(products) == 0:            
      return handle_not_found_error()

    return jsonify({
      'status_code' : 200 ,
      'success' : True,
      'products' : [p.get_product_object() for p in products]
    })
  except :
    print('error while getting all products')
    return abort(500)


@app.route('/products/<int:product_id>')
def get_product_by_id(product_id):
  try:
    product = Product.query.get(product_id)
    if product == None :
      return handle_not_found_error()
    
    return jsonify({
      'status_code' : 200 ,
      'success' : True ,
      'product' : product.get_product_object()
    })
  except:
    print('error with getting product by id')
    return handle_internal_server_error()

@app.route('/customers/<int:customer_id>')
def get_customer_by_id(customer_id):
  try:
    customer = Customer.query.get(customer_id)
    if customer == None :
      return handle_not_found_error()
    
    return jsonify({
      'status_code' : 200 ,
      'success' : True ,
      'customer' : customer.get_customer_object()
    }) 
  except:
    print('error while getting customer by id')
    return handle_internal_server_error()

@app.route('/customers/<int:customer_id>/items')
def get_cart_items(customer_id):
  try:
    cart_items = CartItem.query.filter_by(customer_id=customer_id).all()    
    if cart_items == None or len(cart_items) == 0:
      return handle_not_found_error()

    return jsonify({
      'status_code' : 200 ,
      'success' : True, 
      'cart_items' : [Product.query.get(cart_item.product_id).get_product_object() for cart_item in cart_items]

    })
  except:
    print('error while getting cart items')
    return handle_internal_server_error()

@app.route('/categories')
def get_categories():
  try:
    categories = Category.query.all()
    if categories == None or len(categories) == 0:
      return handle_not_found_error()
    
    return jsonify({
      'status_code' : 200 ,
      'success' :True ,
      'categories' : [category.get_category_object() for category in categories]
    })
  except:
    print('error while geting categories')
    return handle_internal_server_error()


'''
 curl http://127.0.0.1:5000/product -X POST -H "Content-Type: application/json"  -d '{"product_name":"tomi shirt", "product_description":"black - blue tomi teshirt", "category_id":3, "price":100}'

'''
@app.route('/product', methods=['POST'])  ## admin and product_admin roles
def add_product():
  try:
    json_body  = request.get_json()    
    if not is_valid_product(json_body):       
      return handel_unprocessable_entity()
    
    product = Product(product_name=json_body.get('product_name') , product_description = json_body.get('product_description'), category_id=json_body.get('category_id'), price=json_body.get('price'))
    product.add_to_database()   
    return success() 
  except:
    db.session.rollback()
    print('error while adding new product')
    return handle_internal_server_error()

def is_valid_product(json_data):
  if json_data == None or 'product_name' not in json_data or 'product_description' not in json_data or 'category_id' not in json_data or 'price' not in json_data :
    return False
  return True


@app.route('/category', methods=['POST'])  # for admin role
def add_category():
  try:
    json_data = request.get_json()
    if not is_valid_catrgory(json_data):
      return handel_unprocessable_entity()    
    
    new_category = Category(category_name=json_data.get('category_name'))
    new_category.add_to_database()
    return success()
  except:
    db.session.rollback()
    print('error while adding new category')
    return handle_internal_server_error()

def is_valid_catrgory(json_data):
  if json_data == None or 'category_name' not in json_data:
    return False
  return True


def is_valid_customer(json_body):
  if json_body == None or 'first_name' not in json_body or 'last_name' not in json_body or 'address' not in json_body or 'phone' not in json_body :
    return False
  return True
    
def success():
    return jsonify({
      'status_code' : 200 ,
      'success' : True
    })

@app.route('/customer', methods=['POST'])  # for dev role
def add_customer():
  try:
    json_body = request.get_json()
    
    if not is_valid_customer(json_body):
      return handel_unprocessable_entity()
    new_customer = Customer(first_name=json_body.get('first_name'), last_name=json_body.get('last_name'), address=json_body.get('address'), phone=json_body.get('phone'), total_price=0.0)
    new_customer.add_to_database()
    return success()
  except:
    db.session.rollback()
    print('error while adding new customer')
    return handle_internal_server_error()