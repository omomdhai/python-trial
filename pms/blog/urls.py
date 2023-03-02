from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('aboutus/',views.aboutus),
    path('contactus/',views.contactus),
    path('etc1/',views.Etc1),
    path('etc2/',views.Etc2),
    path('etc3/',views.Etc3),

]