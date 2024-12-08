# Generated by Django 5.1.3 on 2024-12-08 22:08

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lms", "0002_alter_lesson_course"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
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
                    "payment_date",
                    models.DateField(
                        default=datetime.datetime.now, verbose_name="Дата оплаты"
                    ),
                ),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2, max_digits=20, verbose_name="Сумма"
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("BANK_TRANSFER", "Банковский перевод"),
                            ("CASH", "Наличными"),
                        ],
                        max_length=50,
                        verbose_name="Способ оплаты",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
                (
                    "paid_course",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="lms.course",
                        verbose_name="Оплаченный курс",
                    ),
                ),
                (
                    "paid_lesson",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="lms.lesson",
                        verbose_name="Оплаченный урок",
                    ),
                ),
            ],
        ),
    ]
