from django.urls import path
from restaurants import views

urlpatterns = [
    path("", views.RestaurantList.as_view(), name="restaurants"),
    path("<int:pk>/", views.RestaurantDetail.as_view(), name="restaurant_detail"),
    path("tag/", views.tag_page, name='tags'),
    path("tag/<str:slug>/", views.tag_page, name='tag'),
    path("recommend/", views.RestaurantCreate.as_view(), name="recommend"),
    path("<int:pk>/edit/", views.RestaurantUpdate.as_view(), name="restaurant_edit"),
    path(
        "<int:pk>/delete/", views.RestaurantDelete.as_view(), name="restaurant_delete"
    ),
    path(
        "<int:pk>/comment/new/", views.CommentCreateView.as_view(), name="comment_new"
    ),
]
