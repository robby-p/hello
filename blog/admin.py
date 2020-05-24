from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('item', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['item', 'content']
    prepopulated_fields = {'slug': ('item',)}
  
admin.site.register(Post, PostAdmin)