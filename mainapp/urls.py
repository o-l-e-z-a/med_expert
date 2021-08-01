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
    path('news/', NewsListView.as_view()),
    path('news_detail/<str:slug>/', NewsDetailView.as_view()),
    path('licenses/', LicenseListView.as_view()),
    path('license/<int:pk>/', LicenseDetailView.as_view()),
    path('categories/', CategoryListView.as_view()),
    path('category/<str:slug>/', CategoryDetailView.as_view()),
    path('company_type/<str:slug>/', CompanyTypeDetailView.as_view()),
    path('search/', SearchView.as_view())
]
