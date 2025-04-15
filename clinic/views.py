from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Medicine, Doctor, Appointment, VirtualAssistance
import re
from django.contrib import messages

# Appointment Booking View
def appointment_booking(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if re.match(r'.+@(gmail\.com|woxsen\.edu\.in)$', email):
            doctor_id = request.POST.get('doctor')
            date = request.POST.get('date')
            time = request.POST.get('time')
            doctor = Doctor.objects.get(id=doctor_id)
            Appointment.objects.create(email=email, date=date, time=time, doctor=doctor)
            return JsonResponse({'status': 'success', 'message': 'Appointment booked'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid email domain'})
    doctors = Doctor.objects.all()
    return render(request, 'booking.html', {'doctors': doctors})

# Medicine Stock Availability View with Google Maps
def medicine_stock(request):
    medicines = Medicine.objects.all()
    return render(request, 'stock.html', {'medicines': medicines})

# Doctor Availability View
def doctor_availability(request):
    doctors = Doctor.objects.filter(available_today=True)
    return render(request, 'availability.html', {'doctors': doctors})

# Emergency Video Chat
def emergency(request):
    return render(request, 'video_chat.html')

# Virtual Assistance View
def virtual_assistance(request):
    if request.method == 'POST':
        problem = request.POST.get('problem')
        advice = VirtualAssistance.objects.filter(problem__icontains=problem).first()
        if advice:
            return JsonResponse({'advice': advice.first_aid})
        else:
            return JsonResponse({'advice': 'Please visit the clinic for better assistance.'})
    return render(request, 'assisstance.html')

def book_appointment(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        date = request.POST.get('date')
        time = request.POST.get('time')
        doctor_id = request.POST.get('doctor')

        if not email.endswith('@woxsen.edu.in'):
            messages.error(request, 'Only Woxsen email addresses are allowed.')
            return redirect('appointment')  # Redirect back to form page

        # Save appointment logic here (you can save in database)

        # After saving, redirect to assistance page
        return redirect('assistance')  # Name your URL correctly in urls.py
def book_appointment(request):
    doctors = Doctor.objects.all()
    return render(request, 'clinic/appointment.html', {'doctors': doctors})

