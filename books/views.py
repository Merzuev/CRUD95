from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from books.models import Book
from django.views.generic import ListView, CreateView,DetailView
from django.views.generic.edit import UpdateView,DeleteView

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_delete.html'
    success_url = reverse_lazy('home')

class BookUpdateView(UpdateView):
    model = Book    
    template_name = 'book_edit.html'
    fields = ['name', 'author', 'description']
    def get_success_url(self):
        return reverse('home')


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'


class BookListView(ListView):
    model = Book
    template_name = 'index.html'
    context_object_name ='books'

class BookCreateView(CreateView):
    model = Book
    fields = ['name', 'author', 'description']
    template_name = 'create.html'
    success_url = 'success'
 
def success(request):
    return render(request, 'success.html')