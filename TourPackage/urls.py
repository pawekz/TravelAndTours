from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('tour/<int:tour_id>/', views.tour_detail, name='tour_detail'),
    path('tour/<int:tour_id>/review/', views.review_submission, name='review_submission'),
]