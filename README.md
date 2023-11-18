# Django Book Review API

This is a Django-based API for managing book reviews, authors, and related information. The API includes models for authors and books, with the ability to add reviews to books. Below are the details on how to set up and use this API.

## Requirements

- Python 3.x
- Django
- Django REST framework

## Setup

1. Clone the GitHub repository:

   ```bash
   git clone https://github.com/yourusername/django-book-review-api.git
   ```

2. Navigate to the project directory:

   ```bash
   cd django-book-review-api
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Load dummy data:

   ```bash
   python manage.py loaddata dummy_data
   ```

## Models

### Author

- **name:** Author's full name
- **birth_date:** Author's birth date
- **biography:** Author's biography

### Book

- **title:** Title of the book
- **author:** Foreign key to the Author model
- **reviewer_name:** Name of the reviewer
- **content:** Review content
- **rating:** Rating on a scale from 1 to 5

## API Endpoints

### Books

- **List Books:**
  - Endpoint: `/api/books/`
  - Method: GET
  - Description: Get a list of all books

- **Book Detail:**
  - Endpoint: `/api/books/<book_id>/`
  - Method: GET
  - Description: Get details of a specific book, including reviews

### Authors

- **List Authors:**
  - Endpoint: `/api/authors/`
  - Method: GET
  - Description: Get a list of all authors

- **Author Detail:**
  - Endpoint: `/api/authors/<author_id>/`
  - Method: GET
  - Description: Get details of a specific author, including their books

## Features

- **Search:**
  - Search for books or authors by name.

- **Filter:**
  - Filter books or authors based on certain criteria.

- **Order:**
  - Order the list of books or authors by various attributes.

- **Pagination:**
  - Limit the number of results per page for better performance.

## Usage

1. Run the Django development server:

   ```bash
   python manage.py runserver
   ```

2. Access the API in your browser or a tool like [Postman](https://www.postman.com/).

3. Explore and interact with the API using the provided endpoints.

Feel free to contribute to this project by creating issues, suggesting improvements, or submitting pull requests. Happy coding!
