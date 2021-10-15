End points
    Two GET requests
    One POST request
    One PATCH request
    One DELETE request

/products                                  GET 
/products/<int:category_id>                GET
/customers/<int:customer_id>/items         GET   returns a list of cart items for a user
/categories                                GET 
/customers/<int:customrt_id>               GET

/product                                   POST   (admin and product_admin rolles)
/category                                  POST   (admin role)
/customer                                  POST   
/product                                   POST   

/customer/<int:customer_id>                PATCH
/product/<int:product_id>                  PATCH   (admin and  product_admin rolles)
/category/<id:category_id>                 PATCH   (admin role)


/customer/<int:customer_id>                DELETE
/item/<int:item_id>                        DELETE
/product/<int:product_id>                  DELETE  (admin role, product_admin rolles)
/category/<int:category_id>                DELETE  (admin role)




Roles and tests

Roles will include at least…
    Two roles with different permissions
    Permissions specified for all endpoints

Tests will include at least….
    One test for success behavior of each endpoint
    One test for error behavior of each endpoint
    At least two tests of RBAC for each role


