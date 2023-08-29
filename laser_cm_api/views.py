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


# The class LaserMarkingParametersList is a generic ListAPIView.
class LaserMarkingParametersList(generics.ListAPIView):
    serializer_class = LaserMarkingParametersSerializer

    def get_queryset(self):
        """
        The `get_queryset` function filters `LaserMarkingParameters` objects based
        on a given hex color or returns all objects if no color is provided.
        :return: The code is returning a list of LaserMarkingParameters objects
        that match the specified hex_color or all LaserMarkingParameters objects
        if no hex_color is provided.
        """
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


# The class LaserMarkingParametersDetail is a generic API view for retrieving a
# specific laser marking parameter detail.
class LaserMarkingParametersDetail(generics.RetrieveAPIView):
    queryset = LaserMarkingParameters.objects.all()
    serializer_class = LaserMarkingParametersSerializer


def landing_page(request):
    """
    The `landing_page` function renders the `api.html` template for the Laser CM
    API.

    :param request: The request parameter is an object that represents the HTTP
    request made by the client. It contains information such as the HTTP method
    (GET, POST, etc.), headers, user session, and any data sent in the request
    body. In this case, it is used to render the 'laser_cm_api
    :return: the rendered HTML template 'laser_cm_api/api.html'.
    """
    return render(request, 'laser_cm_api/api.html')


# The ColorSearchAPIView is an API view that handles color search functionality.
class ColorSearchAPIView(APIView):
    def post(self, request, *args, **kwargs):
        """
        The above function takes a hex color as input, converts it to RGB,
        classifies it based on a color spectrum, and then matches it with colors
        in a database based on the classification.

        :param request: The `request` parameter is an object that represents the
        HTTP request made to the server. It contains information such as the
        request method (GET, POST, etc.), headers, body, and query parameters. In
        this code snippet, the `request` object is used to access the data sent in
        the
        :return: The code is returning a response with the matching colors in the
        database that match the given hex color. The matching colors are
        serialized using the LaserMarkingParametersSerializer and returned in the
        response data. The status code of the response is either 200 if the
        request is valid or 400 if there are validation errors.
        """
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
