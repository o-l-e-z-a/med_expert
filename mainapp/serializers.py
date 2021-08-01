from rest_framework.serializers import ModelSerializer, ListSerializer, Serializer, SlugRelatedField
from .models import License, Company, Category, Service, News


class LicenseSerializer(ModelSerializer):

    class Meta:
        model = License
        fields = '__all__'


class NewsDetailSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class NewsListSerializer(ModelSerializer):
    class Meta:
        model = News
        exclude = ['photo']


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        exclude = ['category']


class ServiceListSerializer(ModelSerializer):

    class Meta:
        model = Service
        fields = ('name', 'price')


class FilterCategoryListSerializer(ListSerializer):
    def to_representation(self, data):
        data = data.filter(parent_id=None)
        return super().to_representation(data)


class RecursiveSerializer(Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CategoryListSerializer(ModelSerializer):
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterCategoryListSerializer
        model = Category
        fields = ("name", "url", "children")


class CompanyListSerializer(ModelSerializer):

    class Meta:
        model = Company
        fields = ("name",)


class SearchSerializer(ModelSerializer):
    category = SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Service
        fields = ('name', 'price', 'category')