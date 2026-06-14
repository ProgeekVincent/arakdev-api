from rest_framework import serializers
from .models import (
    Project,
    ProjectImage,
    ProjectHighlight,
    Technology,
)


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = [
            "id",
            "name",
            "icon",
        ]


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = [
            "id",
            "image",
            "caption",
            "display_order",
        ]


class ProjectHighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectHighlight
        fields = [
            "id",
            "title",
        ]


class ProjectListSerializer(serializers.ModelSerializer):
    technologies = TechnologySerializer(many=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "slug",
            "short_description",
            "thumbnail",
            "project_type",
            "role",
            "featured",
            "status",
            "demo_url",
            "repository_host",
            "repository_url",
            "technologies",
        ]

class ProjectDetailSerializer(serializers.ModelSerializer):
    technologies = TechnologySerializer(many=True)
    images = ProjectImageSerializer(many=True, read_only=True)
    highlights = ProjectHighlightSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "slug",
            "short_description",
            "description",
            "thumbnail",
            "project_type",
            "role",
            "featured",
            "status",
            "demo_url",
            "repository_host",
            "repository_url",
            "start_date",
            "end_date",
            "technologies",
            "images",
            "highlights",
            "created_at",
            "updated_at",
        ]