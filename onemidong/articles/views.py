from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def create(request):
  if request.method == 'POST':
    article_form = ArticleForm(request.POST)
    if article_form.is_valid():
      article_form.save(commit=False)
      article_form.user = request.user
      article_form.save()
      return redirect('articles:index')
  else:
    article_form = ArticleForm()
  context = {
    'article_form': article_form,    
  }
  return render(request, 'articles/create.html', context)


def detail(request, article_pk):
  article = get_object_or_404(Article, pk=article_pk)
  context = {
    'article': article
  }
  return render(request, 'articles/detail.html', context)


def update(request, article_pk):
  article = get_object_or_404(Article, pk=article_pk)
  if request.method == 'POST':
    article_form = ArticleForm(request.POST, instance=article)
    if article_form.is_valid():
      article_form.save()
      return redirect('articles:detail', article.pk)
  else:
    article_form = ArticleForm()
  context = {
    'article_form': article_form,
  }
  return render(request, 'articles/update.html', context)


def delete(request, article_pk):
  article = get_object_or_404(Article, pk=article_pk)
  article.delete()
  return redirect('articles:index')


    