from django.contrib import admin
from django.urls import reverse
from django.utils.html import mark_safe

from chain.models import Chain, Contact, Product


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Класс для настройки отображения модели "Contact" в административной панели."""

    list_display = (
        "pk",
        "email",
        "country",
        "city",
        "street",
        "house_number",
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Класс для настройки отображения модели "Product" в административной панели."""

    list_display = (
        "pk",
        "name",
        "model",
        "launch_date",
    )


@admin.register(Chain)
class ChainAdmin(admin.ModelAdmin):
    """Класс для настройки отображения модели "Chain" в административной панели."""

    def clear_debt(self, request, queryset):
        """Очищает задолженность перед поставщиком."""
        queryset.update(debt=0)

    clear_debt.short_description = "Очистить задолженность перед поставщиком"

    def supplier_name(self, chain):
        """Возвращает ссылку на поставщика для отображения в административной панели."""
        url = reverse("admin:chain_chain_change", args=[chain.id])
        link = '<a href="%s">%s</a>' % (url, chain.name)
        return mark_safe(link)

    supplier_name.short_description = "Поставщик"

    list_display = (
        "pk",
        "name",
        "level",
        "supplier_name",
        "debt",
    )
    list_filter = ("contact__city",)
    actions = [clear_debt]
