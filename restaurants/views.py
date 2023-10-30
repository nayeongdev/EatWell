from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Restaurant
from .forms import RestaurantForm


class RestaurantList(ListView):
    model = Restaurant
    ordering = "-pk"

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get("q", "")
        cuisine = self.request.GET.get("cuisine", "")
        if q:
            qs = qs.filter(name__icontains=q)
        if cuisine:
            qs = qs.filter(cuisine=cuisine)
        return qs


class RestaurantDetail(DetailView):
    model = Restaurant


class RestaurantCreate(CreateView):
    model = Restaurant
    form_class = RestaurantForm
    success_url = reverse_lazy("restaurants")


class RestaurantUpdate(UpdateView):
    model = Restaurant
    form_class = RestaurantForm

    def get_success_url(self):
        return reverse_lazy("restaurant-detail", kwargs={"pk": self.object.pk})


class RestaurantDelete(DeleteView):
    model = Restaurant
    success_url = reverse_lazy("restaurants")


restaurant_list = RestaurantList.as_view()
restaurant_detail = RestaurantDetail.as_view()
restaurant_create = RestaurantCreate.as_view()
restaurant_update = RestaurantUpdate.as_view()
restaurant_delete = RestaurantDelete.as_view()
