
from django.urls import path
from .views import home
 
from .views.signup import Signup  # Import Signup Class 
from .views.login import Login  # Import Signup Class 

urlpatterns = [
  path('', home.index, name='homepage'),
  path('singup', Signup.as_view(), name='singup'),
  path('login', Login.as_view(), name='login'),
]
