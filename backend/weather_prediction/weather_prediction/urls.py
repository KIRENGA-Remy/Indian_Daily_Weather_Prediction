from django.contrib import admin
from django.urls import path, include

print("Root URLs loaded")  # Confirm this file is loaded

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('weather_app.urls')),
]

print("Root URL patterns:", urlpatterns)  # Show the registered patterns