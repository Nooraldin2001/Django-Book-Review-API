"""
This class is for building APIs for the project
"""
#rest_framework librerais
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import filters



from .serializers import BookSerializer, AuthorSerializer
from .models import Book, Author

# Another way to work with api 

class BookListAPI(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'rating']
    search_fields = ['title', 'content']
    ordering_fields = ['rating']


class BookDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all() #it can handle the only one retreving process
    serializer_class = BookSerializer


class AuthorListAPI(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name', 'biography']
    ordering_fields = ['name']


class AuthorDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all() #it can handle the only one retreving process
    serializer_class = AuthorSerializer




# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# @api_view(['GET'])
# def book_list_api(request):
#     """
#     This function will take a request and serialize all books.
#     Returns: All the books in JSON.
#     """
#     books = Book.objects.all()
#     data = BookSerializer(books, many=True).data
#     return Response({'Books': data})

# @api_view(['GET'])
# def book_detail_api(request, id):
#     """
#     This function will take the request and book id from the user.
#     Returns: Book detail in JSON form.
#     """
#     book = Book.objects.get(id=id)
#     data = BookSerializer(book).data
#     return Response({'Book': data})

# @api_view(['GET'])
# def author_list_api(request):
#     """
#     This function will take a request and serialize all authors.
#     Returns: All the authors in JSON.
#     """
#     authors = Author.objects.all()
#     serializer = AuthorSerializer(authors, many=True)
#     return Response({'authors': serializer.data})

# @api_view(['GET'])
# def author_detail_api(request, id):
#     """
#     This function will take the request and author slug from the user.
#     Returns: Author detail in JSON form, including books.
#     """
#     try:
#         author = Author.objects.get(id=id)
#     except Author.DoesNotExist:
#         return Response({'error': 'Author not found'}, status=status.HTTP_404_NOT_FOUND)

#     author_serializer = AuthorSerializer(author)
#     books_serializer = BookSerializer(author.book_set.all(), many=True)
#     return Response({'author': author_serializer.data, 'books': books_serializer.data})

