from django.contrib import admin
from .models import Post, Donation

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on')
    search_fields = ('title', 'content')
    list_filter = ('created_on',)

admin.site.register(Post, PostAdmin)
admin.site.register(Donation)




