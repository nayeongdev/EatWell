from django import forms
from restaurants.models import Restaurant, Comment, Tag


class RestaurantForm(forms.ModelForm):
    tags_input = forms.CharField(
        max_length=100, help_text="태그를 쉼표(,)로 구분하여 입력하세요.", label="태그"
    )

    class Meta:
        model = Restaurant
        fields = [
            "name",
            "address",
            "cuisine",
            "website",
            "description",
            "thumb_image",
            "tags_input",
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["message"]


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
