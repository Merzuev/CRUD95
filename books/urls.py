from django.urls import path
#from books.views import index,create
from books.views import BookListView,BookCreateView, success, BookDetailView, BookUpdateView, BookDeleteView


urlpatterns = [
    path('', BookListView.as_view(), name ='home'),
    path('create/', BookCreateView.as_view(), name='create'),
    path('create/success/', success, name = 'success'),
    path('book/<int:pk>', BookDetailView.as_view(), name ='book_detail'),
    path('book/<int:pk>/edit/',
    BookUpdateView.as_view(), name='book_edit'),
    path('book/<int:pk>/delete/',
    BookDeleteView.as_view(), name='book_delete'),
]