from django.urls import path
from app import views
urlpatterns=[
    path('',views.homeview,name='homepage'),
    path('books',views.booksview,name='bookspage'),
    path('author',views.authorview,name='authorpage'),
    
]