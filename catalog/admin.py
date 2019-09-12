from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'language', 'display_genre']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'date_of_birth', 'date_of_death']
    # fields = ['first_name'] # , 'last_name', ('date_of_birth', 'date_of_death')]
    # exclude = ['date_of_death']

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back', 'borrower')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )

admin.site.register(Book, BookAdmin)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)

