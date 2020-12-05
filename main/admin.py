from django.contrib import admin

from main.models import News, Authors, Category

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','title','date_created','date_update','author','category')
    list_display_links = ('title',)

class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','title')

class AuthorsAdmin(admin.ModelAdmin):
    list_display=('id','name')

admin.site.register (News,NewsAdmin)
admin.site.register(Authors,AuthorsAdmin)
admin.site.register(Category,CategoryAdmin)