# laser_db

Certainly, let's go through the explanation and break down how each step was implemented:

### 1. Create a Virtual Environment and Install Django:

In this step, a virtual environment was created to isolate the project's dependencies from other projects. The following commands were executed in the terminal:

```bash
mkdir laser_color_marking_app
cd laser_color_marking_app
python -m venv venv
source venv/bin/activate
pip install django
```

Here's what each command does:

- `mkdir laser_color_marking_app`: This creates a new directory named "laser_color_marking_app" to contain your project.

- `cd laser_color_marking_app`: This moves into the newly created directory.

- `python -m venv venv`: This creates a virtual environment named "venv" within your project directory.

- `source venv/bin/activate`: This activates the virtual environment. You'll notice that your terminal prompt changes to indicate that you are now operating within the virtual environment.

- `pip install django`: This installs Django within the virtual environment.

### 2. Create the Django Project:

The following command creates the initial project structure:

```bash
django-admin startproject color_marking_project .
```

This command generates the necessary files and directories for a Django project named "color_marking_project." The trailing dot (`.`) specifies that the project files should be created in the current directory.

### 3. Create a New App:

To create a modular component within the project, the following command was used:

```bash
python manage.py startapp color_marking_app
```

Running this command generates an app named "color_marking_app," which will include files and directories for managing specific functionalities within the project.

### 4. Configure Settings:

The `settings.py` file was modified to configure various aspects of the project, including installed apps, database settings, debug mode, and allowed hosts. Changes were made based on your project's requirements:

- `INSTALLED_APPS`: This list contains the names of the apps that are integrated into your project. These apps provide specific functionalities to your application.

- `DATABASES`: This dictionary configures the database connection settings. In your case, a MySQL database is configured with the necessary connection details.

- `DEBUG`: This setting determines whether your project is in debug mode, which provides detailed error messages during development.

- `ALLOWED_HOSTS`: This list specifies the domain names or IP addresses from which your Django site can be accessed. Only requests from these hosts are allowed.

### 5. Run Migrations:

Running the initial migrations creates the necessary database tables based on the defined models. The following command was executed:

```bash
python manage.py migrate
```

This command applies the initial migrations to create the required database tables and relationships.

### 6. Create a Superuser:

A superuser account was created to access the Django admin panel:

```bash
python manage.py createsuperuser
```

This command prompts you to enter a username, email, and password for the superuser account, which is used to manage the admin panel and its functionalities.

### 7. Run the Development Server:

Starting the development server allows you to view and interact with your project:

```bash
python manage.py runserver
```

This command initiates the development server, and you can access your project through a web browser by navigating to the provided URL (usually `http://127.0.0.1:8000/`).

By following these steps, you've successfully set up a Django project from scratch, configured essential settings, and initiated the development server to start building and testing your application. The `settings.py` file, as explained in the earlier section, is a crucial part of this process, enabling you to tailor your project's behavior and functionalities according to your project's needs.




``` mermaid
classDiagram
    class Material {
        +name: String
        +description: String

    }

    class LaserSource {
        +name: String
        +type_of_laser: String
        +wavelength: Integer

    }

    class LaserMarkingParameters {
        +scanning_speed: Integer
        +average_power: Decimal
        +scan_step: Float
        +pulse_duration: Float
        +pulse_repetition_rate: Integer
        +overlap_coefficient: Float
        +volumetric_density_of_energy: Float
        +color_red: Integer
        +color_green: Integer
        +color_blue: Integer
        +author: String
        +date_published: DateTime
        +research_date: DateTime

        +material: Material
        +laser_source: LaserSource
    }

    Material --> LaserMarkingParameters : has
    LaserSource --> LaserMarkingParameters : has
```


# Accounts App Documentation

The **Accounts** app in this Django project handles user authentication, registration, and profile management. This documentation provides an in-depth overview of the app's components, including models, views, URLs, forms, and templates.

## Table of Contents

1. [Models](#models)
2. [Views](#views)
3. [URLs](#urls)
4. [Forms](#forms)
5. [Templates](#templates)

## Models

### Activation

The `Activation` model represents user activation records, which are used during the account activation process.

Fields:
- `user`: ForeignKey to the built-in `User` model.
- `created_at`: DateTimeField recording the creation timestamp.
- `code`: CharField to store a unique activation code.
- `email`: EmailField to store an associated email address.
- `image`: ImageField to store an image related to the activation.
- `token`: CharField to store a token (optional).

## Views

### LogInView

View for user login. Handles different methods of login based on settings.

### SignUpView

View for user sign up. Creates new user accounts with optional activation.

... (Document other views)

## URLs

### log-in/

URL for user login using different methods (username, email, or both).

### sign-up/

URL for user sign up.

... (Document other URLs)

## Forms

### SignIn

Form for user login, including password.

### SignUpForm

Form for user registration, including username, email, and password.

... (Document other forms)

## Templates

### login.html

Template for user login page. Displays login form and related links.

### logout.html

Template for displaying a message after user logout. Provides a link to log in again.

... (Document other templates)



add air_assist
add search specific color 
add filter by machine 
add filter by material
