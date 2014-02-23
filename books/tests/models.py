from django.test import TestCase
from books.models import Book
from django.core.urlresolvers import reverse

class BookModelsTestCase(TestCase):
    def create_book(self, title, author, category, price):
        return Book.objects.create(title=title,
                                      author=author,
                                      category=category,
                                      price=price)     
    def test_book_creation(self):
      book = self.create_book("new_title", "new_author", "classic", 11)
      self.assertTrue(isinstance(book,Book))
      self.assertEqual(book.__unicode__(), book.title)

