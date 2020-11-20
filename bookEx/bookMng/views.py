from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import MainMenu

from .forms import BookForm, UpdateProfile
from django.http import HttpResponseRedirect
from .models import Book, Wishlist

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib import messages


# Create your views here.
def index(request):
    # return HttpResponse("<h1 align='center'> Hello World</h1>")
    # return render(request, 'base.html')
    # return render(request, 'bookMng/displaybooks.html')
    return render(request,
                  'bookMng/home.html',
                  {
                      'item_list': MainMenu.objects.all()
                  }
                  )


@login_required(login_url=reverse_lazy('login'))
def myprofile(request):
    # return HttpResponse("<h1 align='center'> Hello World</h1>")
    # return render(request, 'base.html')
    # return render(request, 'bookMng/displaybooks.html')
    return render(request,
                  'bookMng/myprofile.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'name': request.user.get_full_name,
                      'email': request.user.email,
                  }
                  )


@login_required(login_url=reverse_lazy('login'))
def postbook(request):
    submitted = False
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            #form.save()
            book = form.save(commit=False)
            try:
                book.username = request.user
            except Exception:
                pass
            book.save()
            return HttpResponseRedirect('/postbook?submitted=True')
    else:
        form = BookForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request,
                  'bookMng/postbook.html',
                  {
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                      'submitted': submitted
                  })


@login_required(login_url=reverse_lazy('login'))
def editbook(request, book_id):
    submitted = False
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            #form.save()
            book = form.save(commit=False)
            try:
                book.username = request.user
            except Exception:
                pass
            # book.save()
            bookold = Book.objects.get(id=book_id)
            bookold.name = book.name
            bookold.web = book.web
            bookold.price = book.price
            bookold.picture = book.picture
            bookold.save()
            return HttpResponseRedirect('/postbook?submitted=True')
    else:
        form = BookForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request,
                  'bookMng/editbook.html',
                  {
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                      'submitted': submitted
                  })


@login_required(login_url=reverse_lazy('login'))
def displaybooks(request):
    books = Book.objects.all()
    for b in books:
        b.pic_path = b.picture.url[14:]
    return render(request,
                  'bookMng/displaybooks.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books
                  }
    )

@login_required(login_url=reverse_lazy('login'))
def sort_books(request):
    books = Book.objects.all()
    sort = request.GET.get('sort')
    if sort == 'lowtohigh':
        books = sorted(books, key=lambda x: x.price, reverse=False)
    elif sort == 'hightolow':
        books = sorted(books, key=lambda x: x.price, reverse=True)
    elif sort == 'a_z':
        books = sorted(books, key=lambda x: x.name.lower()[0], reverse=False)
    elif sort == 'z_a':
        books = sorted(books, key=lambda x: x.name.lower()[0], reverse=True)
    for b in books:
        b.pic_path = b.picture.url[14:]
    return render(request,
                  'bookMng/displaybooks.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books
                  }
    )


# @login_required(login_url=reverse_lazy('login'))
# def displaybookslowtohigh(request):
#     books = Book.objects.all()
#     books = sorted(books, key=lambda x: x.price, reverse=False)
#     for b in books:
#         b.pic_path = b.picture.url[14:]
#     return render(request,
#                   'bookMng/displaybooks.html',
#                   {
#                       'item_list': MainMenu.objects.all(),
#                       'books': books
#                   }
#     )
#
#
# @login_required(login_url=reverse_lazy('login'))
# def displaybookshightolow(request):
#     books = Book.objects.all()
#     books = sorted(books, key=lambda x: x.price, reverse=True)
#     for b in books:
#         b.pic_path = b.picture.url[14:]
#     return render(request,
#                   'bookMng/displaybooks.html',
#                   {
#                       'item_list': MainMenu.objects.all(),
#                       'books': books
#                   }
#     )
#
#
# @login_required(login_url=reverse_lazy('login'))
# def displaybooksa_z(request):
#     books = Book.objects.all()
#     books = sorted(books, key=lambda x: x.name.lower()[0], reverse=False)
#     for b in books:
#         b.pic_path = b.picture.url[14:]
#     return render(request,
#                   'bookMng/displaybooks.html',
#                   {
#                       'item_list': MainMenu.objects.all(),
#                       'books': books
#                   }
#     )
#
#
# @login_required(login_url=reverse_lazy('login'))
# def displaybooksz_a(request):
#     books = Book.objects.all()
#     books = sorted(books, key=lambda x: x.name.lower()[0], reverse=True)
#     for b in books:
#         b.pic_path = b.picture.url[14:]
#     return render(request,
#                   'bookMng/displaybooks.html',
#                   {
#                       'item_list': MainMenu.objects.all(),
#                       'books': books
#                   }
#     )


