from django.conf.urls import url
from .views import do_search

urlpatterns = [
    path('', do_search, name='search'),
    ]