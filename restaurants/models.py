from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
    KOREAN = "한식"
    WESTERN = "양식"
    JAPANESE = "일식"
    CHINESE = "중식"
    ASIAN = "아시안음식"
    SNACKS = "분식"
    CAFE = "카페"
    FAST_FOOD = "패스트푸드"
    OTHER = "기타"

    CUISINE_CHOICES = [
        (KOREAN, "한식"),
        (WESTERN, "양식"),
        (JAPANESE, "일식"),
        (CHINESE, "중식"),
        (ASIAN, "아시안음식"),
        (SNACKS, "분식"),
        (CAFE, "카페"),
        (FAST_FOOD, "패스트푸드"),
        (OTHER, "기타"),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, help_text="식당 이름을 입력하세요.")
    address = models.CharField(max_length=100, help_text="식당은 어디에 있나요?")
    cuisine = models.CharField(
        max_length=10, choices=CUISINE_CHOICES, help_text="어떤 종류의 음식인가요?"
    )
    website = models.URLField(
        max_length=200,
        blank=True,
        null=True,
        help_text="(선택) 식당과 관련 있는 웹사이트 주소를 입력하세요.",
    )
    description = models.TextField(help_text="식당을 추천하는 이유를 작성해 주세요.")
    thumb_image = models.ImageField(
        upload_to="restaurants/images/%Y/%m/%d/",
        blank=True,
        help_text="(선택) 썸네일 이미지를 넣어보세요.",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    view_count = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField("Tag", blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/restaurants/{self.pk}/"


class Comment(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["created_at"])]

    def __str__(self):
        return f'"{self.restaurant}"에서 {self.author}님의 댓글'


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
