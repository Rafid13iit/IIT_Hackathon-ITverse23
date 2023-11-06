import requests
from django.shortcuts import render


def step1(request):
    city_list = None
    state = ''
    country = ''
    if request.method == 'POST':
        state = request.POST.get('state')
        country = request.POST.get('country')
        YOUR_API_KEY = 'c875f965-df7b-4d10-a957-14654b35a017'

        # Step 1: Retrieve the list of cities based on state and country
        city_list_url = f'http://api.airvisual.com/v2/cities?state={state}&country={country}&key={YOUR_API_KEY}'
        r = requests.get(url=city_list_url)
        city_list = r.json()
        # Remove leading/trailing spaces from 'state' and 'country'
    state = state.strip()
    country = country.strip()

    return render(request, 'step1.html', {'city_list': city_list, 'state' : state, 'country' : country})


def step2(request, state, country, selected_city):
    city_data = None

    YOUR_API_KEY = 'c875f965-df7b-4d10-a957-14654b35a017'

    # Step 2: Retrieve city-specific air quality data
    city_data_url = f'http://api.airvisual.com/v2/city?city={selected_city}&state={state}&country={country}&key={YOUR_API_KEY}'
    r = requests.get(url=city_data_url)
    city_data = r.json()

    return render(request, 'step2.html', {'city_data': city_data})
