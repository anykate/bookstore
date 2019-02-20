from django.contrib import admin

# Register your models here.

from .models import Book, Author, Review, BookOrder, Cart


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'stock', 'price']


class BookOrderAdmin(admin.ModelAdmin):
    list_display = ['book', 'cart', 'quantity']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'active', 'order_date']


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(BookOrder, BookOrderAdmin)
admin.site.register(Cart, CartAdmin)