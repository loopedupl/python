from django.contrib import admin
from blog.models import Author, Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author')  # Kolumny wyświetlane w panelu
    search_fields = ('title', 'content')  # Pola, po których można wyszukiwać
    list_filter = ('title',)  # Dodanie filtrów w panelu bocznym

admin.site.register(Post, PostAdmin)

class ChildModelInline(admin.TabularInline):  # Inline dla modelu zależnego
    model = Post

class AuthorModelAdmin(admin.ModelAdmin):
    inlines = [ChildModelInline]

admin.site.register(Author, AuthorModelAdmin)