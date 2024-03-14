from django.urls import path

from main.views import product_list, contacts


urlpatterns = [
    path('', product_list),
    path("contacts/", contacts)
    ]