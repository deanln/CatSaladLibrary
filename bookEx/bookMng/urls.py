from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('book_detail/<int:book_id>', views.book_detail, name='book_detail'),
    path('book_delete/<int:book_id>', views.book_delete, name='book_delete'),
    path('postbook', views.postbook, name='postbook'),
    path('myprofile', views.myprofile, name='myprofile'),
    path('displaybooks', views.displaybooks, name='displaybooks'),
    path('mybooks', views.mybooks, name='mybooks'),
    path('sort_books', views.sort_books, name='sort_books'),
    path('editbook/<int:book_id>', views.editbook, name='editbook'),
    path(r'^password/$', views.change_password, name='change_password'),
    path('update_profile', views.update_profile, name='update_profile'),
    path('mywishlist', views.mywishlist, name='mywishlist'),
    path('wishlist_add/<int:book_id>', views.wishlist_add, name='wishlist_add'),
    path('wishlist_remove/<int:book_id>', views.wishlist_remove, name='wishlist_remove'),
    path('search_books', views.search_books, name='search_books'),
]