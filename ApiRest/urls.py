from django.conf.urls import include, url
from .views import HamburguesasRudView, HamburguesasListCreateView, IngredientesRudView, IngredientesListCreateView, IngredientesEnHamburguesaView
from django.urls import path
urlpatterns = [
    path('hamburguesa', HamburguesasListCreateView.as_view(),
         name='hamburguesa-create'),
    path('hamburguesa/<int:id>',
         HamburguesasRudView.as_view(), name='hamburguesa-rud'),
    path('ingrediente', IngredientesListCreateView.as_view(),
         name='ingrediente-create'),
    path('ingrediente/<int:id>',
         IngredientesRudView.as_view(), name='ingrediente-rud'),
    path('hamburguesa/<int:id>/ingrediente/<int:id2>',
         IngredientesEnHamburguesaView.as_view(), name='ingredienteEnHamburguesa-ud')
]
app_name = 'ApiRest'
