from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Restaurant


class RestaurantList(ListView):
    model = Restaurant
    ordering = "-pk"


class RestaurantDetail(DetailView):
    model = Restaurant


restaurant_list = RestaurantList.as_view()
restaurant_detail = RestaurantDetail.as_view()
