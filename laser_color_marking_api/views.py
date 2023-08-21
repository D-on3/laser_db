# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_api_key.models import APIKey
from rest_framework_api_key.permissions import HasAPIKey
from pages.models import LaserSource, LaserMarkingParameters
from .serializers import LaserSourceSerializer, LaserMarkingParametersSerializer
from rest_framework import generics

class GenerateAPIKeyView(APIView):
    permission_classes = [HasAPIKey]

    def post(self, request, *args, **kwargs):
        # Generate a new API key for the requesting user
        user = self.request.user
        api_key, key = APIKey.objects.create_key(name=user.username)
        return Response({'api_key': key}, status=status.HTTP_201_CREATED)

class LaserSourceList(generics.ListCreateAPIView):
    queryset = LaserSource.objects.all()
    serializer_class = LaserSourceSerializer

class LaserSourceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LaserSource.objects.all()
    serializer_class = LaserSourceSerializer

class LaserMarkingParametersList(generics.ListCreateAPIView):
    queryset = LaserMarkingParameters.objects.all()
    serializer_class = LaserMarkingParametersSerializer

class LaserMarkingParametersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LaserMarkingParameters.objects.all()
    serializer_class = LaserMarkingParametersSerializer
