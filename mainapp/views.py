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
    serializer_class = NewsListSerializer
    queryset = News.objects.all()
    pagination_class = PaginationNews


class NewsDetailView(RetrieveAPIView):
    serializer_class = NewsDetailSerializer
    queryset = News.objects.all()
    lookup_url_kwarg = 'slug'
    lookup_field = 'url'


class LicenseListView(ListAPIView):
    serializer_class = LicenseSerializer
    queryset = License.objects.all()


class LicenseDetailView(RetrieveAPIView):
    serializer_class = LicenseSerializer
    queryset = License.objects.all()


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class SearchView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = SearchSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', "category__name"]


class CategoryDetailView(ListAPIView):
    serializer_class = ServiceListSerializer

    def get_queryset(self):
        return Service.objects.filter(category__url=self.kwargs['slug'])


class CompanyTypeDetailView(ListAPIView):
    serializer_class = CompanyListSerializer

    def get_queryset(self):
        return Company.objects.filter(type__url=self.kwargs['slug'])

