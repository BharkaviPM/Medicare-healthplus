from django.urls import path
from . import views

urlpatterns = [
    path('appointment_booking/', views.book_appointment, name='appointment_booking'),
    path('medicine/', views.medicine_stock, name='medicine_stock'),
    path('doctors/', views.doctor_availability, name='doctor_availability'),
    path('emergency/', views.emergency, name='emergency'),
    path('assistance/', views.virtual_assistance, name='virtual_assistance'),
]
