from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pages.models import LaserMarkingParameters
from .serializers import LaserMarkingParametersSerializer, \
    ColorSearchSerializer
from pages.utils import ColorSpectrum, hex_to_rgb
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pages.models import LaserMarkingParameters
from .serializers import ColorSearchSerializer
from pages.utils import ColorSpectrum
from django.shortcuts import render


class LaserMarkingParametersList(generics.ListAPIView):
    serializer_class = LaserMarkingParametersSerializer

    def get_queryset(self):
        hex_color = self.request.query_params.get('hex_color', None)
        if hex_color:
            rgb_color = hex_to_rgb(hex_color.lstrip('#'))
            form_color = ColorSpectrum(
                [rgb_color]).classify_colors_by_spectrum()
            filtered_dict = {key: value for key, value in form_color.items()
                             if value}

            queryset = LaserMarkingParameters.objects.all()
            matching_colors = []

            for parameters in queryset:
                current_color_classifier = ColorSpectrum([
                    (parameters.color_red, parameters.color_green,
                     parameters.color_blue)
                ]).classify_colors_by_spectrum()
                current_color_classifier = {key: value for key, value in
                                            current_color_classifier.items()
                                            if value}

                if current_color_classifier.keys() == filtered_dict.keys():
                    matching_colors.append(parameters)

            return matching_colors
        else:
            return LaserMarkingParameters.objects.all()


class LaserMarkingParametersDetail(generics.RetrieveAPIView):
    queryset = LaserMarkingParameters.objects.all()
    serializer_class = LaserMarkingParametersSerializer


def landing_page(request):
    return render(request, 'laser_cm_api/api.html')


class ColorSearchAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ColorSearchSerializer(data=request.data)
        if serializer.is_valid():
            hex_color = serializer.validated_data['hex_color']
            hex_color = hex_color.lstrip('#')
            rgb_color = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

            if len(rgb_color) != 3:
                return Response({'error_message': 'Invalid RGB color'},
                                status=status.HTTP_400_BAD_REQUEST)

            form_color = ColorSpectrum(
                [rgb_color]).classify_colors_by_spectrum()
            filtered_dict = {key: value for key, value in form_color.items()
                             if value}

            all_colors_in_db = LaserMarkingParameters.objects.all()

            matching_colors = []
            for current_color in all_colors_in_db:
                current_color_classifier = ColorSpectrum([
                    (current_color.color_red, current_color.color_green,
                     current_color.color_blue)
                ]).classify_colors_by_spectrum()
                current_color_classifier = {key: value for key, value in
                                            current_color_classifier.items()
                                            if value}

                if current_color_classifier.keys() == filtered_dict.keys():
                    matching_colors.append(current_color)

            serialized_matching_colors = LaserMarkingParametersSerializer(
                matching_colors, many=True)

            return Response(
                {'matching_colors': serialized_matching_colors.data},
                status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
