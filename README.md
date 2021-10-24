# README

# Shopping - Store

## Domain Name

[https://shopping-cap.herokuapp.com/](https://shopping-cap.herokuapp.com/)

## End Points

- GET / redirect to login page
- GET /login login using auth0
- GET /logout logout using auth0
- GET /products get all products /
- GET /products/
- GET /customers/<int:customer_id
- GET /customers/int:customer_id/items gets cart item for a user
- GET /categories
- POST /item
- POST /product
- POST /category
- POST /customer
- PATCH /customers/
- PATCH /products/
- PATCH /categories/
- DELETE /customers/
- DELETE /items/
- DELETE /products/
- DELETE /categories/

---

## Roles and Permission

- dev - public
    - GET /products get all products /
    - GET /products/
    - GET /customers/<int:customer_id
    - GET /customers/int:customer_id/items gets cart item for a user
    - GET /categories
    - POST /item
    - POST /customer
    - PATCH /customers/
    - DELETE /customers/
- product admin role
    - all dev - public end points
    - POST /product
    - PATCH /products/
    - DELETE /products/
- Admin
    - all dev - public end points
    - all product - admin end proints
    - POST /category
    - PATCH /categories/
    - DELETE /categories/
    

---

Postman test end points in shopping -api.postman_collection.json file

product role JWT :

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkNiLV82dmRxTXJ4YUxLV0hKWHRkZyJ9.eyJpc3MiOiJodHRwczovL3VkLWNhcC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTMwMTczNzI2Mzc3ODA3MjMyNjIiLCJhdWQiOiJzaG9waW5nIiwiaWF0IjoxNjM1MDc5OTM1LCJleHAiOjE2MzUwODcxMzUsImF6cCI6IkJ6enQyOTNRMVh6RW5lVGY2bHQ0RE9OenZWcnJVb1VYIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6cHJvZHVjdCIsInBhdGNoOnByb2R1Y3QiLCJwb3N0OnByb2R1Y3QiXX0.Iibnb6_T3lzGwfW23yxil0ePrsT5JqQ4pl0Svx1Eliy4VUP1XNwUKeu3SJysOQcrg1vQo_uOGChBgCjLtskHP7cVbwNFzw3igM1tEBNHLEEeJ77iZBr4pOdB7RyOK_MYMCakjWZImDltysydJRLFIZ8rtuBiTNL9QeZjr2kLdit_nVYxH-7K0lDZ8uQh6kuChoeB63lyj9RgE7PXsvRdiVFx63mibFMU6GSNRXGM2NblNfpUxWfgIC3oIM-S0qxgMMdpngL3RBHbvS30qOYi3DNe5jJoRtelxnozTcgl477Bp2saQ4yk-yCwv5RJrccX8hG1_vFt8stC5QCrC5Rw0A

Admin JWT :

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkNiLV82dmRxTXJ4YUxLV0hKWHRkZyJ9.eyJpc3MiOiJodHRwczovL3VkLWNhcC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTEyMzExMDM3Nzk1ODI2OTIzNDYiLCJhdWQiOiJzaG9waW5nIiwiaWF0IjoxNjM1MDgwMjg5LCJleHAiOjE2MzUwODc0ODksImF6cCI6IkJ6enQyOTNRMVh6RW5lVGY2bHQ0RE9OenZWcnJVb1VYIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6Y2F0ZWdvcnkiLCJkZWxldGU6cHJvZHVjdCIsInBhdGNoOmNhdGVnb3J5IiwicGF0Y2g6cHJvZHVjdCIsInBvc3Q6Y2F0ZWdvcnkiLCJwb3N0OnByb2R1Y3QiXX0.EFXoMH2UKHaRFtqAqCWLiP9hRPrCVBF6Xsjwzg9p4DYwwNpfT3L03JwwhyNADi2ORF5FWPN7LOOJHYgKOrZ9rFnJO6zmUbcWv9w1jRm7UUAklOML1AAuqEXOdTsFoyhjnDPOMPZ6JSsDabvcXhHxaUCcPvzSQgYRqO3bK8lTP4yEt_PLHN6JGqygKrgIJUuJafIRahHqT5iiGnIUWSP-udtSXZ7WYCJ1Rg2qkDNL5dazlHQrIekQ-MMN9bvBTfUld587_ok_7IihdCpk94R7it1MVCQ0oM-PCWC2CY-zZupsuA29N4zvPVyAfmeJRcj0xVYz4TcyhoBtbT-BXPV9pw

---

test_end_points.py File :

unit test for success and failure for each end point

---

add_data.py File :

- to be able to run end point unit test
- fill database with data

---

/database-design/database.png :

database design