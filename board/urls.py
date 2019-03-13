from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('',views.article_list, name='article_list'), # /board
    path('<int:article_id>/', views.article_detail, name='article_detail'), # /board/1
    path('create/',views.create_article, name='create_article'),
    path('<int:article_id>/update/', views.update_article, name='update_article'),
    path('<int:article_id>/delete/', views.delete_article, name='delete_article'),

    path('<int:article_id>/comments/create',views.create_comment,name='create_comment'), # board/1/comments/create
    path('<int:article_id>/comments/<int:comment_id>/delete',views.delete_comment, name='delete_comment'),
]