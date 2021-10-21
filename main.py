from flask import Flask , jsonify , abort  , request , redirect
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

@app.route("/login")
def starting_url():
    return redirect("https://ud-cap.us.auth0.com/authorize?audience=shoping&response_type=token&client_id=Bzzt293Q1XzEneTf6lt4DONzvVrrUoUX&redirect_uri=https://shopping-cap.herokuapp.com/login-results")

@app.route('/login-results', methods=['POST'])
def login_results():
  json_body = request.get_json()
  if json_body != None:
    print(json_body)
  return jsonify({
    'status_code' : 200 ,
    'message' : 'loged in - test'
  })

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

def is_valid_cart_item(json_body):
  return json_body != None and 'quantity'  in json_body and 'product_id' in json_body and 'customer_id'  in json_body

# this method update the new total peice for a customer
def add_cart_item_dependencies(customer, product, quantity):    
    customer.total_price += quantity * product.price
    customer.update()

def is_valid_item_dependencies(customer, product):
  return customer != None and product != None
@app.route('/item' , methods=['POST'])
def add_cart_item():
  try:
    json_body = request.get_json()
    if not is_valid_cart_item(json_body):
      return handel_unprocessable_entity()    
    
    quantity = json_body.get('quantity')
    customer_id = json_body.get('customer_id')
    product_id = json_body.get('product_id')

    product = Product.query.get(product_id) 
    customer = Customer.query.get(customer_id) 

    if not is_valid_item_dependencies(customer, product):
      return handle_not_found_error()

    new_item = CartItem(quantity=quantity, product_id=product_id, customer_id=customer_id)
    new_item.add_to_database()
    # add dependencies
    add_cart_item_dependencies(customer, product, quantity)
    return success()
  except:
    db.session.rollback()
    print('error while adding new cart item for customer number', customer_id)
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
  return json_data != None and 'product_name' in json_data and 'product_description'  in json_data and 'category_id' in json_data and 'price'  in json_data
  


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
  return json_data != None and 'category_name'  in json_data
  


def is_valid_customer(json_body):
  return  json_body != None and 'first_name'  in json_body and 'last_name' in json_body and 'address' in json_body and 'phone'  in json_body  
    
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


def update_customer_data(json_body , customer): 
    customer.first_name = json_body.get('first_name')
    customer.last_name = json_body.get('last_name')
    customer.address = json_body.get('address')
    customer.phone = json_body.get('phone')
    customer.update()



## curl http://127.0.0.1:5000/customers/1 -X PATCH -H "Content-Type: application/json"  -d '{"first_name":"Mohamed", "last_name":"Diaa Eldin", "address":"October city", "phone":"012274666163"}'
@app.route('/customers/<int:customer_id>', methods=['PATCH'])  # for dev role
def update_customer(customer_id):
  try:
    customer = Customer.query.get(customer_id)
    if customer == None :
      return handle_not_found_error()
    
    json_body = request.get_json()
    if not is_valid_customer(json_body) :
      return handel_unprocessable_entity()

    update_customer_data(json_body, customer)
    return success()
  except:
    db.session.rollback()
    print('error while updating customer with id: ', customer_id)
    return handle_internal_server_error()



## curl http://127.0.0.1:5000/products/13 -X PATCH -H "Content-Type: application/json"  -d '{"product_name":"tomi shirt", "product_description":"black - blue tomi teshirt", "category_id":3, "price":1000}'
@app.route('/products/<int:product_id>',methods=['PATCH']) # adminandproduct_adminroles
def update_product(product_id):
  try:
    product = Product.query.get(product_id)
    if product == None :
      return handle_not_found_error()

    json_body = request.get_json()
    if not is_valid_product(json_body):
      return handel_unprocessable_entity()

    update_product_data(json_body, product)
    return success()
  except:
    db.session.rollback()
    print('error while updating product with id', product_id )
    return handle_internal_server_error()

def update_product_data(json_body, product):  
  product.product_name = json_body.get('product_name') 
  product.product_decription = json_body.get('product_decription') 
  product.category_id = json_body.get('category_id')
  product.price = json_body.get('price')
  product.update()

@app.route('/categories/<int:category_id>', methods=['PATCH'])
def update_category(category_id) :## admin role
  try:
    json_body = request.get_json()
    if not is_valid_catrgory(json_body):
      return handel_unprocessable_entity()    
    update_category_data(json_body, category_id)
    return success()
  except:
    db.session.rollback()
    print('error while updating category with id', category_id)
    return handle_internal_server_error()

def update_category_data(json_body, category_id):
  category = Category.query.get(category_id)
  print(category)
  category.category_name = json_body.get('category_name')
  category.update()

# DELETE
@app.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
  try:
    customer = Customer.query.get(customer_id)    
    if customer == None :
      return handle_not_found_error()        

    ## delete dependencies
    delete_customer_dependencies(customer_id)
    # delete customer
    customer.delete()
    return success()
  except:
    db.session.rollback()
    print('error while deleting customer with id', customer_id)
    return handle_internal_server_error()

def delete_customer_dependencies(customer_id):
  items = CartItem.query.filter_by(customer_id=customer_id).all()
  if len(items) == 0 :
    return
  for item in items:
    item.delete()

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
  try:    
    item = CartItem.query.get(item_id)
    if item == None :
      return handle_not_found_error()

    customer = Customer.query.get(item.customer_id)
    product = Product.query.get(item.product_id)
    customer.total_price -= product.price * item.quantity
    customer.update()
    item.delete()
    return success()
  except:
    db.session.rollback()
    print('error while deleting cart items')
    return handle_internal_server_error()
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
  try:    
    product = Product.query.get(product_id)
    if product == None :
      return handle_not_found_error()
      ## if the product is connected with cart_item table 
      ## i may need another table or do some changes
    elif len(CartItem.query.filter_by(product_id=product_id).all()) > 0:
      return handel_not_implemented_error()
    product.delete()
    return success()
  except:
    db.session.rollback()
    print('error while deleting product')
    return handle_internal_server_error()

@app.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
  try:
    category = Category.query.get(category_id)
    if category == None:
      return handle_not_found_error()
    ## i may need to set defualt category in in category table to be replaced 
    ## while deleting category connected with products
    elif len(Product.query.filter_by(category_id=category_id).all()) > 0:
      return handel_not_implemented_error()
    category.delete()
    return success() 
  except:
    db.session.rollback()
    print('error while deleting category')
    return handle_internal_server_error()

    '''
    https://ud-cap.us.auth0.com/authorize?audience=shoping&response_type=token&client_id=Bzzt293Q1XzEneTf6lt4DONzvVrrUoUX&redirect_uri=https://shopping-cap.herokuapp.com/login-results
    '''
