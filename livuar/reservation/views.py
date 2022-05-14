from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import FormView
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import ReservationForm


def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('reservation')
            except:
                form.add_error(None, 'Error with add reservation')
    else:
        form = ReservationForm()

    return render(request, 'reservation/reservation.html', {'form': form})