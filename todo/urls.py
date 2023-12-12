from django.urls import path
from .views import to_do_items

urlpatterns = [
    path('',to_do_items)
    ]