from rest_framework import serializers
from .models import Book



class BookSerializer(serializers.ModelSerializer):
    """
    this class will take all the data 
    Returns it in a json form 
    """
    class Meta:
        model = Book
        fields = '__all__'
