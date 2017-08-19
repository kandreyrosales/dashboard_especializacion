from .views import VotoListView
from django.conf.urls import url

urlpatterns = [
    url(r'^voto_list/', VotoListView.as_view(), name='voto_list')
]