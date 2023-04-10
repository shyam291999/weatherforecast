
from django.urls import path
from . import views


urlpatterns = [
   # path("", views.Function.as_view()),
   path("", views.Findweather),

]
