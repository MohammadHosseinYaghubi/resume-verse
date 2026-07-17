import django_filters
from apps.resume.models import Skill, SkillCategory

class SkillFilter(django_filters.FilterSet):
    category = django_filters.UUIDFilter(
        field_name="category__id",
    )
    
    name = django_filters.CharFilter(
        lookup_expr="icontains",
    )
    
    created_after = django_filters.DateFilter(
        field_name="created_at",
        lookup_expr="gte",
    )

    created_before = django_filters.DateFilter(
        field_name="created_at",
        lookup_expr="lte",
    )
    
    class Meta:
        model = Skill

        fields = (
            "category",
            "name",
        )
    

class CategoryFilter(django_filters.FilterSet):

    name = django_filters.CharFilter(
        lookup_expr="icontains",
    )

    created_after = django_filters.DateFilter(
        field_name="created_at",
        lookup_expr="gte",
    )

    created_before = django_filters.DateFilter(
        field_name="created_at",
        lookup_expr="lte",
    )

    class Meta:

        model = SkillCategory

        fields = (
            "name",
        )