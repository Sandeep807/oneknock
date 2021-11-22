from django.urls import path
from .views import *
urlpatterns = [
    path('service/',ServiceView.as_view()),
    path('sub_service/',ServiceSubCategoryView.as_view()),
    path('bookingservice/',BookingServiceView.as_view()),
]
