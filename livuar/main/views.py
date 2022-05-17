from django.shortcuts import render, redirect

# Create your views here.
from rest_framework.views import APIView

from news.models import News
from reservation.forms import ReservationForm


def home(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('home')
            except:
                form.add_error(None, 'Error with add reservation')
    else:
        form = ReservationForm()
        
    news = News.objects.all()

    return render(request, 'main/index.html', {'news_list': news, 'form': form})