from django.urls import path

from detection import views

app_name = "detection"
urlpatterns = [
    path('',views.home,name='home'),

]