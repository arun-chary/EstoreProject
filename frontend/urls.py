
from django.urls import path
from . import views


urlpatterns = [

    path('', views.product, name = 'products'),
    path('<int:id>/', views.product_details, name = 'product_details'),

]