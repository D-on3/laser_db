"""
URL configuration for laser_db project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... Other URL patterns for your apps

    # Include the Django admin site URL
    path('admin/', admin.site.urls),

    # Include the URLs for your apps
    path('', include('laser_color_marking_db.urls',
                     namespace='laser_color_marking_db')),
    path('api/', include(('laser_cm_api.urls', 'laser_cm_api'),
                         namespace='laser_cm_api')),
    path('acc/', include('accounts.urls', namespace='accounts')),
    path('laser_optimization/', include('laser_cm_optimisation.urls',namespace="laser_optimisation")),

]

# Serve static files and media files only during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
