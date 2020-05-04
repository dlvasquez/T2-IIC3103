from django.conf.urls import include, url
from .views import IngredientesRudView, IngredientesListCreateView

urlpatterns = [
    url(r'^$', IngredientesListCreateView.as_view(), name='ingrediente-create'),
    url(r'^(?P<id>\d+)/$', IngredientesRudView.as_view(), name='ingrediente-rud')
]
app_name = 'ApiRest'
