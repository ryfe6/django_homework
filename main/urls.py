from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from main.views import product_list, contacts, product_view
from main.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', product_list, name='product_list'),
    path("contacts/", contacts, name='contacts'),
    path('main/<int:pk>/', product_view, name='product_view'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
