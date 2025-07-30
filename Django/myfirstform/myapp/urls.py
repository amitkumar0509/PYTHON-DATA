from django.urls import path
from .views import contact_view

urlpatterns = [
    path('', contact_view, name='home'),  # for home page
    path('contact/', contact_view, name='contact'),  # optional
]
