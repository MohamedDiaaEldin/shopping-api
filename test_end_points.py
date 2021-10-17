from itertools import dropwhile
import unittest
from main import app , CartItem , Category , Customer , Product , db
import json

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
        self.assertEqual(data['customer']['total_price'], 36800.0)
        
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
        # check for new added product and delete it from database 
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
        # check for new added category and delete it from database 
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

    
if __name__ == '__main__':
    unittest.main()