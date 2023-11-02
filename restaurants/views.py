from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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


class RestaurantCreate(LoginRequiredMixin, CreateView):
    model = Restaurant
    form_class = RestaurantForm
    success_url = reverse_lazy("restaurants")

    def form_valid(self, form):
        restaurant = form.save(commit=False)  # commit=False는 DB에 저장하지 않고 객체만 반환
        restaurant.author = self.request.user
        return super().form_valid(form)  # 이렇게 호출했을 때 저장


class RestaurantUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Restaurant
    form_class = RestaurantForm

    def test_func(self):
        return self.get_object().author == self.request.user

    def handle_no_permission(self):
        return redirect("restaurants")

    def get_success_url(self):
        return reverse_lazy("restaurant-detail", kwargs={"pk": self.object.pk})


class RestaurantDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Restaurant
    success_url = reverse_lazy("restaurants")

    def test_func(self):
        return self.get_object().author == self.request.user

    def handle_no_permission(self):
        return redirect("restaurants")


restaurant_list = RestaurantList.as_view()
restaurant_detail = RestaurantDetail.as_view()
restaurant_create = RestaurantCreate.as_view()
restaurant_update = RestaurantUpdate.as_view()
restaurant_delete = RestaurantDelete.as_view()
