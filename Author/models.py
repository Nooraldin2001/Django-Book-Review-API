# models.py

from django.db import models
from django.utils.text import slugify


class Author(models.Model):
    name = models.CharField(max_length=255, help_text="Author's full name")
    birth_date = models.DateField(null=True, blank=True, help_text="Author's birth date")
    biography = models.TextField(blank=True, help_text="Author's biography")
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Author, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Book(models.Model):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    title = models.CharField(max_length=255, help_text="Title of the book")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, help_text="Foreign key to the Author model")
    reviewer_name = models.CharField(max_length=255, help_text="Name of the reviewer")
    content = models.TextField(help_text="Review content")
    rating = models.IntegerField(choices=RATING_CHOICES, help_text="Rating: from 1 to 5")
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
       self.slug = slugify(self.title)
       super(Book, self).save(*args, **kwargs) # Call the real save() method

    def __str__(self):
        return f"{self.title} by {self.author.name}"
