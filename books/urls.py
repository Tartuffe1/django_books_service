from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^all/$','books.views.books'),
    url(r'^get/(?P<book_id>\d+)/$','books.views.book', name='detail'),
    url(r'^add_book/$','books.views.add_book'),
    url(r'^(?P<book_category>\w+)/$','books.views.category', name='category'),
)
