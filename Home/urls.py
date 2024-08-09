
from django.urls import include, path
from .import views

urlpatterns = [
    path('', views.index,name='home'),
    path('about/', views.about, name='about'),
    #path('dept/', views.base, name='dept'),
    path('dept/', views.base, name='dept'),
    path('basecall/',views.basecall, name='basecall'),
    path('doctor',views.doctor, name='doctor'),
    path('booking',views.booking,),
    #path('gallery/', views.imagegallery, name='gallery'),
]