from django.shortcuts import render, redirect, get_object_or_404
import requests
from farms.forms import ContactForm
from .models import *
import json
from django.views import View
from datetime import datetime, timedelta
# Create your views here.

class HomeView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'store/index.html', {'form':form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['fname']
            email_address = form.cleaned_data['email_address']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            reg = Contact(fname=fname, email_address=email_address, subject=subject, message=message)
            reg.save()
        return redirect('alchemy:home')

def categories(request):
    crops = Crop.objects.all()
    crops_rainy = Crop.objects.filter(category=1)
    crops_dry = Crop.objects.filter(category=2)
    url = 'https://pro.openweathermap.org/data/2.5/forecast/climate?q=Zamboanga City&units=metric&cnt=30&appid=1047600834087dd796420df1c5149a42'
    city = 'Zamboanga City'
    total_dry = 0
    total_rain = 0
    city_weather_data = requests.get(url.format(city)).json()
    city_weather = json.dumps(city_weather_data)
    
    count_sky = city_weather.count('clear sky')
    count_few_clouds = city_weather.count('few clouds')
    count_scattered_clouds = city_weather.count('scattered clouds')
    count_broken_clouds = city_weather.count('broken clouds')
    count_light_rain = city_weather.count('light rain')
    count_moderate_rain = city_weather.count('moderate rain')
    count_shower_rain = city_weather.count('shower rain')
    count_heavy_intensity_rain = city_weather.count('heavy intensity rain')
    count_very_heavy_rain = city_weather.count('very heavy rain')
 
    total_dry = count_sky + count_few_clouds + count_scattered_clouds + count_broken_clouds
    total_rain = count_light_rain + count_moderate_rain + count_shower_rain + count_heavy_intensity_rain + count_very_heavy_rain
    context = {
        'crops':crops,
        'crops_dry':crops_dry,
        'crops_rainy':crops_rainy,
        'total_dry':total_dry,
        'total_rain':total_rain,
    }
    return render(request, 'store/categories.html',context)

def detail(request,slug):
    crop = get_object_or_404(Crop, slug=slug)
    url = 'https://pro.openweathermap.org/data/2.5/forecast/climate?q=Zamboanga City&units=metric&cnt=30&appid=1047600834087dd796420df1c5149a42'
    city = 'Zamboanga City'
    total_dry = 0
    total_rain = 0
    city_weather_data = requests.get(url.format(city)).json()
    city_weather = json.dumps(city_weather_data)
    
    count_sky = city_weather.count('clear sky')
    count_few_clouds = city_weather.count('few clouds')
    count_scattered_clouds = city_weather.count('scattered clouds')
    count_broken_clouds = city_weather.count('broken clouds')
    count_light_rain = city_weather.count('light rain')
    count_moderate_rain = city_weather.count('moderate rain')
    count_shower_rain = city_weather.count('shower rain')
    count_heavy_intensity_rain = city_weather.count('heavy intensity rain')
    count_very_heavy_rain = city_weather.count('very heavy rain')
 
    total_dry = count_sky + count_few_clouds + count_scattered_clouds + count_broken_clouds
    total_rain = count_light_rain + count_moderate_rain + count_shower_rain + count_heavy_intensity_rain + count_very_heavy_rain
    print(f'{total_dry=}')
    print(f'{total_rain=}')

