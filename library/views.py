from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView, TemplateView
from django.views import View
from django.utils import timezone

from .models import Publisher, Book, Author

class LibraryHome(TemplateView):
    template_name = 'library/index.html'

class AuthorList(ListView):
    model = Author

class PublisherList(ListView):
    # nao precisa por causa do queryset
    # model = Publisher
    context_object_name = 'pubs'
    queryset = Publisher.objects.order_by('-name')

class BookList(ListView):
    model = Book
    # igual a linha abaixo
    queryset = Book.objects.all()
    # template_name = 'library/book_list.html'

class PublisherDetail(DetailView):
    model = Publisher

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = Book.objects.all()
        return context

class PubBookList(ListView):
    template_name = 'library/books_by_pub.html'
    context_object_name = 'books'

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher,
            name=self.kwargs['pub'])
        return Book.objects.filter(publisher=self.publisher)

class AuthorDetailView(DetailView):
    model = Author

    def get_object(self):
        object = super().get_object()
        object.last_accessed = timezone.now()
        object.name = "teste 2"
        # raise Exception(object)
        object.save()
        return object


# simple view example
# pattern: /req/
class MyView(View):
    def get(self, request):
        if request.method == "GET":
            return HttpResponse("GueTchyyy!")

    def post(self, request):
        if request.method == "POST":
            return HttpResponse("Poustchyy!")

class Safadao(View):
    def get(self, request, nome): 
        vagabundo = self.hamming(nome, 'wesley')
        anjo = 100 - vagabundo

        if nome.upper() != 'wesley'.upper():
            anjo, vagabundo = vagabundo, anjo

        data = {
            'nome': nome,
            'anjo': anjo,
            'vagabundo': vagabundo
        }

        return JsonResponse(data)

    def hamming(self, x, y):
        diffs = 0
        for ch1, ch2 in zip(x, y):
                if ch1 != ch2:
                        diffs += 1
        return diffs
