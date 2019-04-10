from .models import Author
from .models import Post

from django.contrib import admin

# Register your models here.

admin.site.register(Post)

admin.site.register(Author)
