from django.contrib import admin
# Register your models here.

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('userName', 'file','visible')

# Register your models here.

admin.site.register(Post, PostAdmin)
