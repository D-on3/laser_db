from django.contrib.auth import authenticate
from rest_framework import generics
from materials.models import Material
from author.models import Author
from machines.models import Machine
from colors.models import ColorOutcome
from .serializers import MaterialSerializer, AuthorSerializer, MachineSerializer, ColorOutcomeSerializer
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def obtain_auth_token(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if username and password:
        token = Token.objects.filter(user__username=username).first()
        if token:
            token.delete()
        user = authenticate(request, username=username, password=password)
        if user:
            token = Token.objects.create(user=user)
            return Response({'token': token.key})
    return Response(status=400)
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
