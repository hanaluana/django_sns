from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('',views.article_list, name='article_list'), # /board
    path('<int:article_id>/', views.article_detail, name='article_detail'), # /board/1
    path('create/',views.create_article, name='create_article'),
    path('<int:article_id>/update/', views.update_article, name='update_article'),
    path('<int:article_id>/delete/', views.delete_article, name='delete_article'),
]