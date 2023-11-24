"""
This class is for building APIs for the project
"""
#rest_framework librerais
from rest_framework import status
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
    return Response({'Books': data})

@api_view(['GET'])
def book_detail_api(request, id):
    """
    This function will take the request and book id from the user.
    Returns: Book detail in JSON form.
    """
    book = Book.objects.get(id=id)
    data = BookSerializer(book).data
    return Response({'Book': data})

@api_view(['GET'])
def author_list_api(request):
    """
    This function will take a request and serialize all authors.
    Returns: All the authors in JSON.
    """
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return Response({'authors': serializer.data})

@api_view(['GET'])
def author_detail_api(request, id):
    """
    This function will take the request and author slug from the user.
    Returns: Author detail in JSON form, including books.
    """
    try:
        author = Author.objects.get(id=id)
    except Author.DoesNotExist:
        return Response({'error': 'Author not found'}, status=status.HTTP_404_NOT_FOUND)

    author_serializer = AuthorSerializer(author)
    books_serializer = BookSerializer(author.book_set.all(), many=True)
    return Response({'author': author_serializer.data, 'books': books_serializer.data})