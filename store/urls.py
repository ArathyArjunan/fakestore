from django.urls import path
from store import views
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("category",views.CategoryView,basename="category")
router.register("products",views.ProductView,basename="products")

urlpatterns = [
    path("register/",views.UserCreationView.as_view()),
    path("token/",ObtainAuthToken.as_view())
    
]+router.urls
