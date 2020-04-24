from django.urls import path
from .views import index, contact, aboutus, store, service



urlpatterns = [
    path('', index),
    path('contact', contact),
    path('aboutus', aboutus),
    path('store', store),
    path('service', service),
    path('index', index),
]