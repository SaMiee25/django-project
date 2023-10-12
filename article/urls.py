from django.urls import path
from .views import getAllArticles, getArticle, createArticle

urlpatterns = [
    path('getarticles/', getAllArticles),
    path('getarticle/', getArticle),
    path('createarticle/', createArticle)
]