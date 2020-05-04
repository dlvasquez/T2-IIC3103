from rest_framework import generics, mixins, viewsets, response, status
from ApiRest.models import Hamburguesa, Ingrediente
from .serializers import HamburguesaSerializer, IngredienteSerializer


class HamburguesasRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Hamburguesa.objects.all()
    serializer_class = HamburguesaSerializer

    def get_queryset(self):
        return Hamburguesa.objects.all()

    def delete(self, request):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)

            self.perform_destroy(instance)
            return response.Response(
                {"code": "200", "descripcion": 'hamburguesa eliminada'},
                status=status.HTTP_200_OK
            )

        except:
            return response.Response(
                {"code": "404", "descripcion": 'hamburguesa inexistente'},
                status=status.HTTP_404_NOT_FOUND
            )


class HamburguesasListCreateView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    queryset = Hamburguesa.objects.all()
    serializer_class = HamburguesaSerializer

    def get_queryset(self):
        return Hamburguesa.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class IngredientesRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer

    def get_queryset(self):
        return Ingrediente.objects.all()


class IngredientesListCreateView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer

    def get_queryset(self):
        return Ingrediente.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class IngredientesEnHamburguesaView(generics.RetrieveUpdateDestroyAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    lookup_field = 'id'
    queryset = Hamburguesa.objects.all()
    serializer_class = HamburguesaSerializer

    def get_queryset(self):
        return Ingrediente.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
