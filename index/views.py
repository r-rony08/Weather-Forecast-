from django.shortcuts import render
import requests
import datetime

# Create your views here.
def index(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'comilla'
    appid = '427349b76be8c2bf0f428e4b2be79372'
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    PARMS = {'q':'city', 'appid': appid, 'units': 'metrics'}

    r = requests.get(url=URL, params=PARMS)
    res = r.json()
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    day = datetime.date.today()
    return render(request, 'weatherapp/index.html', {'description': description, 'icon': icon, 'temp': temp, 'day': day, 'city': city})