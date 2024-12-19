from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('all.urls')),  # `/api/` ni to'g'ri kiritganimizga ishonch hosil qiling
]