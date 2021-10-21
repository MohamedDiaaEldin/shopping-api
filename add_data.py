from  main import Category , CartItem , Product , Customer 


def add_products():
    f = open('data/products.txt', 'r')
    for line in f.readlines():        
        data = line.split(', ')
        product_name = data[0].strip()
        category_id = data[1].strip()
        product_description = data[2].strip()
        product_id = data[3].strip()
        price = float(data[4].strip())
        product = Product(id=int(product_id), product_name=product_name, product_description=product_description, category_id=int(category_id), price=price)
        product.add_to_database()
    

def add_categories():
    f = open('data/categories.txt', 'r')
    for line in f.readlines():                
        data = line.split(', ')
        category_id = data[0].strip()
        category_name = data[1].strip()
        category  = Category(id=int(category_id),  category_name=category_name)
        category.add_to_database()

def add_customers():
    f = open('data/customers.txt')
    for line in f.readlines():
        data = line.split(', ')
        
        customer_id = int(data[0].strip())
        first_name = data[1].strip()
        last_name = data[2].strip()
        address = data[3].strip()
        phone = data[4].strip()
        total_price = float(data[5].strip())

        customer = Customer(id=customer_id, first_name=first_name, last_name=last_name, address=address, phone=phone, total_price=total_price)
        customer.add_to_database()

def add_cart_item():
    f = open('data/cart_item.txt', 'r')
    for line in f.readlines():
        data = line.split(', ')
        item_id = data[0].strip()
        quantity = data[1].strip()
        product_id = data[2].strip()
        customer_id = data[3].strip()
        item = CartItem(id=item_id, quantity=quantity, product_id=product_id, customer_id=customer_id)
        item.add_to_database()
        ## update customer total price 
        customer = Customer.query.get(customer_id)
        customer.total_price += int(quantity) * Product.query.get(product_id).price
        customer.update()



'''
you should add categories before products  
you should add products and customer before cart_item  

'''
#first 
add_categories()

#second
add_products()

# third 
add_customers()

#fourth 
add_cart_item()
