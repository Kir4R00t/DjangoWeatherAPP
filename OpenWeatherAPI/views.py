from django.shortcuts import render
from .forms import CityForm
from .utils import get_weather_data  # Import your get_weather_data function

def weather(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['city']
            weather_data = get_weather_data(city_name)  # Pass the city name as an argument
            if weather_data:
                context = {
                    'form': form,
                    'city_name': city_name,
                    'temperature': weather_data['temperature'],
                    'humidity': weather_data['humidity'],
                    'wind_speed': weather_data['wind_speed'],
                }
                return render(request, 'index.html', context)
            else:
                error_message = 'Error: Unable to fetch weather data. Please make sure the city name is correct.'
                return render(request, 'index.html', {'form': form, 'error_message': error_message})
    else:
        form = CityForm()
        return render(request, 'index.html', {'form': form})
