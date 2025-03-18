from django.contrib import admin
from django.urls import path
from myapp.views import htop_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('htop/', htop_view),
    path('', htop_view),  # This makes the root URL (/) show the same as /htop
]
