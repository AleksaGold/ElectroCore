from django.db import models

NULLABLE = {"blank": True, "null": True}


class Contact(models.Model):
    """Класс для описания модели Contact."""

    email = models.EmailField(verbose_name="Электронная почта (email)")
    country = models.CharField(max_length=150, verbose_name="Страна")
    city = models.CharField(max_length=150, verbose_name="Город")
    street = models.CharField(max_length=150, verbose_name="Улица")
    house_number = models.CharField(max_length=10, verbose_name="Номер дома")

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return f"{self.email} - {self.country}({self.city})"


class Product(models.Model):
    """Класс для описания модели Product."""

    name = models.CharField(max_length=150, verbose_name="Название продукта")
    model = models.CharField(max_length=50, verbose_name="Модель продукта")
    launch_date = models.DateField(
        auto_now=False, verbose_name="Дата выхода продукта на рынок"
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return f"{self.name} ({self.model})"


class Chain(models.Model):
    """Класс для описания модели Chain."""

    LEVELS = [
        (0, "Завод"),
        (1, "Розничная сеть"),
        (2, "Индивидуальный предприниматель"),
    ]

    name = models.CharField(max_length=150, verbose_name="Название звена сети")
    level = models.PositiveSmallIntegerField(
        choices=LEVELS, verbose_name="Уровень звена сети"
    )
    contact = models.ForeignKey(
        "chain.Contact",
        on_delete=models.SET_NULL,
        verbose_name="Контакты",
        related_name="chain_contact",
        **NULLABLE,
    )
    product = models.ManyToManyField(
        "chain.Product",
        verbose_name="Продукты",
        related_name="chain_product",
    )
    supplier = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        verbose_name="Поставщик",
        related_name="chain_supplier",
        **NULLABLE,
    )
    debt = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name="Задолженность перед поставщиком в денежном выражении",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    class Meta:
        verbose_name = "Звено сети"
        verbose_name_plural = "Звенья сети"

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return (
            f"{self.name} - уровень: {self.level}, задолженность: {self.debt}"
        )
