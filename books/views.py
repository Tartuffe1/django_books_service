# Create your views here.
from django.shortcuts import render, get_object_or_404
from books.models import Book

from forms import BookForm
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect

def books(request):
    latest_book_list = Book.objects.all()[:10]
    context = {'latest_book_list': latest_book_list}
    return render(request, 'books/books.html', context)      
def book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/book.html',
                            {'book': book })

def add_book(request):
   if request.method == 'POST':
      form=BookForm(request.POST)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect('/books/all/')
   else:  
      form=BookForm() 
   
   args={}
   args.update(csrf(request))
   args['form']= form
   return render(request, 'books/add_book.html', args)
