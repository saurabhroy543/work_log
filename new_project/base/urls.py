from django.urls import path
from . import views

urlpatterns = [
    path('add_book', views.add_book, name='savebook'),
    path('library', views.library, name='library'),
    path('author', views.author, name='author'),
    path('author_delete',views.delete_author,name = 'delete_author'),
    path('delete_book', views.delete_book, name='delete_book'),
    path('edit_book', views.edit_book, name='edit_book'),
    path('edit_author', views.edit_author, name='edit_author'),

]
