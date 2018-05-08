from django.urls import path
from .views import PublisherList, BookList,\
    PubBookList, AuthorDetailView, MyView,\
    Safadao, LibraryHome, AuthorList

urlpatterns = [
    path('', LibraryHome.as_view(), name='home'),

    path('publishers/', PublisherList.as_view(), name='publishers'),

    path('books/<str:pub>', PubBookList.as_view(), name='pub_book'),
    path('books/', BookList.as_view(), name='books'),

    path('authors/<int:pk>', AuthorDetailView.as_view(), name='author_detail'),
    path('authors/', AuthorList.as_view(), name='authors'),

    path('req/', MyView.as_view(), name='myview'),
    path('safadao/<str:nome>', Safadao.as_view(), name='safadao'),
]