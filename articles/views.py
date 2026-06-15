from rest_framework import generics
from .models import Article
from .serializers import ArticleListSerializer, ArticleDetailSerializer

class ArticleListView(generics.ListAPIView):
    serializer_class = ArticleListSerializer

    def get_queryset(self):
        return Article.objects.filter(
            status="published"
        ).select_related(
            "category"
        ).prefetch_related(
            "tags"
        )


class ArticleDetailView(generics.RetrieveAPIView):
    serializer_class = ArticleDetailSerializer
    lookup_field = "slug"

    def get_queryset(self):
        return Article.objects.filter(
            status="published"
        ).select_related(
            "category"
        ).prefetch_related(
            "tags"
        )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1
        instance.save(update_fields=["views"])
        return super().retrieve(request, *args, **kwargs)



class RecentFeaturedArticleListView(generics.ListAPIView):
    serializer_class = ArticleListSerializer
    pagination_class = None

    def get_queryset(self):
        return (
            Article.objects
            .filter(
                status="published",
                featured=True
            )
            .select_related("category")
            .prefetch_related("tags")
            .order_by("-published_at")[:3]
        )