from decimal import Decimal

from rest_framework import serializers

from library.models import Author, Book, User
from djoser.serializers import UserSerializer as CurrentUserSerializer
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'isbn', 'book_number', 'description', 'author', 'discounted_price', 'genre']

    author = serializers.HyperlinkedRelatedField(
        queryset=Author.objects.all(),
        view_name='author_detail'
    )
    book_number = serializers.CharField(max_length=13, source='isbn')
    discounted_price = serializers.SerializerMethodField(method_name='calculate')

    def calculate(self, book: Book):
        calculated_price = book.price * Decimal(0.1)
        rounded_price = round(calculated_price, 2)
        return rounded_price


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']


class UserSerializers(CurrentUserSerializer):
    class Meta(CurrentUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
