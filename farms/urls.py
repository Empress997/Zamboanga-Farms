from django.urls import path
from . import views 

app_name = "farms"

urlpatterns = [
    path('',views.HomeView.as_view(), name="home"),
    path('categories/',views.categories,name="categories"),
    path('crop/<slug:slug>/',views.detail, name="crop-detail"),
    path('about/',views.about_us,name="about"),
    path('services/',views.services,name="services"),
]
