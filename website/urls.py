from django.urls import path
from . import views
app_name = "website"
urlpatterns = [
    path('home', views.home_page_view, name="home"),
    path('base', views.base_page_view, name="base"),
    path ('filho1', views.filho_page_view, name='filho')
]
