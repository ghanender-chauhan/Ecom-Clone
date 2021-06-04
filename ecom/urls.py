
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static 
from .import views
# from django import views   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('amazon/', include('amazon.urls')),
    path("about/", views.about , name = "about"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)