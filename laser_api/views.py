from rest_framework import generics
from materials.models import Material
from author.models import Author
from machines.models import Machine
from colors.models import ColorOutcome
from .serializers import MaterialSerializer, AuthorSerializer, MachineSerializer, ColorOutcomeSerializer

class MaterialListAPIView(generics.ListAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class MaterialDetailAPIView(generics.RetrieveAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class AuthorListAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailAPIView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class MachineListAPIView(generics.ListAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

class MachineDetailAPIView(generics.RetrieveAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

class ColorOutcomeListAPIView(generics.ListAPIView):
    queryset = ColorOutcome.objects.all()
    serializer_class = ColorOutcomeSerializer

class ColorOutcomeDetailAPIView(generics.RetrieveAPIView):
    queryset = ColorOutcome.objects.all()
    serializer_class = ColorOutcomeSerializer
