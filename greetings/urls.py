from django.urls import path
from greetings.views import helloWorld, helloWorldName

urlpatterns = [
    path('', helloWorld),
    path('<name>', helloWorldName),
]