from django.shortcuts import render

# Create your views here.

"""
    here we use this file of views if we would make a fronend website 
    but in this project case we gonna only build api's 
"""

# from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# from django.shortcuts import render, get_object_or_404
# from .models import Book, Author


# def book_list(request):
#     all_books = Book.objects.all()
#     books_count = all_books.count()

#     page = request.GET.get('page', 1)

#     paginator = Paginator(all_books, 50)
#     try:
#         all_books = paginator.page(page)
#     except PageNotAnInteger:
#         all_books = paginator.page(1)
#     except EmptyPage:
#         all_books = paginator.page(paginator.num_pages)

#     return render(request, 'book/book_list.html', {'books': all_books, 'books_count': books_count})

# def book_detail(request, id):
#     book = get_object_or_404(Book, id=id)
#     return render(request, 'book/book_detail.html', {'book': book})

# def author_list(request):
#     all_authors = Author.objects.all()
#     authors_count = all_authors.count()

#     page = request.GET.get('page', 1)

#     paginator = Paginator(all_authors, 50)
#     try:
#         all_authors = paginator.page(page)
#     except PageNotAnInteger:
#         all_authors = paginator.page(1)
#     except EmptyPage:
#         all_authors = paginator.page(paginator.num_pages)

#     return render(request, 'author/author_list.html', {'authors': all_authors, 'authors_count': authors_count})

# def author_detail(request, id):
#     author = get_object_or_404(Author, id=id)
#     return render(request, 'author/author_detail.html', {'author': author})
