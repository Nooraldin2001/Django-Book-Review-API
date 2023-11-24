from rest_framework import serializers
from .models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    """
    this class will take all the data 
    Returns it in a json form for author model
    """
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name', read_only=True)
    
    """
    this class will take all the data 
    Returns it in a json form for Books model 
    """
    class Meta:
        model = Book
        fields = '__all__'