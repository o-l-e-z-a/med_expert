from rest_framework.serializers import ModelSerializer, ListSerializer, Serializer, SlugRelatedField
from .models import License, Company, Category, Service, News


class LicenseSerializer(ModelSerializer):
    """ Сериализатор для просмотра лицензий """

    class Meta:
        model = License
        fields = '__all__'


class NewsDetailSerializer(ModelSerializer):
    """ Сериализатор для просмотра конкретной новости """

    class Meta:
        model = News
        fields = '__all__'


class NewsListSerializer(ModelSerializer):
    """ Сериализатор для просмотра списка новостей """

    class Meta:
        model = News
        exclude = ['photo']


class ServiceListSerializer(ModelSerializer):
    """ Сериализатор для просмотра услуг"""

    class Meta:
        model = Service
        fields = ('name', 'price')


class FilterCategoryListSerializer(ListSerializer):
    """ Сериализатор для рекурсивного вывода родительских категорий """
    def to_representation(self, data):
        data = data.filter(parent_id=None)
        return super().to_representation(data)


class RecursiveSerializer(Serializer):
    """ Сериализатор для рекурсивного вывода "детей" категории"""
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CategoryListSerializer(ModelSerializer):
    """ Сериализатор для просмотра категорий """

    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterCategoryListSerializer
        model = Category
        fields = ("name", "url", "children")


class CompanyListSerializer(ModelSerializer):
    """ Сериализатор для просмотра списка компаний"""

    class Meta:
        model = Company
        fields = ("name",)


class SearchSerializer(ModelSerializer):
    """ Сериализатор для поиска"""
    category = SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Service
        fields = ('name', 'price', 'category')
