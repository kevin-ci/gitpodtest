from django.conf.urls import url
from .views import all_cars

urlpatterns = [
    url('', all_cars),
]