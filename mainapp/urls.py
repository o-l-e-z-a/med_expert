from django.urls import path
from .views import (
    CategoryListView,
    CategoryDetailView,
    NewsListView,
    NewsDetailView,
    LicenseDetailView,
    LicenseListView,
    CompanyTypeDetailView,
    SearchView
)

urlpatterns = [
    path('news/', NewsListView.as_view(), name='news'),
    path('news_detail/<str:slug>/', NewsDetailView.as_view(), name='news_detail'),
    path('licenses/', LicenseListView.as_view(), name='licenses'),
    path('license/<int:pk>/', LicenseDetailView.as_view(), name='license_detail'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('company_type/<str:slug>/', CompanyTypeDetailView.as_view(), name='company_type'),
    path('search/', SearchView.as_view(), name='search')
]
