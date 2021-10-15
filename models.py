from flask_sqlalchemy import SQLAlchemy 
from os.path import join, dirname
from dotenv import load_dotenv

import os
import psycopg2

# # heroku database
# DATABASE_URL = os.environ['DATABASE_URL']
# if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
#     DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
# conn = psycopg2.connect(DATABASE_URL, sslmode='require')


# local
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
LOCAL_DATABASE_URL = os.environ.get("LOCAL_DATABASE_URL")
DATABASE_URL = LOCAL_DATABASE_URL

print('database url ---------> ', DATABASE_URL)



db = SQLAlchemy()

def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()
    return db

'''
Customers
	id (pr), first_name , last_name , address , phone_number , total_cart


Cart items :
	id (pr), quantity,  product_id (fk), customer_id (fk)


Categories:
	id (pr), category_name

Products :
	id (pr), product_name  , category (fk)


'''
Column = db.Column
String = db.String
Integer = db.Integer
Float = db.Float


class Category(db.Model):
    id = Column(Integer, primary_key=True)
    category_name = Column(String, nullable=False)
    products = db.relationship('Product', backref='category')

    def get_catgory_object(self):
        return {
            'category_id' : self.id,
            'category_name' : self.name
        }
    
    def add_to_database(self):
        db.session.add(self)
        db.session.commit()

class Product(db.Model):
    id = Column(Integer, primary_key=True)
    product_name = Column(String, nullable=False)    
    product_description = Column(String)    
    products = db.relationship('CartItem', backref='product')
    category_id = Column(Integer, db.ForeignKey('category.id'), nullable=False)
    price = Column(Float, nullable=False)

    def get_product_object(self):
        return {
            'id' : self.id,
            'product_name' : self.product_name,
            'product_description' : self.product_description,
            'category_id' : self.category_id,
            'price' : self.price,
            'category' : Category.query.get(self.category_id).category_name
        }

    def add_to_database(self):
        db.session.add(self)
        db.session.commit()


class Customer(db.Model):
    id = Column(db.Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    total_price = Column(Float) 
       
    customers = db.relationship('CartItem', backref='customer')
    
    def get_customer_object(self):
        return {
            'id' : self.id,
            'first_name' : self.first_name,
            'last_name' : self.last_name,
            'address' : self.address,
            'phone' : self.phone,
            'total_price' : self.total_price            
        }

    def add_to_database(self):
        db.session.add(self)
        db.session.commit()

        

class CartItem(db.Model):
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    ## foreign keys
    product_id = Column(Integer, db.ForeignKey('product.id'), nullable=False)
    customer_id = Column(Integer, db.ForeignKey('customer.id'), nullable=False)

    def get_item_object(self):
        return{            
            'id' : self.id ,
            'quantity' :  self.quantity,
            'product_id' : self.product_id , 
            'customer_id' : self.customer_id
        }
    
    def add_to_database(self):
        db.session.add(self)
        db.session.commit()