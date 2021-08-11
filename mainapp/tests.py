from datetime import timedelta, date

from decimal import Decimal

from django.urls import reverse
from django.utils import timezone

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Service, News, Category, Company, CompanyType, License
from .serializers import ServiceListSerializer, LicenseSerializer


class NewsTests(APITestCase):

    def setUp(self) -> None:
        self.news1 = News.objects.create(name='test-1', url='test-1', description='test_description', date='2020-07-04')
        self.news1.save()
        self.news2 = News.objects.create(name='test-2', url='test-2', description='test_description', date=date.today())
        self.news2.save()

    def test_news_list(self):
        response = self.client.get(reverse('news'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 2)

    def test_fail_news_detail(self):
        response = self.client.get(reverse('news_detail', kwargs={'slug': 'fail_url'}), format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_news_detail(self):
        response = self.client.get(reverse('news_detail', kwargs={'slug': self.news1.url}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            {
                'id': self.news1.pk,
                'name': 'test-1',
                'url': 'test-1',
                'description': 'test_description',
                'date': '2020-07-04',
                'photo': None
            },
            response.data
        )


class LicenseTests(APITestCase):

    def setUp(self) -> None:
        self.license1 = License.objects.create(name='license_1')
        self.license1.save()
        self.license2 = License.objects.create(name='license_1')
        self.license2.save()

    def test_license_list(self):
        response = self.client.get(reverse('licenses'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        serializer = LicenseSerializer([self.license1, self.license2], many=True)
        self.assertEqual(response.data, serializer.data)

    def test_license_detail(self):
        response = self.client.get(reverse('license_detail', kwargs={'pk': self.license1.pk}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            {
                'id': self.license1.pk,
                'name': 'license_1',
                'photo': None
            },
            response.data
        )

    def test_fail_license_detail(self):
        response = self.client.get(reverse('license_detail', kwargs={'pk': 666}), format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CompanyTests(APITestCase):

    def setUp(self) -> None:
        self.company_type = CompanyType.objects.create(name='Партнеры', url='partneri')
        self.company1 = Company.objects.create(name='Test company', type=self.company_type)

    def test_company_to_type_list(self):
        response = self.client.get(reverse('company_type', kwargs={'slug': self.company_type.url}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0].get('name', None), self.company1.name)

    def test_fail_company_to_type_list(self):
        response = self.client.get(reverse('company_type', kwargs={'slug': 'test_slug'}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)


class ServiceSearchTests(APITestCase):

    def setUp(self) -> None:
        self.category1 = Category.objects.create(name='Приём врачей', url='prichem-vrachej')
        self.category1.save()
        self.category2 = Category.objects.create(name='Приём врача-невролога',
                                                 description='description',
                                                 url='priyom-vracha-nevrologa',
                                                 parent=self.category1)
        self.category2.save()

        self.service1 = Service.objects.create(name='Первичный прием невролога', price='1500', category=self.category2)
        self.service1.save()
        self.service2 = Service.objects.create(name='Повторный прием невролога', price='500', category=self.category2)
        self.service2.save()

    def test_categories_list(self):
        response = self.client.get(reverse('categories'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(len(response.data[0]['children']), 1)

    def test_service_to_category(self):
        response = self.client.get(reverse('category_detail', kwargs={'slug': self.category2.url}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        serializer = ServiceListSerializer([self.service1, self.service2], many=True)
        self.assertEqual(response.data, serializer.data)

    def test_fail_service_to_category(self):
        response = self.client.get(reverse('category_detail', kwargs={'slug': 'test_slug'}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_search(self):
        response_nevrolog = self.client.get(reverse('search') + '?search=Невролог', format='json')
        self.assertEqual(response_nevrolog.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_nevrolog.data), 2)
        response_doctor = self.client.get(reverse('search') + '?search=врач', format='json')
        self.assertEqual(response_doctor.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_doctor.data), 2)
        response_first = self.client.get(reverse('search') + '?search=первичный', format='json')
        self.assertEqual(response_first.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_first.data), 1)

    def test_fail_search(self):
        response = self.client.get(reverse('search') + '?search=fdbdfbdfb', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)



