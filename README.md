# Shopping - Store

## End Points

- GET  /   redirect to login page
- GET /login     login using auth0
- GET /logout  logout using auth0
- GET /products get all products /
- GET /products/<int:product_id>
- GET /customers/<int:customer_id
- GET  /customers/int:customer_id/items   gets cart item for a user
- GET /categories
- POST /item
- POST  /product
- POST  /category
- POST  /customer
- PATCH /customers/<int:customer_id>
- PATCH /products/<int:product_id>
- PATCH /categories/<int:category_id>
- DELETE /customers/<int:customer_id>
- DELETE /items/<int:item_id>
- DELETE /products/<int:product_id>
- DELETE /categories/<int:category_id>

---

## Roles and Permission

- dev - public
    - GET /products get all products /
    - GET /products/<int:product_id>
    - GET /customers/<int:customer_id
    - GET  /customers/int:customer_id/items   gets cart item for a user
    - GET /categories
    - POST /item
    - POST  /customer
    - PATCH /customers/<int:customer_id>
    - DELETE /customers/<int:customer_id>
    
- product  admin role
    - all dev - public end points
    - POST  /product
    - PATCH /products/<int:product_id>
    - DELETE /products/<int:product_id>
- Admin
    - all dev - public end points
    - all product - admin end proints
    - POST  /category
    - PATCH /categories/<int:category_id>
    - DELETE /categories/<int:category_id>
    

---

Postman test end points in shopping -api.postman_collection.json file

product role JWT : 

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkNiLV82dmRxTXJ4YUxLV0hKWHRkZyJ9.eyJpc3MiOiJodHRwczovL3VkLWNhcC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTMwMTczNzI2Mzc3ODA3MjMyNjIiLCJhdWQiOiJzaG9waW5nIiwiaWF0IjoxNjM1MDY5NTA3LCJleHAiOjE2MzUwNzY3MDcsImF6cCI6IkJ6enQyOTNRMVh6RW5lVGY2bHQ0RE9OenZWcnJVb1VYIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6cHJvZHVjdCIsInBhdGNoOnByb2R1Y3QiLCJwb3N0OnByb2R1Y3QiXX0.p0CeBbpp6H7h5K_ax0UkAb0k1NZSh5N_75j_1de1pouO0Td3gpjtpB1sDv08kURQW8z6gqnLWP0n2ADNZuhz5kBT7GmuvgPsFUfM9sy6_ag-_6A84DFQSkAq2dkS_7QEDphgcAJtlRGry7YvU149AVmEzQnG3ijLRjgyW_Rb-k_wtQrTw04hJ4EIrFAuB6Cf-9GoLf2IOLoUnywfrwNM11Qbv8n9Dq6feY9DdXhbQyt4rwhZlVOfRRn7YoqAqgYX8aSPfstMPT9Of_sIlZYeC263LI42YuNqsK9DynSSSkAZRufd24tWMPGX3x105UDXy44PaiKGxw-nuwtsP25vPw 

Admin JWT :

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkNiLV82dmRxTXJ4YUxLV0hKWHRkZyJ9.eyJpc3MiOiJodHRwczovL3VkLWNhcC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTEyMzExMDM3Nzk1ODI2OTIzNDYiLCJhdWQiOiJzaG9waW5nIiwiaWF0IjoxNjM1MDY5NzkzLCJleHAiOjE2MzUwNzY5OTMsImF6cCI6IkJ6enQyOTNRMVh6RW5lVGY2bHQ0RE9OenZWcnJVb1VYIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6Y2F0ZWdvcnkiLCJkZWxldGU6cHJvZHVjdCIsInBhdGNoOmNhdGVnb3J5IiwicGF0Y2g6cHJvZHVjdCIsInBvc3Q6Y2F0ZWdvcnkiLCJwb3N0OnByb2R1Y3QiXX0.Wl7iTDm1ZjNQKy2goBTMTd3ECJrLKRQ7hjsQwPnilExc0CNpgLu1B74zwQ7tWMZyqJ5JCSH2JI8kjaWHiGG7eYWCqcCrVXavpkF2YCGXUFf1iZY6lnK6tnFCx-5vEtOwu7glDvy1KZSxH9p4FZVBx2xqlFXwhVdznbsgO75Ay97ggiws9x67z9MC45T5NMF4CRMGTMxDzkO2EhCkS4ZPPq7TQfTTXPscaK_bdMQJTJ2i7H4Z1MHpWNRzxjSIigyvTC5Q4JOPZuoxZrYhxR-Za7dzydAVcvufO-Q_qZH7ffCLuWddnOrPhWu_EwfcbiUBdZRjL5A2xY02KIsD4u1-eA

---

test_end_points.py  File : 

unit test for  success and failure  for each end point 

---

add_data.py File :

- to be able to run end point unit test
- fill database with data

Database design

![database.png](Shopping%20-%20Store%209f4bd29da0544e1c8da3f84d74b98e9a/database.png)