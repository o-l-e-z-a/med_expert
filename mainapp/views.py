from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import filters

from .models import News, License, Category, Service, Company
from .serializers import (
    NewsListSerializer,
    NewsDetailSerializer,
    CategoryListSerializer,
    ServiceListSerializer,
    LicenseSerializer,
    CompanyListSerializer,
    SearchSerializer
)
from .service import PaginationNews


class NewsListView(ListAPIView):
    """ Просмотр списка новостей """
    serializer_class = NewsListSerializer
    queryset = News.objects.all()
    pagination_class = PaginationNews


class NewsDetailView(RetrieveAPIView):
    """ Детальный просмотр конкретной новости"""
    serializer_class = NewsDetailSerializer
    queryset = News.objects.all()
    lookup_url_kwarg = 'slug'
    lookup_field = 'url'


class LicenseListView(ListAPIView):
    """ Просмотр списка лицензий"""
    serializer_class = LicenseSerializer
    queryset = License.objects.all()


class LicenseDetailView(RetrieveAPIView):
    """ Детальный просмотр конкртетной лицензии"""
    serializer_class = LicenseSerializer
    queryset = License.objects.all()


class CategoryListView(ListAPIView):
    """ Просмотр списка категорий"""
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class SearchView(ListAPIView):
    """ Поиск """
    queryset = Service.objects.all()
    serializer_class = SearchSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', "category__name"]


class CategoryDetailView(ListAPIView):
    """  Просмотр услуг, принадлежащих к конкретной категории"""
    serializer_class = ServiceListSerializer

    def get_queryset(self):
        return Service.objects.filter(category__url=self.kwargs['slug'])


class CompanyTypeDetailView(ListAPIView):
    """  Просмотр компаний, принадлежащих к конкретному типу компании"""
    serializer_class = CompanyListSerializer

    def get_queryset(self):
        return Company.objects.filter(type__url=self.kwargs['slug'])

