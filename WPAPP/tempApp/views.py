from django.shortcuts import render
import requests

# Create your views here.

def tempApp(request):
    # city = "Bidar"
    city = request.GET.get("city")
    apikey = "f75613bba4664f4eaaa8acf36bfc600b"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"
    response = requests.get(url)
    resp = response.json()

   

    payload = {
        "city": resp['name'],        
        "weather": resp['weather'][0]['main'],
        "kelvin": (int(resp["main"]["temp"])),
        "celcius": (int(resp["main"]["temp"])) - 273,
        "weatherIcon": resp["weather"][0]['icon']
    }

    context = { "resp": payload}

    return render(request, "index.html", context)