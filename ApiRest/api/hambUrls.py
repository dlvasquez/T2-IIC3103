from django.conf.urls import include, url
from .views import HamburguesasRudView, HamburguesasListCreateView, IngredientesRudView, IngredientesListCreateView

urlpatterns = [
    url(r'^$', HamburguesasListCreateView.as_view(), name='hamburguesa-create'),
    url(r'^(?P<id>\d+)/$', HamburguesasRudView.as_view(), name='hamburguesa-rud')
]
app_name = 'ApiRest'
