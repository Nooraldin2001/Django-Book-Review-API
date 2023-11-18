"""
This class is for building APIs for the project
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer, AuthorSerializer
from .models import Book, Author


@api_view(['GET'])
def book_list_api(request):
    """
    This function will take a request and serialize all books.
    Returns: All the books in JSON.
    """
    books = Book.objects.all()
    data = BookSerializer(books, many=True).data
    return Response({'books': data})

@api_view(['GET'])
def book_detail_api(request, id):
    """
    This function will take the request and book id from the user.
    Returns: Book detail in JSON form.
    """
    book = Book.objects.get(id=id)
    data = BookSerializer(book).data
    return Response({'book': data})

@api_view(['GET'])
def author_list_api(request):
    """
    This function will take a request and serialize all authors.
    Returns: All the authors in JSON.
    """
    authors = Author.objects.all()
    data = AuthorSerializer(authors, many=True).data
    return Response({'authors': data})

@api_view(['GET'])
def author_detail_api(request, id):
    """
    This function will take the request and author id from the user.
    Returns: Author detail in JSON form.
    """
    author = Author.objects.get(id=id)
    data = AuthorSerializer(author).data
    return Response({'author': data})
