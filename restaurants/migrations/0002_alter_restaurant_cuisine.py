# Generated by Django 4.2.6 on 2023-10-27 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='cuisine',
            field=models.CharField(choices=[('한식', '한식'), ('양식', '양식'), ('일식', '일식'), ('중식', '중식'), ('아시안음식', '아시안음식'), ('분식', '분식'), ('카페', '카페'), ('패스트푸드', '패스트푸드'), ('기타', '기타')], help_text='어떤 종류의 음식인가요?', max_length=10),
        ),
    ]
