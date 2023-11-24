from django.urls import path
#from .views import book_list, book_detail, author_list, author_detail
#from .api import book_list_api, book_detail_api, author_list_api, author_detail_api
from .api import BookListAPI, BookDetailAPI, AuthorListAPI, AuthorDetailAPI
urlpatterns = [
    # Web views
    # path('books/', book_list, name='book_list'),
    # path('books/<slug:slug>/', book_detail, name='book_detail'),
    # path('authors/', author_list, name='author_list'),
    # path('authors/<int:id>/', author_detail, name='author_detail'),

    # API URLs
    path('api/books/list/', BookListAPI.as_view(), name='book_list_api'),
    path('api/book/detail/<int:id>/', BookDetailAPI.as_view(), name='book_detail_api'),
    path('api/authors/list/', AuthorListAPI.as_view(), name='author_list_api'),
    path('api/authors/detail/<int:id>/', AuthorDetailAPI.as_view(), name='author_detail_api'),
]
