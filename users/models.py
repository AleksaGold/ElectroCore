from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    """Модель User для хранения информации о пользователях веб-приложения."""

    username = None
    email = models.EmailField(
        unique=True, verbose_name="Электронная почта пользователя (email)"
    )
    phone_number = PhoneNumberField(verbose_name="Номер телефона", **NULLABLE)
    country = models.CharField(max_length=150, verbose_name="Страна", **NULLABLE)
    city = models.CharField(max_length=150, verbose_name="Город", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return f"{self.email} - {self.country}({self.city})"
