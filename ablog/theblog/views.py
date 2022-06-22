from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

#ListView will format the blog posts as a List
#DetailView will format the detailed blog post view when a blog post is clicked on

#def home(request):
 #   return render(request, 'home.html', {})

#import HomeView as a list view
class HomeView(ListView):
    model = Post
    template_name = 'home.html'


#import Article View as detail view
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'

#import Add post to create a view
class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'



