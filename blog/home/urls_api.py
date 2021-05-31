from django.urls import path #added
from .views_api import *


urlpatterns = [ 
    path('login/', LoginView),
    path('register/', RegisterView)

]