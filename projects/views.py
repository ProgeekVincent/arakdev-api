from rest_framework import generics

from .models import Project
from .serializers import (
    ProjectListSerializer,
    ProjectDetailSerializer,
)

class ProjectListView(generics.ListAPIView):
    serializer_class = ProjectListSerializer

    def get_queryset(self):
        return (
            Project.objects
            .prefetch_related(
                "technologies"
            )
            .order_by(
            	"featured",
                "display_order",
                "-created_at",
            )
        )


class ProjectDetailView(generics.RetrieveAPIView):
    serializer_class = ProjectDetailSerializer
    lookup_field = "slug"

    def get_queryset(self):
        return (
            Project.objects
            .prefetch_related(
                "technologies",
                "images",
                "highlights",
            )
        )