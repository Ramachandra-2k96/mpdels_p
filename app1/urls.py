from django.urls import path
from app1.views import home,certificate
urlpatterns = [
	path('',home),
	path('certificate',certificate),
]