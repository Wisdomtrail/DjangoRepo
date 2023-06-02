from django_filters import rest_framework as filters
from .models import Author, Book, User


class AuthorFilter(filters.FilterSet):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']


class BookFilter(filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'title': ['exact'],
            'price': ['gt', 'lt']
        }


class UserFilter(filters.FilterSet):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
