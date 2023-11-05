from django import forms
from restaurants.models import Restaurant, Comment, Tag


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = [
            "name",
            "address",
            "cuisine",
            "website",
            "description",
            "thumb_image",
            "tags",
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["message"]


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
