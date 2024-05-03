from django.urls import path
from home.views import *

urlpatterns = [
    path('cat/', CatView.as_view(), name='cat'),
    path('about/', AboutView.as_view(), name='about'),
    path('books/', BookList.as_view(), name='books'),
    path('books/<int:pk>', BookDetail.as_view(), name='book'),
    path('orders/', OrderCreateList.as_view(), name='orders'),
    path('orders/<int:pk>', OrderDetail.as_view(), name='order'),
]