from django.urls import path
from restaurants import views

urlpatterns = [
    path("", views.restaurant_list, name="restaurants"),
    path("<int:pk>/", views.restaurant_detail, name="restaurant-detail"),
]
