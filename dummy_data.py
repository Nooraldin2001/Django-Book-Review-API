# django setup code
import os
import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

import random
from Author.models import Author, Book

fake = Faker()

def create_authors_and_books(n):
    for _ in range(n):
        # Create Author
        author = Author.objects.create(
            name=fake.name(),
            birth_date=fake.date_of_birth(),
            biography=fake.text(),
        )

        # Create Book
        Book.objects.create(
            title=fake.sentence(),
            author=author,
            reviewer_name=fake.name(),
            content=fake.paragraph(),
            rating=random.choice([1, 2, 3, 4, 5]),
        )

    print(f"{n} authors and their books were added successfully")

# Create dummy data
create_authors_and_books(500)
