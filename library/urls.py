from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register the AuthorViewSet
router = DefaultRouter()
router.register('authors', views.AuthorViewSet)
router.register('users', views.UserViewSet)
router.register('books', views.BookViewSet)

urlpatterns = [
    # path('books/', views.book_list, name='book_list'),
    # path('book/<int:pk>/', views.book_detail, name='book_detail'),
    # path('welcome/', views.welcome),
    path('authors/<int:pk>/', views.AuthorDetail.as_view(), name='author_detail'),
    path('', include(router.urls)),
]
