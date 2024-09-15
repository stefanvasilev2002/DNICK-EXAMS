from django.contrib import admin
from .models import *


class AuthorAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser


class BookAdmin(admin.ModelAdmin):
    search_fields = ['genre',]

    def has_add_permission(self, request):
        return request.user.role == 'author'

    def has_change_permission(self, request, obj=None):
        bookAuthors = BookAuthor.objects.filter(book=obj)

        for bookAuthor in bookAuthors:
            if bookAuthor.author.user == request.user:
                return True

        return False

    def save_model(self, request, obj, form, change):
        bookAuthor = BookAuthor(book=obj, author=Author.objects.get(user=request.user))
        obj.save()

        if BookAuthor.objects.filter(book=obj, author=Author.objects.get(user=request.user)).exists():
            return
        bookAuthor.save()

    def get_queryset(self, request):
        if request.user.role == 'author':
            return Book.objects.filter(genre__isnull=False)
        return Book.objects.all()


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(User)
admin.site.register(BookAuthor)
