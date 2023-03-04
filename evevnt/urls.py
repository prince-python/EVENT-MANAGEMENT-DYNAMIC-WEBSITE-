from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from .import views


urlpatterns = [
    path('photos/',views.index,name="photos")

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
