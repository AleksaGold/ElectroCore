from rest_framework.serializers import ModelSerializer

from chain.models import Chain, Contact, Product
from chain.validators import validate_structure


class ContactSerializer(ModelSerializer):
    """Сериализатор для модели Contact."""

    class Meta:
        model = Contact
        fields = (
            "id",
            "email",
            "country",
            "city",
            "street",
            "house_number",
        )


class ProductSerializer(ModelSerializer):
    """Сериализатор для модели Product."""

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "model",
            "launch_date",
        )


class ChainSerializer(ModelSerializer):
    """Сериализатор для модели Chain."""

    class Meta:
        model = Chain
        fields = (
            "id",
            "name",
            "level",
            "contact",
            "product",
            "supplier",
            "debt",
            "created_at",
        )
        validators = [validate_structure]


class ChainUpdateSerializer(ModelSerializer):
    """Сериализатор для обновления одного объекта модели Chain."""

    class Meta:
        model = Chain
        fields = (
            "id",
            "name",
            "level",
            "contact",
            "product",
            "supplier",
            "created_at",
        )
        validators = [validate_structure]


class ChainDetailSerializer(ModelSerializer):
    """Сериализатор для одного объекта модели Chain."""

    contact = ContactSerializer(read_only=True)
    product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Chain
        fields = (
            "id",
            "name",
            "level",
            "contact",
            "product",
            "supplier",
            "debt",
            "created_at",
        )
