from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.book_list),
    path('create/', views.create_book),
    path('edit/', views.edit_book),
    path('delete/', views.delete_book),
]
