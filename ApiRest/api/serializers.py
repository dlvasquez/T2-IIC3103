from rest_framework import serializers
from ApiRest.models import Hamburguesa, Ingrediente


class HamburguesaSerializer(serializers.HyperlinkedModelSerializer):
    ingredientes = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='ingrediente-detail'
    )

    class Meta:
        model = Hamburguesa
        fields = ('id', 'nombre', 'descripcion',
                  'precio', 'imagen', 'ingredientes')

    # def validate_nombre(self, value):
    #     qs = Hamburguesa.objects.filter(nombre__iexact=value)
    #     if self.instance:
    #         qs = qs.exclude(id=self.instance.id)
    #     if qs.exists():
    #         raise serializers.ValidationError("The name must be unique")
    #     return value


class IngredienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ('id', 'nombre', 'descripcion')
