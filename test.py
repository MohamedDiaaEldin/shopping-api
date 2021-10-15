from  main import Category , CartItem , Product , Customer , db

first_customer = Customer(first_name='mohamed', last_name='diaa', address='6th of october city',
                           phone='012744444', total_price=0.0)


category = Category(category_name='laptops')
product = Product(product_name='gammig leptop' , product_description='core i7 - 8 ram - amd 4 gb' , category_id=1)
cart_item = CartItem(quantity=1, product_id=2, customer_id=1)

db.session.add(first_customer)
db.session.commit()
                    