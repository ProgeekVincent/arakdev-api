from django.contrib import admin
from .models import Article, Category, Tag

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "status",
        "featured",
        "category",
        "views",
        "published_at",
    )

    list_filter = (
        "status",
        "featured",
        "category",
        "tags",
    )

    search_fields = (
        "title",
        "excerpt",
        "content",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    filter_horizontal = ("tags",)

    list_editable = ("featured",)

    readonly_fields = ("views", "created_at", "updated_at")

    fieldsets = (
        ("Content", {
            "fields": (
                "title",
                "slug",
                "excerpt",
                "content",
                "cover_image",
            )
        }),
        ("Classification", {
            "fields": (
                "category",
                "tags",
            )
        }),
        ("Publishing", {
            "fields": (
                "status",
                "featured",
                "published_at",
            )
        }),
        ("Analytics", {
            "fields": (
                "views",
                "created_at",
                "updated_at",
            )
        }),
    )