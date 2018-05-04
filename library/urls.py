from django.urls import path
from .views import PublisherList, BookList,\
    PubBookList, AuthorDetailView, MyView,\
    Safadao

urlpatterns = [
    path('publishers/', PublisherList.as_view(), name='publishers'),
    path('books/<str:pub>', PubBookList.as_view()),
    path('authors/<int:pk>', AuthorDetailView.as_view()),
    path('books/', BookList.as_view(), name='books'),
    path('req/', MyView.as_view(), name='myview'),
    path('safadao/<str:nome>', Safadao.as_view(), name='dirty_wesley'),
]