@login_required(login_url=reverse_lazy('login'))
def mybooks(request):
    books = Book.objects.filter(username=request.user)
    for b in books:
        b.pic_path = b.picture.url[14:]
    return render(request,
                  'bookMng/mybooks.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books
                  }
    )


@login_required(login_url=reverse_lazy('login'))
def mywishlist(request):
    wish = Wishlist.objects.filter(username=request.user)
    # books = Book.objects.filter(username=request.user)
    wish = Wishlist.objects.filter(username=request.user)
    books = []
    for w in wish:
        book = Book.objects.get(id=w.book_id)
        book.pic_path = book.picture.url[14:]
        books.append(book)

    # wishlist = Wishlist.objects
    return render(request,
                  'bookMng/mywishlist.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': zip(books, wish)
                  })


@login_required(login_url=reverse_lazy('login'))
def wishlist_add(request, book_id):
    book = Book.objects.get(id=book_id)
    # wish = Wishlist.objects.filter(username=request.user)
    wish = Wishlist()
    wish.book_id = book_id
    wish.username = request.user
    wish.save()
    return render(request,
                  'bookMng/wishlist_add.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'book': book
                  })


@login_required(login_url=reverse_lazy('login'))
def wishlist_remove(request, book_id):
    wish = Wishlist.objects.get(username=request.user, id=book_id)
    book = Book.objects.get(id=wish.book_id)
    wish.delete()
    # for w in wish:
    #     if w.book_id == book_id:
    #         w.delete()
    return render(request,
                  'bookMng/wishlist_remove.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'book': book
                  })


def search_books(request):
    search = request.GET.get('search')
    search_result = Book.objects.filter(name__contains = search)
    for b in search_result:
        b.pic_path = b.picture.url[14:]
    return render(request,
                  'bookMng/search_result.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': search_result,
                      'search': search
                  })


@login_required(login_url=reverse_lazy('login'))
def book_delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return render(request,
                  'bookMng/book_delete.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  }
    )


@login_required(login_url=reverse_lazy('login'))
def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    book.pic_path = book.picture.url[14:]
    return render(request,
                  'bookMng/book_detail.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'book': book,
                  })


class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        user = form.save(commit=False)
        # user.first_name = "john"
        user.save()
        return HttpResponseRedirect(self.success_url)


@login_required(login_url=reverse_lazy('login'))
def update_profile(request):
    if request.method == 'POST':
        form = UpdateProfile(request.POST)
        if form.is_valid():
            request.user.first_name = form.cleaned_data.get("first_name")
            request.user.last_name = form.cleaned_data.get("last_name")
            request.user.email = form.cleaned_data.get("email")
            request.user.save()
            # Important!
            messages.success(request, 'Profile has been updated!')
            return redirect('/myprofile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UpdateProfile()
    return render(request, 'bookMng/update_profile.html', {
        'form': form,
        'item_list': MainMenu.objects.all()
    })


@login_required(login_url=reverse_lazy('login'))
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/myprofile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'bookMng/change_password.html', {
        'form': form
    })