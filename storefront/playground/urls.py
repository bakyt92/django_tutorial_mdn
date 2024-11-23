from django.urls import path
from . import views

urlpatterns = [
	path('hello/', views.say_hello, name='hello_view'),
	path('hello1/', views.say_hello1, name='hello_view1'),
]