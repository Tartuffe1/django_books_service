from django.test import TestCase
from books.forms import BookForm
from books.models import Book

from django.shortcuts import get_object_or_404

class BookFormTestCase(TestCase):
    fixtures = ['books_forms_testdata.json']

    def setUp(self):
        super(BookFormTestCase, self).setUp()
        self.book_1 = Book.objects.get(pk=1)
        self.book_2 = Book.objects.get(pk=2)
    def test_init(self):
        # Test successful init without data.
        form = BookForm(instance=self.book_1)
        self.assertTrue(isinstance(form.instance, Book))
        self.assertEqual(form.instance.pk, self.book_1.pk)
        
    def test_save(self):
        self.assertEqual(self.book_1.title, "The Great Gatsby")
        
        # Test changing title in existing book record
        dict= {'title': "new_title", 'author':"new_author", 'category':"classic", 'price': 11}
        form_1 =BookForm(dict, instance=self.book_1)
        form_1.save()
        self.assertEqual(self.book_1.title, "new_title")
        # pk is still the same
        self.assertEqual(self.book_1.pk, 1)
        
        # Testing without instance argument, it means testing of new record
        form_2 =BookForm(dict)
        form_2.save()
        self.assertEqual(form_2.instance.pk, 4)
        
    def test_forms(self):
        form_data = {'title': "test_title", 'author': "test_author", 'category': "other", 'price': 11}
        form = BookForm(data=form_data)
        self.assertEqual(form.is_valid(), True)
        # other tests relating forms, for example checking the form data    
            
