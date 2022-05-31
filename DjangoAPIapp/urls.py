from django.contrib import admin
from django.urls import path
from .views import ListCategory,DetailCategory,ListBook,DetailBook,ListProduct,DetailProduct

urlpatterns = [
    path('categories',ListCategory.as_view(),name='categories'),
    path('categories/<int:pk>/',DetailCategory.as_view(),name='categories'),

    path('book',ListBook.as_view(),name='book'),
    path('book/<int:pk>/',DetailBook.as_view(),name='book'),
    
    path('product',ListProduct.as_view(),name='product'),
    path('product/<int:pk>/',DetailProduct.as_view(),name='product'),
]