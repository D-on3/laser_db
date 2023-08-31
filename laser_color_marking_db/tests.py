
from .forms import AddSampleForm, LaserSourceForm, MaterialForm,LaserMarkingParametersForm

from .forms import AddSampleForm, LaserSourceForm, MaterialForm
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import LaserSource, Material, LaserMarkingParameters
from .forms import GaeParamsForm, LaserSourceForm, MaterialForm


class PagesFormsTestCase(TestCase):

    def setUp(self):
        self.material = Material.objects.create(name='Test Material', description='Test Description')
        self.laser_source = LaserSource.objects.create(name='Test Laser', type_of_laser='Diode', wavelength=532)

    class FormTests(TestCase):

        def test_add_sample_form_valid(self):
            laser_source = LaserSource.objects.create(
                name='Test Laser', type_of_laser='Diode', wavelength=532
            )
            material = Material.objects.create(
                name='Test Material', description='This is a test material.'
            )
            form_data = {
                'laser_source': laser_source.pk,
                'material': material.pk,
                'scanning_speed': 100,
                'average_power': 10.5,
                'authors': 'Test Author',
                'research_date': '2023-08-29 12:00:00',
            }
            form = AddSampleForm(data=form_data)
            self.assertTrue(form.is_valid())

        def test_laser_source_form_valid(self):
            form_data = {
                'name': 'New Laser',
                'type_of_laser': 'Gas',
                'wavelength': 1064,
            }
            form = LaserSourceForm(data=form_data)
            self.assertTrue(form.is_valid())

        def test_material_form_valid(self):
            form_data = {
                'name': 'New Material',
                'description': 'A new material.',
            }
            form = MaterialForm(data=form_data)
            self.assertTrue(form.is_valid())

        def test_add_sample_form_invalid(self):
            # Test with missing required fields
            form_data = {}
            form = AddSampleForm(data=form_data)
            self.assertFalse(form.is_valid())
            self.assertEqual(len(form.errors), 8)  # Number of required fields

        def test_laser_source_form_invalid(self):
            # Test with missing required fields
            form_data = {}
            form = LaserSourceForm(data=form_data)
            self.assertFalse(form.is_valid())
            self.assertEqual(len(form.errors), 3)  # Number of required fields

        def test_material_form_invalid(self):
            # Test with missing required fields
            form_data = {}
            form = MaterialForm(data=form_data)
            self.assertFalse(form.is_valid())
            self.assertEqual(len(form.errors), 2)  # Number of required fields

    def test_add_sample_form_valid_data(self):
        form_data = {
            'laser_source': self.laser_source.pk,
            'material': self.material.pk,
            'scanning_speed': 100,
            'average_power': '50.0',
            'authors': 'Test Author',
            'research_date': '2023-08-01T12:00:00',
        }
        form = AddSampleForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_add_sample_form_invalid_data(self):
        form_data = {
            'laser_source': self.laser_source.pk,
            'material': self.material.pk,
            'scanning_speed': -100,
            'average_power': 'not_a_number',
            'authors': 'Test Author',
            'research_date': 'invalid_date',
        }
        form = AddSampleForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)

    def test_laser_source_form(self):
        form_data = {
            'name': 'Test Laser',
            'type_of_laser': 'Diode',
            'wavelength': 532,
        }
        form = LaserSourceForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_material_form(self):
        form_data = {
            'name': 'Test Material',
            'description': 'This is a test material.',
        }
        form = MaterialForm(data=form_data)
        self.assertTrue(form.is_valid())

    # Add more tests for other forms...

    def test_laser_marking_parameters_form(self):
        form_data = {
            'laser_source': self.laser_source.pk,
            'material': self.material.pk,
            'scanning_speed': 100,
            'average_power': '50.0',
            'authors': 'Test Author',
            'research_date': '2023-08-01T12:00:00',
        }
        form = LaserMarkingParametersForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_gae_params_form_valid_data(self):
        form_data = {
            'hex_color': '#FF0000',
        }
        form = GaeParamsForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_gae_params_form_invalid_data(self):
        form_data = {
            'hex_color': 'invalid_color',
        }
        form = GaeParamsForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_laser_source_form_valid_data(self):
        form_data = {
            'name': 'Test Laser',
            'type_of_laser': 'Diode',
            'wavelength': 532,
        }
        form = LaserSourceForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_laser_source_form_invalid_data(self):
        form_data = {
            'name': 'Test Laser',
            'type_of_laser': 'Diode',
            'wavelength': -532,
        }
        form = LaserSourceForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_material_form_valid_data(self):
        form_data = {
            'name': 'Test Material',
            'description': 'This is a test material.',
        }
        form = MaterialForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_material_form_invalid_data(self):
        form_data = {
            'name': '',
            'description': 'This is a test material.',
        }
        form = MaterialForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)


class PagesViewsTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )

        self.material = Material.objects.create(
            name='Test Material', description='This is a test material.'
        )
        self.laser_source = LaserSource.objects.create(
            name='Test Laser', type_of_laser='Diode', wavelength=532
        )
        self.marking_params = LaserMarkingParameters.objects.create(
            laser_source=self.laser_source, material=self.material,
            scanning_speed=100, average_power=10.5,
            authors='Test Author', research_date='2023-08-29 12:00:00'
        )

    # Test forms
    def test_gae_params_form(self):
        form_data = {'hex_color': '#FF0000'}
        form = GaeParamsForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_laser_source_form(self):
        form_data = {
            'name': 'New Laser', 'type_of_laser': 'Gas', 'wavelength': 1064
        }
        form = LaserSourceForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_material_form(self):
        form_data = {'name': 'New Material', 'description': 'A new material.'}
        form = MaterialForm(data=form_data)
        self.assertTrue(form.is_valid())

    # Test views
    def test_home_view(self):
        response = self.client.get(reverse('pages:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laser_color_marking_db/views/home.html')

    def test_about_view(self):
        response = self.client.get(reverse('pages:about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laser_color_marking_db/views/about.html')

    def test_contact_view(self):
        response = self.client.get(reverse('pages:contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laser_color_marking_db/views/contact.html')

    def test_material_list_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('pages:material_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laser_color_marking_db/materials/material_list.html')

    def test_add_sample_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('pages:add_sample'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laser_color_marking_db/laser_markin_parameters/add_sample.html')

    # Add more view tests here...




from django.test import TestCase
from .utils import hex_to_rgb, rgb_to_hex, ColorSpectrum, get_value, parse_data_string

class UtilsTests(TestCase):

    def test_hex_to_rgb(self):
        hex_color = "#FF9900"
        rgb_values = hex_to_rgb(hex_color)
        self.assertEqual(rgb_values, (255, 153, 0))

    def test_rgb_to_hex(self):
        red = 255
        green = 153
        blue = 0
        hex_color = rgb_to_hex(red, green, blue)
        self.assertEqual(hex_color, "#FF9900")


    def test_get_value(self):
        int_value = get_value("42")
        float_value = get_value("3.14")
        string_value = get_value("hello")
        dash_value = get_value("-")
        self.assertEqual(int_value, 42)
        self.assertEqual(float_value, 3.14)
        self.assertEqual(string_value, "hello")
        self.assertIsNone(dash_value)

