from django.urls import path

from .views import item_api, item_list

urlpatterns = [
    path('api/items/', item_api, name='item_api'),
    path('', item_list, name='item_list'),
]
