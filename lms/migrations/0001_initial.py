# Generated by Django 5.1.3 on 2024-12-03 09:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="укажите название курса",
                        max_length=100,
                        verbose_name="название курса",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="опишите курс",
                        max_length=250,
                        null=True,
                        verbose_name="описание курса",
                    ),
                ),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите превью",
                        null=True,
                        upload_to="lms/previews",
                        verbose_name="превью",
                    ),
                ),
            ],
            options={
                "verbose_name": "Курс",
                "verbose_name_plural": "Курсы",
            },
        ),
        migrations.CreateModel(
            name="Lesson",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="укажите название урока",
                        max_length=100,
                        verbose_name="название урока",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="опишите урок",
                        max_length=250,
                        null=True,
                        verbose_name="описание урока",
                    ),
                ),
                (
                    "picture",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите картинку",
                        null=True,
                        upload_to="lms/pictures",
                        verbose_name="картинка",
                    ),
                ),
                (
                    "video_url",
                    models.URLField(
                        blank=True,
                        help_text="загрузите видео",
                        null=True,
                        verbose_name="ссылка на видео",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        help_text="выберите курс",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lms.course",
                        verbose_name="курс",
                    ),
                ),
            ],
            options={
                "verbose_name": "Урок",
                "verbose_name_plural": "Уроки",
            },
        ),
    ]
