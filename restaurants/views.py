from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ObjectDoesNotExist

from .models import Restaurant, Tag, Comment
from .forms import RestaurantForm, CommentForm


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context
    
    def get_object(self, queryset=None):
        pk = self.kwargs.get("pk")
        restaurant = Restaurant.objects.get(pk=pk)
        restaurant.view_count += 1
        restaurant.save()
        return super().get_object(queryset)


class RestaurantCreate(LoginRequiredMixin, CreateView):
    model = Restaurant
    form_class = RestaurantForm
    success_url = reverse_lazy("restaurants")

    def form_valid(self, form):
        tags_input = form.cleaned_data["tags_input"]
        tags_list = [tag.strip() for tag in tags_input.split(",") if tag.strip()]

        restaurant = form.save(commit=False)  # commit=False는 DB에 저장하지 않고 객체만 반환
        restaurant.author = self.request.user
        restaurant.save()

        for tag_name in tags_list:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            restaurant.tags.add(tag)

        return super().form_valid(form)  # 이렇게 호출했을 때 저장


class RestaurantUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Restaurant
    form_class = RestaurantForm

    def test_func(self):
        return self.get_object().author == self.request.user

    def handle_no_permission(self):
        return redirect("restaurants")

    def get_initial(self):
        # 이전에 저장된 값을 불러와서 초기 데이터로 설정
        initial = super().get_initial()
        restaurant = self.get_object()
        tag_names = ", ".join([tag.name for tag in restaurant.tags.all()])
        initial["tags_input"] = tag_names
        return initial

    def form_valid(self, form):
        tags_input = form.cleaned_data["tags_input"]
        tags_list = [tag.strip() for tag in tags_input.split(",") if tag.strip()]

        restaurant = form.save(commit=False)

        if "thumb_image" in self.request.FILES:
            restaurant.thumb_image = self.request.FILES["thumb_image"]

        restaurant.save()

        restaurant.tags.clear()
        for tag_name in tags_list:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            restaurant.tags.add(tag)

        return super().form_valid(form)  # 이렇게 호출했을 때 저장

    def get_success_url(self):
        return reverse_lazy("restaurant_detail", kwargs={"pk": self.object.pk})


class RestaurantDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Restaurant
    success_url = reverse_lazy("restaurants")

    def test_func(self):
        return self.get_object().author == self.request.user

    def handle_no_permission(self):
        return redirect("restaurants")


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.restaurant_id = self.kwargs['pk']
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("restaurant_detail", kwargs={"pk": self.kwargs['pk']})

def tag_page(request, slug=None):
    try:
        if not slug:
            tag = '해시태그가 달린 맛집'
            restaurant_list = Restaurant.objects.exclude(tags=None)
        else:
            tag = Tag.objects.get(slug=slug)
            restaurant_list = Restaurant.objects.filter(tags=tag)
    except ObjectDoesNotExist:
        return redirect("tags")

    return render(
        request,
        "restaurants/restaurant_list.html",
        {
            "restaurant_list": restaurant_list,
            "tag": tag,
        },
    )
