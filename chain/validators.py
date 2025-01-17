from rest_framework import serializers


def validate_structure(value):
    """Валидатор структуры (иерархии) объекта Chain."""
    level = dict(value).get("level")
    supplier = dict(value).get("supplier")
    if supplier:
        if level <= supplier.level:
            raise serializers.ValidationError("Поставщик не может быть ниже или равен в иерархии")
    elif level is not None and level != 0:
        raise serializers.ValidationError("Уровень больше 0 требует указания поставщика.")
    return value
