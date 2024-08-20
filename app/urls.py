from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart , name="cart"),
    path('about/', views.about , name="about"),
    path('contact/', views.contact , name="contact"),
    path('main/', views.main , name="main"),
    path('store/', views.store , name="store"),
    # path('category/', views.category , name="category"),
    # path('category/', views.CategoryView.as_view, name="category"),
    path('category/<slug:val>/', views.CategoryView.as_view(), name="category"),
    path('product-detail/<int:pk>/', views.ProductDetail.as_view(), name="product-detail"),

    
]
