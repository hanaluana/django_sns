from django.contrib import admin
from .models import Posting

# Register your models here.
class PostingModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at') # 개별 정보 화면
    list_display = ('id', 'content', 'created_at', 'updated_at') # 전체 리스트 화면
    list_display_links = ('id','content') # 리스트에서 click 해서 들어갈 수 있는 column

admin.site.register(Posting, PostingModelAdmin)
