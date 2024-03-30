from django.contrib import admin

from .models import Book, Author, Address, Country
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)  # takes a tuple as input argument

    # takes a dict as input argument
    prepopulated_fields = {"slug": ("title",)}

    # takes a tuple as input with the fields for which we want to add a filter
    list_filter = ("author", "rating",)
    # takes a tuple as input with the fields for which we want to add a column in admin
    list_display = ("title", "author",)


    # key is the field name that should be prepopulated
    # value - a tuple that lists all the fields should be used for pre-populating this field
    #
admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)
