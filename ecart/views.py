from django.shortcuts import render

# Create your views here.
from ecart.models import Category,Products,Cart,Reviews
from django.contrib.auth.models import User
from ecart.serializers import CategorySerialzer,ProductSerializer,UserSerializer,CartSerializer,ReviewSerializer
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework.response import Response
from rest_framework import permissions,authentication
from rest_framework.decorators import action



class UsersView(ViewSet):
    def create(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def list(self, request, *args, **kwargs):
        qs = User.objects.all()
        serializer = UserSerializer(qs, many=True)
        return Response(data=serializer.data)

    def destroy(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = User.objects.get(id=id)
        qs.delete()
        return Response({"msg": "deleted"})


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerialzer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
#localhost:8000/ekart/categories/{id}/add_product
    @action(methods=["post"],detail=True)
    def add_product(self,request,*args,**kwargs):

        id=kwargs.get("pk")
        cat=Category.objects.get(id=id)
        serializer = ProductSerializer(data=request.data,context={"category":cat})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    @action(methods=["get"],detail=True)
    def products(self,request,*args,**kwargs):
        cid=kwargs.get("pk")
        cat=Category.objects.get(id=cid)
        products=cat.products_set.all()
        serializer=ProductSerializer(products,many=True)
        return Response(data=serializer.data)


  #localhost:8000/ekart/categories/{id}/get_product
class ProductsView(ViewSet):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def list(self,request,*args,**kwargs):

        all_products=Products.objects.all()

        serializer=ProductSerializer(all_products,many=True)
        return Response(data=serializer.data)

    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Products.objects.get(id=id)
        serializer=ProductSerializer(qs,many=False)
        return Response(data=serializer.data)

    @action(methods=["post"],detail=True)
    def add_to_cart(self,request,*args,**kwargs):
        pid = kwargs.get("pk")
        product = Products.objects.get(id=pid)
        user = request.user
        serializer=CartSerializer(data=request.data,context={"product":product,"user":user})
        if serializer.is_valid():
            print(user)
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    @action(methods=["post"],detail=True)
    def add_review(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        prd=Products.objects.get(id=id)
        user=request.user
        serializer=ReviewSerializer(data=request.data,context={"user":user,"product":prd})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

#localhost:8000/ekart/products/1/get_review
    @action(methods=["get"],detail=True)
    def get_review(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        product=Products.objects.get(id=id)
        reviews=product.reviews_set.all()
        serializer=ReviewSerializer(reviews,many=True)
        return Response(data=serializer.data)

# class CartsView(ModelViewSet):
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     def create(self, request, *args, **kwargs):
#         id=kwargs.get("pk")
#         prd=Products.objects.get(id=id)
#         user=request.user
#         Cart.objects.create(product=prd,user=user)
#         return Response(data)

class CartView(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):

        return Cart.objects.filter(user=self.request.user)
