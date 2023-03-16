from django.urls import path
from ecart import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("categories",views.CategoryView,basename="categories")
router.register("account",views.UsersView,basename="signup")
router.register("products",views.ProductsView,basename="product")
router.register("carts",views.CartView,basename="cart")

urlpatterns = [


]+router.urls
