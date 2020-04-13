from . import views
from django.conf.urls import url




urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^authors/$', views.AuthorsListView.as_view(), name='authors'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    url(r'^allbooks/$', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),
]

