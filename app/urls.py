from django.urls import path
from . import views

urlpatterns = [
    path('',views.VideoProcessor.as_view(),name="video-processor"),
    path('features/',views.features,name="features"),
    path('reach-me/',views.contact,name="contact"),
]
