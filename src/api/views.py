import requests
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

#
# class Function(APIView):
#
#     permission_classes = [AllowAny]
#     http_method_names = ['post', 'get']
#
#     def post(self, request):
#         city = request.POST.get('city')
#         print(city)
#         url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=5eb7704639bc82d83bda28371acacf0e&units=metric"
#
#         response = requests.get(url)
#         weather_data = response.json()
#         weather_data_context = []
#         if weather_data['cod'] != 200:
#             weather = weather_data
#         else:
#
#             # "".join(word[0].upper() + word[1:].lower() for word in city),
#             weather={
#                 "city": weather_data["name"],
#                 "description": weather_data["weather"][0]["description"],
#                 "feels_like": weather_data["main"]['feels_like'],
#                 "temp": weather_data["main"]['temp'],
#                 "temp_min": weather_data["main"]['temp_min'],
#                 "temp_max": weather_data["main"]['temp_max'],
#                 "cod": weather_data['cod']
#             }
#         weather_data_context.append(weather)
#         context = {"weather_data": weather_data_context}
#         return render(request, "index.html", context)


def Findweather(request):

    context = {}
    if request.method == "POST":
        city = request.POST.get('city')

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=5eb7704639bc82d83bda28371acacf0e&units=metric"

        response = requests.get(url)
        weather_data = response.json()

        weather_data_context = []
        if weather_data['cod'] != 200:
            weather = weather_data
        else:

            # "".join(word[0].upper() + word[1:].lower() for word in city),
            weather = {
                "city": weather_data["name"],
                "description": weather_data["weather"][0]["description"],
                "feels_like": weather_data["main"]['feels_like'],
                "temp": weather_data["main"]['temp'],
                "temp_min": weather_data["main"]['temp_min'],
                "temp_max": weather_data["main"]['temp_max'],
                "cod": weather_data['cod']
            }
        weather_data_context.append(weather)
        context = {"weather_data": weather_data_context}
    return render(request, "index.html", context)
