from django.db import models
from apps.common.models import TimeStampedModel

# ==========================================================
# Skill Category
# ==========================================================

class SkillCategory(TimeStampedModel):
    name = models.CharField(
        max_length=50,
        unique=True,
    )

    slug = models.SlugField(
        unique=True,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Skill Category"
        verbose_name_plural = "Skill Categories"

    def __str__(self):
        return self.name


# ==========================================================
# Skill
# ==========================================================

class Skill(TimeStampedModel):
    name = models.CharField(
        max_length=50,
    )

    slug = models.SlugField(
        unique=True,
    )

    category = models.ForeignKey(
        SkillCategory,
        on_delete=models.CASCADE,
        related_name="skills",
    )

    class Meta:
        ordering = ["name"]

        verbose_name = "Skill"

        verbose_name_plural = "Skills"

        indexes = [
            models.Index(fields=["name"]),
        ]

        constraints = [
            models.UniqueConstraint(
                fields=["name", "category"],
                name="unique_skill_per_category",
            ),
        ]

    def __str__(self):
        return self.name