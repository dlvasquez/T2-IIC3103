from rest_framework import serializers
from .models import Hamburguesa, Ingrediente
from django.urls import reverse


class IngredienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ('id', 'nombre', 'descripcion')


class HamburguesaSerializer(serializers.HyperlinkedModelSerializer):
    ingredientes = serializers.HyperlinkedRelatedField(
        many=True, read_only=True,
        view_name='ApiRest:ingrediente-rud', lookup_url_kwarg='id'
    )

    class Meta:
        model = Hamburguesa
        fields = ('id', 'nombre', 'descripcion',
                  'precio', 'imagen', 'ingredientes')
