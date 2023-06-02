from django.contrib import admin
from django.urls import include, path
from test_app.views import get_manufacturer_id

urlpatterns = [
    path(r"get_id_man/<int:id>", get_manufacturer_id, name='get_id'),
]