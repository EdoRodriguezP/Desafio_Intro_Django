from django.urls import path, include  # Import include to include URLs from other apps
from .views import home, about, contact  # Import views from the current app


urlpatterns = [
    path('', home, name='home'),  # Define a URL pattern for the home view
    path('about/', about, name='about'),  # Define a URL pattern for the
    path('contact/', contact, name='contact'),  # Define a URL pattern for the contact view]
]