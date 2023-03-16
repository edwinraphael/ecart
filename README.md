# ecart



1-localhost:8000/account(post)- for user registartion
2-localhost:8000/token-to generate token by giving username and password
3-localhost:8000/ecart/categories-to list all categories,products are added by the category
4-localhost:8000/ecart/categories/category_id-list specific category
5-localhost:8000/ecart/categories/category_id/add_product(post)-adding product to specific category
6-localhost:8000/ecart/categories/1/products(get)-list all products of category_id=1
7-localhost:8000/ecart/products-list all the products in ecart
8-localhost:8000/ecart/products/product_id-list a single product with the given id
9-localhost:8000/ecart/products/product_id/add_to_cart-for adding product to the cart
10-localhost:8000/ecart/carts-shows cart items of logged user
11-localhost:8000/ecart/products/product_id/add_review-adding review to the single product
12-localhost:8000/ecart/products/product_id/get_review-to get review of the single product






Admin-only  this user can manage categories and adding products,created with username=admin, password=admin.Other users can view products,add reviews and they can add ptoducts to the cart
