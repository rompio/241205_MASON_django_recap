from django.contrib import admin
from .models import User, Post, Category


class UserAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin (admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)