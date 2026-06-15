from django.urls import path
from .views import ArticleListView, ArticleDetailView, RecentFeaturedArticleListView

urlpatterns = [
    path("", ArticleListView.as_view(), name="article-list"),
    path("<slug:slug>/", ArticleDetailView.as_view(), name="article-detail"),
    path("featured/", RecentFeaturedArticleListView.as_view()),
]