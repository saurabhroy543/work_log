from django.http import JsonResponse
from django.shortcuts import render
from .models import Author, Book
from .forms import AddAuthor, AddBook


def library(request):
    form = AddAuthor()
    author_data = Author.objects.all()
    book_data = Book.objects.all()
    data = {
        'authors': author_data,
        'books': book_data
    }
    return render(request, 'library.html', {'form': form, 'authors': author_data,
                                            'books': book_data})


def author(request):
    if request.method == "POST":
        form = AddAuthor(request.POST)
        if form.is_valid():
            authorid = request.POST.get('author_id')
            author = request.POST['author']
            if authorid == '':
                auth = Author(author=author)
            else:
                auth = Author(id=authorid, author=author)

            auth.save()
            authr = Author.objects.values()
            author_data = list(authr)
            return JsonResponse({'status': 'save', 'author_data': author_data})
        else:
            return JsonResponse({'status': 'not saved'})
    elif request.method == "GET":
        author = Author.objects.values()
        author = list(author)
        return JsonResponse({"author": author})


def add_book(request):
    if request.method == "POST":
        book = request.POST['book_name']
        authorid = request.POST['author']
        if book and authorid:
            author_instance = Author.objects.filter(pk=authorid).first()
            authorid = int(authorid)
            bk = Book(book=book, author=author_instance)
            bk.save()
            return JsonResponse({'status': 200, 'data': 'done'})
        else:
            return JsonResponse({'status': 403, 'data': 'Insufficient data '})


def delete_book(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        pi = Book.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status': 0})


def edit_book(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        pi = Book.objects.get(pk=id)
        book_data = {'id': pi.id, 'book': pi.book,
                     'author': pi.author}

        return JsonResponse(book_data)
    else:
        return JsonResponse({'status': 0})