    context = {
        'crop':crop,
        'total_dry':total_dry,
        'total_rain':total_rain,
        "city":city,
        "temperature":city_weather_data['list'][0]['temp']['day'],
        "description":city_weather_data['list'][0]['weather'][0]['description'],
        "icon":city_weather_data['list'][0]['weather'][0]['icon'],
    }
    return render(request, 'store/detail.html',context)

def about_us(request):
    return render(request, 'store/about.html')

def services(request):
    url = 'https://pro.openweathermap.org/data/2.5/forecast/climate?q=Zamboanga City&units=metric&cnt=30&appid=1047600834087dd796420df1c5149a42'
    city = 'Zamboanga City'
    city_weather = requests.get(url.format(city)).json()
    day_1 = datetime.now().date()
    day_2 = datetime.now() + timedelta(days=1)
    day_3 = datetime.now() + timedelta(days=2)
    day_4 = datetime.now() + timedelta(days=3)
    day_5 = datetime.now() + timedelta(days=4)
    day_6 = datetime.now() + timedelta(days=5)
    day_7 = datetime.now() + timedelta(days=6)
    day_8 = datetime.now() + timedelta(days=7)
    day_9 = datetime.now() + timedelta(days=8)
    format_date_1 = day_1.strftime("%a, %b-%d")
    format_date_2 = day_2.strftime("%a, %b-%d")
    format_date_3 = day_3.strftime("%a, %b-%d")
    format_date_4 = day_4.strftime("%a, %b-%d")
    format_date_5 = day_5.strftime("%a, %b-%d")
    format_date_6 = day_6.strftime("%a, %b-%d")
    format_date_7 = day_7.strftime("%a, %b-%d")
    format_date_8 = day_8.strftime("%a, %b-%d")
    format_date_9 = day_9.strftime("%a, %b-%d")

    data = {
        "city":city,
        "format_date_1":format_date_1,
        "temperature":city_weather['list'][0]['temp']['max'],
        "description":city_weather['list'][0]['weather'][0]['description'],
        "speed":city_weather['list'][0]['speed'],
        "rainfall":city_weather['list'][0]['rain'],
        "cloud":city_weather['list'][0]['clouds'],

        "format_date_2":format_date_2,
        "temperature_2":city_weather['list'][1]['temp']['max'],
        "description_2":city_weather['list'][1]['weather'][0]['description'],
        "speed_2":city_weather['list'][1]['speed'],
        "rainfall_2":city_weather['list'][1]['rain'],
        "cloud_2":city_weather['list'][1]['clouds'],

        "format_date_3":format_date_3,
        "temperature_3":city_weather['list'][2]['temp']['max'],
        "description_3":city_weather['list'][2]['weather'][0]['description'],
        "speed_3":city_weather['list'][2]['speed'],
        "rainfall_3":city_weather['list'][2]['rain'],
        "cloud_3":city_weather['list'][2]['clouds'],

        "format_date_4":format_date_4,
        "temperature_4":city_weather['list'][3]['temp']['max'],
        "description_4":city_weather['list'][3]['weather'][0]['description'],
        "speed_4":city_weather['list'][3]['speed'],
        "rainfall_4":city_weather['list'][3]['rain'],
        "cloud_4":city_weather['list'][3]['clouds'],

        "format_date_5":format_date_5,
        "temperature_5":city_weather['list'][4]['temp']['max'],
        "description_5":city_weather['list'][4]['weather'][0]['description'],
        "speed_5":city_weather['list'][4]['speed'],
        "rainfall_5":city_weather['list'][4]['rain'],
        "cloud_5":city_weather['list'][4]['clouds'],

        "format_date_6":format_date_6,
        "temperature_6":city_weather['list'][5]['temp']['max'],
        "description_6":city_weather['list'][5]['weather'][0]['description'],
        "speed_6":city_weather['list'][5]['speed'],
        "rainfall_6":city_weather['list'][5]['rain'],
        "cloud_6":city_weather['list'][5]['clouds'],

        "format_date_7":format_date_7,
        "temperature_7":city_weather['list'][6]['temp']['max'],
        "description_7":city_weather['list'][6]['weather'][0]['description'],
        "speed_7":city_weather['list'][6]['speed'],
        "rainfall_7":city_weather['list'][6]['rain'],
        "cloud_7":city_weather['list'][6]['clouds'],

        "format_date_8":format_date_8,
        "temperature_8":city_weather['list'][7]['temp']['max'],
        "description_8":city_weather['list'][7]['weather'][0]['description'],
        "speed_8":city_weather['list'][7]['speed'],
        "rainfall_8":city_weather['list'][7]['rain'],
        "cloud_8":city_weather['list'][7]['clouds'],
    }
    return render(request, 'store/services.html', data)
