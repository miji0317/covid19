from django.contrib import admin
from django.urls import path, include
from chart import views as chart_views

urlpatterns = [
    path('', include('chart.urls')),
    path('chart/', include('chart.urls')),
    path('admin/', admin.site.urls),
]