from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)

from chain.models import Chain, Contact, Product
from chain.serializers import (ChainDetailSerializer, ChainSerializer,
                               ContactSerializer, ProductSerializer)


class ContactCreateAPIView(CreateAPIView):
    """Представление для создания объекта модели Contact."""

    serializer_class = ContactSerializer


class ContactListAPIView(ListAPIView):
    """Представление для просмотра списка объектов модели Contact."""

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactRetrieveAPIView(RetrieveAPIView):
    """Представление для просмотра одного объекта модели Contact."""

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactUpdateAPIView(UpdateAPIView):
    """Представление для обновления объекта модели Contact."""

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDestroyAPIView(DestroyAPIView):
    """Представление для удаления объекта модели Contact."""

    queryset = Contact.objects.all()


class ProductCreateAPIView(CreateAPIView):
    """Представление для создания объекта модели Product."""

    serializer_class = ProductSerializer


class ProductListAPIView(ListAPIView):
    """Представление для просмотра списка объектов модели Product."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveAPIView(RetrieveAPIView):
    """Представление для просмотра одного объекта модели Product."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPIView(UpdateAPIView):
    """Представление для обновления объекта модели Product."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDestroyAPIView(DestroyAPIView):
    """Представление для удаления объекта модели Product."""

    queryset = Product.objects.all()


class ChainCreateAPIView(CreateAPIView):
    """Представление для создания объекта модели Chain."""

    serializer_class = ChainSerializer


class ChainListAPIView(ListAPIView):
    """Представление для просмотра списка объектов модели Chain."""

    queryset = Chain.objects.all()
    serializer_class = ChainSerializer


class ChainRetrieveAPIView(RetrieveAPIView):
    """Представление для просмотра одного объекта модели Chain."""

    queryset = Chain.objects.all()
    serializer_class = ChainDetailSerializer


class ChainUpdateAPIView(UpdateAPIView):
    """Представление для обновления объекта модели Chain."""

    queryset = Chain.objects.all()
    serializer_class = ChainSerializer


class ChainDestroyAPIView(DestroyAPIView):
    """Представление для удаления объекта модели Chain."""

    queryset = Chain.objects.all()
