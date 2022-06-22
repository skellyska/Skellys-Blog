from django.urls import path
#from . import views
from .views import AddPostView, ArticleDetailView, HomeView 

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    #pk = private key, references primary key (int)
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
]

