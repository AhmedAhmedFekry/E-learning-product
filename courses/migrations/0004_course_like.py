# Generated by Django 3.2 on 2021-06-28 08:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0003_course_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='courses_liked', to=settings.AUTH_USER_MODEL),
        ),
    ]