from django.test import TestCase
from django.core.urlresolvers import reverse

from books.models import Book

class BooksViewsTestCase(TestCase):
    fixtures = ['books_views_testdata.json']
    
    def test_books_all(self):
        resp = self.client.get('/books/all/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('latest_book_list' in resp.context)
        self.assertEqual([book.pk for book in resp.context['latest_book_list']], [1,2,3])
        
        book_1 = resp.context['latest_book_list'][0]
        self.assertEqual(book_1.title, "The Great Gatsby")
        self.assertEqual(book_1.author, "F. Scott Fitzgerald")
        self.assertEqual(book_1.category, "classic")
        self.assertEqual(book_1.price, 50)
        
    def test_book_detail(self):
      resp = self.client.get(reverse('books:detail',kwargs={'book_id':1}))
      self.assertEqual(resp.status_code, 200)
      self.assertTrue('book' in resp.context)
      self.assertEqual(resp.context['book'].pk, 1)
      self.assertEqual(resp.context['book'].title, 'The Great Gatsby')

      # Ensure that non-existent books throw a 404.
      resp = self.client.get(reverse('books:detail',kwargs={'book_id':11}))
      self.assertEqual(resp.status_code, 404)
      
    
    
