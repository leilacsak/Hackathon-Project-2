from datetime import date

from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect

from .forms import BookingForm
from .models import Booking


def home(request):
    context = {
        "today": date.today(),
        "upcoming_count": Booking.objects.filter(date__gte=date.today()).count(),
    }
    return render(request, "core/home.html", context)


def courts(request):
    courts_data = [
        {"number": 1, "surface": "Hard", "indoors": False},
        {"number": 2, "surface": "Hard", "indoors": False},
        {"number": 3, "surface": "Clay", "indoors": False},
        {"number": 4, "surface": "Grass", "indoors": True},
    ]
    return render(request, "core/courts.html", {"courts": courts_data})


def book_court(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking created successfully.")
            return redirect("my_bookings")
    else:
        form = BookingForm()

    return render(request, "core/book_court.html", {"form": form})


def my_bookings(request):
    bookings = Booking.objects.order_by("date", "start_time")
    return render(request, "core/my_bookings.html", {"bookings": bookings})
