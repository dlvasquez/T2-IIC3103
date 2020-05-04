from django.shortcuts import render
from rest_framework import generics, mixins, viewsets, status
from .models import Hamburguesa, Ingrediente
from .serializers import HamburguesaSerializer, IngredienteSerializer
from rest_framework.response import Response


class HamburguesasRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Hamburguesa.objects.all()
    serializer_class = HamburguesaSerializer

    def get_queryset(self):
        return Hamburguesa.objects.all()

    def destroy(self, request, *args, **kwargs):
        try:

            instancia = self.get_object()
            serializer = self.get_serializer(instancia)

            self.perform_destroy(instancia)
            return Response(
                {"message": 'hamburguesa eliminada'},
                status=status.HTTP_200_OK
            )

        except:
            return Response(
                {"message": 'hamburguesa inexistente'},
                status=status.HTTP_404_NOT_FOUND
            )

    def patch(self, request, *args, **kwargs):
        try:
            instancia = Hamburguesa.objects.get(id=kwargs['id'])
        except:
            return Response(
                {"message": 'Hamburguesa inexistente'},
                status=status.HTTP_400_BAD_REQUEST
            )
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        try:
            instancia = self.get_object()
            serializer = self.get_serializer(
                instancia, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instancia, '_prefetched_objects_cache', None):
                instancia._prefetched_objects_cache = {}

            return Response({"message": "operacion exitosa"}, status=status.HTTP_200_OK)

        except:
            return Response({"message": "Parámetros inválidos"}, status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        serializer.save()


class HamburguesasListCreateView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    queryset = Hamburguesa.objects.all()
    serializer_class = HamburguesaSerializer

    def get_queryset(self):
        return Hamburguesa.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class IngredientesRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer

    def get_queryset(self):
        return Ingrediente.objects.all()

    def delete(self, request, *args, **kwargs):
        instancia = self.get_object()
        serializer = self.get_serializer(instancia)
        lista_ingredientes = Hamburguesa.objects.values_list(
            'ingredientes', flat=True)
        if instancia.id in lista_ingredientes:
            return Response(
                {"message": 'Ingrediente no se puede borrar, se encuentra presente en una hamburguesa'},
                status=status.HTTP_409_CONFLICT
            )
        else:
            self.perform_destroy(instancia)
            return Response(
                {"message": 'operacion exitosa'},
                status=status.HTTP_200_OK
            )


class IngredientesListCreateView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer

    def get_queryset(self):
        return Ingrediente.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class IngredientesEnHamburguesaView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Hamburguesa.objects.all()
    serializer_class = HamburguesaSerializer

    def get_queryset(self):
        return Ingrediente.objects.all()

    def put(self, request, *args, **kwargs):
        try:
            instancia = Hamburguesa.objects.get(id=kwargs['id'])
        except:
            return Response(
                {"message": 'Id de hamburguesa inválido'},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            instancia2 = Ingrediente.objects.get(id=kwargs['id2'])
        except:
            return Response({"message": 'Ingrediente inexistente'},
                            status=status.HTTP_404_NOT_FOUND
                            )
        instancia.ingredientes.add(instancia2)
        kwargs['put'] = '1'

        instancia = self.get_object()
        serializer = self.get_serializer(
            instancia, data=request.data, partial=True)
        serializer.is_valid()
        self.perform_update(serializer)

        return Response(
            {"message": 'Ingrediente agregado'},
            status=status.HTTP_201_CREATED
        )


# maneja si existen los ids solicitados y remueve la instancia


    def delete(self, request, *args, **kwargs):
        try:
            instancia = Hamburguesa.objects.get(id=kwargs['id'])

        except:
            return Response(
                {"message": 'Id de hamburguesa inválido'},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            instancia2 = Ingrediente.objects.get(id=kwargs['id2'])
        except:
            return Response(
                {"message": 'Ingrediente inexistente'},
                status=status.HTTP_404_NOT_FOUND
            )
        instancia.ingredientes.remove(instancia2)
        kwargs['delete'] = '1'
        instancia = self.get_object()
        serializer = self.get_serializer(
            instancia, data=request.data, partial=True)
        serializer.is_valid()
        serializer.save()
        self.perform_update(serializer)

        return Response(
            {"message": 'ingrediente retirado'},
            status=status.HTTP_200_OK
        )

    def perform_update(self, serializer):
        serializer.save()
