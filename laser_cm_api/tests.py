from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.urls import reverse
from pages.models import LaserMarkingParameters

class LaserMarkingParametersAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_list_marking_parameters(self):
        url = reverse('laser_cm_api:marking-parameters-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), LaserMarkingParameters.objects.count())

    def test_retrieve_marking_parameter(self):
        marking_parameter = LaserMarkingParameters.objects.first()
        url = reverse('laser_cm_api:marking-parameters-detail', args=[marking_parameter.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['pk'], marking_parameter.pk)

class ColorSearchAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_valid_color_search(self):
        url = reverse('laser_cm_api:color-search-api')
        hex_color = '#FF5733'
        response = self.client.post(url, {'hex_color': hex_color}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('matching_colors', response.data)

    def test_invalid_color_search(self):
        url = reverse('laser_cm_api:color-search-api')
        response = self.client.post(url, {'hex_color': 'invalid_color'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Add more tests as needed
