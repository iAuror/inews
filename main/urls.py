from django.urls import path

from main.views import  Layout

urlpatterns = [
    path ('', Layout.as_view(),name='index')
]