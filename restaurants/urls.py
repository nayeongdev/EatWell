from django.urls import path
from restaurants import views

urlpatterns = [
    path("", views.restaurant_list, name="restaurants"),
    path("<int:pk>/", views.restaurant_detail, name="restaurant_detail"),
    path("recommend/", views.restaurant_create, name="recommend"),
    path("<int:pk>/edit/", views.restaurant_update, name="restaurant_edit"),
    path("<int:pk>/delete/", views.restaurant_delete, name="restaurant_delete"),
    path('<int:pk>/comment/new/', views.comment_new, name='comment_new'),
]
