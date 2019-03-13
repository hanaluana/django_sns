from django.shortcuts import render, get_object_or_404, redirect
from board.models import Article, Comment
from IPython import embed

def article_list(request):
    articles = Article.objects.all().order_by('-id')
    # embed()
    return render(request, 'board/list.html', {'articles':articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = article.comment_set.all()
    return render(request, 'board/detail.html',{'article':article, 'comments':comments})

def create_article(request):
    if request.method=="GET":
        return render(request, 'board/new.html')
    else:
        article = Article()
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('board:article_detail',article.id)

def update_article(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method=="GET":
        return render(request, 'board/update.html', {'article':article})
    else:
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('board:article_detail',article.id)

def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == "POST":
        article.delete()
        return redirect('board:article_list')
    elif request.method == "GET":
        return redirect('board:article_detail', article_id)

def create_comment(request,article_id):
    article = get_object_or_404(Article, id=article_id)
    comment = Comment()
    comment.content = request.POST.get('content')
    comment.article = article
    comment.save()
    return redirect('board:article_detail',article.id)

def delete_comment(request, article_id, comment_id):
    article = get_object_or_404(Article, id=article_id)
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        comment.delete()
    return redirect('board:article_detail',article.id)