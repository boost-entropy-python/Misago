from django.urls import reverse
from rest_framework import serializers

from ..core.serializers import MutableFields
from ..core.utils import format_plaintext_for_html
from .models import Category

__all__ = ["CategorySerializer"]


def last_activity_detail(f):
    """util for serializing last activity details"""

    def decorator(self, obj):
        if not obj.last_thread_id:
            return None

        acl = self.get_acl(obj)
        tested_acls = (
            acl.get("can_see"),
            acl.get("can_browse"),
            acl.get("can_see_all_threads"),
        )

        if not all(tested_acls):
            return None

        return f(self, obj)

    return decorator


class CategorySerializer(serializers.ModelSerializer, MutableFields):
    parent = serializers.PrimaryKeyRelatedField(read_only=True)
    description = serializers.SerializerMethodField()
    is_read = serializers.SerializerMethodField()
    subcategories = serializers.SerializerMethodField()
    acl = serializers.SerializerMethodField()

    url = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = [
            "id",
            "parent",
            "name",
            "short_name",
            "color",
            "description",
            "is_closed",
            "threads",
            "posts",
            "last_post_on",
            "last_thread_title",
            "last_poster",
            "last_poster_name",
            "css_class",
            "is_read",
            "subcategories",
            "acl",
            "level",
            "lft",
            "rght",
            "url",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.special_role:
            data["special_role"] = instance.special_role

        return data

    def get_description(self, obj):
        if obj.description:
            return {
                "plain": obj.description,
                "html": format_plaintext_for_html(obj.description),
            }

        # Serve root category's description
        if obj.special_role == "root_category" and self.context:
            settings = self.context["request"].settings
            if settings.index_message:
                return {
                    "plain": settings.index_message,
                    "html": format_plaintext_for_html(settings.index_message),
                }

    def get_css_class(self, obj):
        return obj.css_class or None

    def get_is_read(self, obj):
        try:
            return obj.is_read
        except AttributeError:
            return None

    def get_subcategories(self, obj):
        try:
            return CategorySerializer(
                obj.subcategories, context=self.context, many=True
            ).data
        except AttributeError:
            return []

    def get_acl(self, obj):
        try:
            return obj.acl
        except AttributeError:
            return {}

    @last_activity_detail
    def get_last_poster(self, obj):
        if obj.last_poster_id:
            return {
                "id": obj.last_poster_id,
                "avatars": obj.last_poster.avatars,
                "url": reverse(
                    "misago:user",
                    kwargs={"slug": obj.last_poster_slug, "pk": obj.last_poster_id},
                ),
            }

    def get_url(self, obj):
        return {
            "index": obj.get_absolute_url(),
            "last_thread": self.get_last_thread_url(obj),
            "last_thread_new": self.get_last_thread_new_url(obj),
            "last_post": self.get_last_post_url(obj),
        }

    @last_activity_detail
    def get_last_thread_url(self, obj):
        return obj.get_last_thread_url()

    @last_activity_detail
    def get_last_thread_new_url(self, obj):
        return obj.get_last_thread_new_url()

    @last_activity_detail
    def get_last_post_url(self, obj):
        return obj.get_last_post_url()


class CategoryWithPosterSerializer(CategorySerializer):
    last_poster = serializers.SerializerMethodField()

    def get_subcategories(self, obj):
        try:
            return CategoryWithPosterSerializer(obj.subcategories, many=True).data
        except AttributeError:
            return []


CategoryWithPosterSerializer = CategoryWithPosterSerializer.extend_fields("last_poster")
