import re
from django.db import models
from .resume import Resume
from .skill import Skill
from apps.common.models import TimeStampedModel
from apps.resume.managers import ProjectManager
objects = ProjectManager()

# ==========================================================
# Project
# ==========================================================

class ProjectStatus(models.TextChoices):
    DRAFT = "draft", "Draft"
    PUBLISHED = "published", "Published"


class Project(TimeStampedModel):
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name="projects",
    )

    title = models.CharField(
        max_length=200,
    )

    slug = models.SlugField(
        unique=True,
    )

    description = models.TextField()

    technologies = models.ManyToManyField(
        Skill,
        related_name="projects",
        blank=True,
    )

    project_url = models.URLField(
        blank=True,
    )

    video_url = models.URLField(
        blank=True,
        help_text="Embed URL",
    )

    image = models.ImageField(
        upload_to="resume/projects/",
        blank=True,
        null=True,
    )

    status = models.CharField(
        max_length=20,
        choices=ProjectStatus.choices,
        default=ProjectStatus.PUBLISHED,
    )

    display_order = models.PositiveIntegerField(
        default=0,
    )

    published_at = models.DateField(
        blank=True,
        null=True,
    )

    class Meta:
        ordering = [
            "display_order",
            "-published_at",
        ]

        indexes = [
            models.Index(fields=["title"]),
            models.Index(fields=["slug"]),
        ]

    def get_embed_url(self):
        if self.video_url and "aparat.com/v/" in self.video_url:
            video_id_match = re.search(
                r"aparat.com/v/(\w+)",
                self.video_url,
            )

            if video_id_match:
                video_id = video_id_match.group(1)

                return (
                    f"https://www.aparat.com/video/video/embed/"
                    f"videohash/{video_id}/vt/frame"
                )

        return self.video_url
    
    @property
    def embed_url(self):
        return self.get_embed_url()

    def __str__(self):
        return self.title
    
    @property
    def is_published(self):

        return (
            self.status
            == ProjectStatus.PUBLISHED
        )
