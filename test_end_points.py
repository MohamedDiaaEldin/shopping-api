import re
from time import sleep
import unittest

from werkzeug.test import Client
from main import app , CartItem , Category , Customer , Product , db
import json
'''
    you should use the test data which is in data folder 
    - define a LOCAL_DATABASE_URL in .env 
    - run add_data.py to fill the database with data
'''


class ShoppingTest(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app
        self.client = self.app.test_client
        self.db = db
        self.Product = Product
        self.Customer = Customer
        self.Category = Category
        self.CartItem = CartItem
        
    def test_get_products(self):        
        res = self.client().get('/products')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status_code'], 200)
        self.assertTrue(len(data['products']) > 0)
        self.assertTrue(data['success'])
        
    def test_get_product_with_id(self):
        res = self.client().get('/products/1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status_code'], 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['product']['product_name'], 'gamming laptop')
        self.assertEqual(data['product']['price'], 12000.0)
    
    def test_failures_get_product_with_id(self):
        res = self.client().get('/products/10000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['status_code'], 404)
        self.assertEqual(data['message'], 'not found')
    
    
    def test_get_customer_with_id(self):
        res = self.client().get('/customers/1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status_code'], 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['customer']['first_name'], 'Mohamed')
        self.assertEqual(data['customer']['last_name'], 'Diaa')
        
    def test_failures_get_customer_by_id(self):
        res = self.client().get('/customers/1000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['status_code'], 404)
        self.assertEqual(data['message'], 'not found')
        
    def test_get_cart_items(self):
        res = self.client().get('/customers/1/items')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status_code'], 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['cart_items']) > 0)

    def test_failures_cart_items(self):
        res = self.client().get('/customers/1000/items')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['status_code'], 404)
        self.assertEqual(data['message'], 'not found')

    def test_get_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status_code'], 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['categories']) > 0)
        self.assertEqual(data['categories'][0]['category_id'] ,  1)
        self.assertEqual(data['categories'][0]['category_name'] ,  'laptop')
        
    '''
     post product test 
    '''
    def test_post_product(self):
        product = {
            "product_name":"short-for-test",
             "product_description":"white short", 
             "category_id":3, 
             "price":75
            }
        res = self.client().post('/product', data=json.dumps(product), content_type='application/json')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status_code'], 200)
        self.assertTrue(data['success'])
        # get new added product
        # delete it
        try:
            new_added = self.Product.query.filter_by(product_name='short-for-test').all()[0]
            self.assertEqual(new_added.product_name, 'short-for-test')
            new_added.delete()
        except :
            self.db.session.rollback()
            print('error while deleting or getting new added product for testing')
    
    def test_failures_post_product(self):
        product = {
            "product_name":"short-for-test",
            "product_description":"white short", 
            "category_number":3,  # wrong key
            "price":75
        }
        res = self.client().post('/product', data=json.dumps(product), content_type='application/json')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['message'], 'unprocessable entity')
        self.assertEqual(data['status_code'], 422)

    '''
     post category test
    '''
    def test_post_category(self):
        category = {
            "category_name":"category-for-test"             
        }
        res = self.client().post('/category', data=json.dumps(category), content_type='application/json')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status_code'], 200)
        self.assertTrue(data['success'])

        # get new added category 
        # delete it
        try:
            new_added = self.Category.query.filter_by(category_name='category-for-test').all()[0]            
            self.assertEqual(new_added.category_name, 'category-for-test')
            new_added.delete()
        except :
            self.db.session.rollback()
            print('error while deleting or getting new added category for testing')
    
    def test_failures_post_category(self):
        category = {
            "product":"category-for-test", ## wrong key
        }
        res = self.client().post('/category', data=json.dumps(category), content_type='application/json')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['message'], 'unprocessable entity')
        self.assertEqual(data['status_code'], 422)

    '''
     post customer test 
    '''
    def test_add_customer(self):
        first_name = 'hassan test'
        customer = {
            "first_name": first_name ,
            "last_name": "ali test" ,
            "address":"Giza" ,
            "phone" : "012222453"
        }
        res = self.client().post('/customer', data=json.dumps(customer), content_type='application/json')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status_code'], 200)
        self.assertTrue(data['success'])

        ## get new added customer 
        # delete it
        try:
            new_added = self.Customer.query.filter_by(first_name=first_name).all()[0]
            self.assertEqual(new_added.first_name, first_name)
            new_added.delete()
        except:            
            print('error while getting or deleting new added customer')            
    
    def test_failures_add_customer(self):
        customer = { ## customer object with  wrong keys
            "first": 'hassan test',
            "last": "ali test" ,
            "address":"Giza" ,
            "phone" : "012222453"
        }
        res = self.client().post('/customer', data=json.dumps(customer), content_type='application/json')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['message'], 'unprocessable entity')
        self.assertEqual(data['status_code'], 422)


    def test_patch_customer(self):        
        new_phone = "01111111111" 
        customer = {
            "first_name": 'Mohamed' ,
            "last_name": "Diaa" ,
            "address":"October city" ,
            "phone" : new_phone ## this will be chancged
        }

        res = self.client().patch('/customers/1', data=json.dumps(customer), content_type='application/json')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status_code'], 200)
        self.assertTrue(data['success'])
        ## get new updated customer 
        try:
            new_updated = self.Customer.query.get(1)
            self.assertEqual(new_updated.phone, new_phone)
        except:            
            print('error while getting new updated customer')            
    
    def test_failures_patch_customer(self):
        new_phone = "012212121" 
        customer = {
            "first_name": 'Mohamed' ,
            "last_name": "Diaa" ,
            "address":"October city" ,
            "phone_number" : new_phone  ## wrong key
        }
        res = self.client().patch('/customers/1', data=json.dumps(customer), content_type='application/json')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['message'], 'unprocessable entity')
        self.assertEqual(data['status_code'], 422)

    def test_patch_product(self):
        product = {
            "product_name":"T-shirt",
             "product_description":"red - cotton", 
             "category_id":3, 
             "price":100  ## change is here
            }
        res = self.client().patch('/products/3', data=json.dumps(product), content_type='application/json')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status_code'], 200)
        self.assertTrue(data['success'])
        try:
            new_updated = self.Product.query.get(3)
            self.assertEqual(new_updated.price, 100)
        except:
            print('error while geting new updated product')

    def test_failures_patch_product(self):
        product = {
            "product_name":"short-for-test",
            "product_description":"white short", 
            "category_number":3,  # wrong key
            "price":75
        }
        res = self.client().patch('/products/3', data=json.dumps(product), content_type='application/json')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['message'], 'unprocessable entity')
        self.assertEqual(data['status_code'], 422)


    # this test depends on post customer and post cart item 
    def test_delete_customer(self):
        # add customer
        customer = {
            "first_name": "ahmed test" ,
            "last_name": "ali test" ,
            "address":"Giza" ,
            "phone" : "012222453"
        }
        res = self.client().post('/customer', data=json.dumps(customer), content_type='application/json')
        self.assertEqual(res.status_code, 200)
        
        new_added_customer = self.Customer.query.filter_by(first_name='ahmed test').all()[0]
        new_customer_id = new_added_customer.id
        ## add cart item
        cart_item = {
            "product_id" : 7,
            "customer_id" : new_customer_id,
            "quantity" : 1  
        }        
        res = self.client().post('/item', data=json.dumps(cart_item), content_type='application/json')
        self.assertEqual(res.status_code, 200) 
        # test delete customer 
        res = self.client().delete(f'/customers/{new_customer_id}')
        data = json.loads(res.data)        
        self.assertEqual(res.status_code, 200)        
        self.assertEqual(data['status_code'], 200)
        self.assertEqual(data['success'], True)

    def test_failures_delete_customer(self):
        res = self.client().delete('/customers/1000') ## not found id
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['status_code'], 404)        
        self.assertEqual(data['message'], 'not found')        
        

    # this test uses post customer and post cart_item end points    
    def test_delete_cart_item(self):
        # add customer
        customer = {
            "first_name": "ahmed-test" ,
            "last_name": "ali test" ,
            "address":"Giza" ,
            "phone" : "012222453"
        }
        res = self.client().post('/customer', data=json.dumps(customer), content_type='application/json')
        self.assertEqual(res.status_code, 200)
        
        new_added_customer = self.Customer.query.filter_by(first_name='ahmed-test').all()[0]
        new_customer_id = new_added_customer.id
        ## add cart item
        cart_item = {
            "product_id" : 7,
            "customer_id" : new_customer_id,
            "quantity" : 1
        }        
        res = self.client().post('/item', data=json.dumps(cart_item), content_type='application/json')
        self.assertEqual(res.status_code, 200) 
        new_added_item_id = self.CartItem.query.filter_by(customer_id=new_customer_id).all()[0].id     

        ## test  delete cart item 
        res = self.client().delete(f'/items/{new_added_item_id}')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status_code'], 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(self.CartItem.query.get(new_added_item_id), None)
        self.assertEqual(self.Customer.query.get(new_customer_id).total_price, 0)
        ## delete new added customer 
        res = self.client().delete(f'/customers/{new_customer_id}')
        data = json.loads(res.data)      

    def test_failures_delete_cart_item(self):
        res = self.client().delete('/items/1000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['status_code'], 404)
        self.assertEqual(data['message'], 'not found')
    
    def test_delete_product(self):
        ## extract product data that will be deleted 
        product = self.Product.query.get(9)
        id = product.id
        product_name = product.product_name
        product_description = product.product_description
        category_id = product.category_id
        price = product.price

        res = self.client().delete('/products/9') 
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status_code'], 200)
        self.assertEqual(data['success'], True)
        ## add deleted product again
        try:
            product = self.Product(id=id, product_name=product_name, product_description=product_description, price=price, category_id=category_id)
            product.add_to_database()
        except:
            price('error while adding new deleted product')

    def test_failures_delete_prodcut(self):
        res = self.client().delete('/products/10000') 
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['status_code'], 404)
        self.assertEqual(data['message'], 'not found')

    def test_delete_category(self):
        # category will be deleted
        category = self.Category.query.get(5)
        id = category.id
        category_name = category.category_name
        
        res = self.client().delete('/categories/5')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status_code'], 200)
        self.assertEqual(data['success'], True)
        ## add new deleted category
        try:            
            category = Category(id=id, category_name=category_name)
            category.add_to_database()
        except:
            print('error while deleting new deleted category')
    def test_failures_delete_category(self):
        res = self.client().delete('/categories/1000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['status_code'], 404)
        self.assertEqual(data['message'], 'not found')
if __name__ == '__main__':
    unittest.main()