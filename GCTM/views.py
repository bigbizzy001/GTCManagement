from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect

from .forms import HotelForm, FlightForm, ContactForm, VisaForm
# Create your views here


def home(request):
    template = 'gctm/home.html'
    context = {}
    return render(request, template, context)


def flight_deals(request):
    if request.method == 'POST':
        form = FlightForm(data=request.POST)
        if form.is_valid():
            form.save()
            # return  HttpResponseRedirect('Thanks')

    form = FlightForm()
    template = 'gctm/flights.html'
    context = {'form': form}
    return render(request, template, context)


def hotel_deals(request):
    if request.method == 'POST':
        form = HotelForm(data=request.POST)
        if form.is_valid():
            form.save()
            # return  HttpResponseRedirect('Thanks')

    form = HotelForm()
    template = 'gctm/hotels.html'
    context = {'form': form}
    return render(request, template, context)


def visa_works(request):
    if request.method == 'POST':
        form = VisaForm(data=request.POST)
        if form.is_valid():
            form.save()
            # return  HttpResponseRedirect('Thanks')

    form = VisaForm()
    template = 'gctm/visa.html'
    context = {'form': form}
    return render(request, template, context)


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            # return  HttpResponseRedirect('Thanks')

    form = ContactForm()
    template = 'gctm/contact_us.html'
    context = {'form': form}
    return render(request, template, context)

