from django.conf import settings
from django.db import models
from . import Skill
from apps.common.models import TimeStampedModel
from ..managers import ResumeManager

# ==========================================================
# Resume
# ==========================================================

class Resume(TimeStampedModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="resume",
    )

    full_name = models.CharField(
        max_length=150,
        db_index=True,
    )

    slug = models.SlugField(
        unique=True,
    )

    title = models.CharField(
        max_length=150,
        help_text="Example: Senior Backend Django Developer",
    )

    bio = models.TextField()

    email = models.EmailField()

    phone = models.CharField(
        max_length=20,
        blank=True,
    )

    location = models.CharField(
        max_length=150,
        blank=True,
    )

    experience = models.TextField()

    education = models.TextField()

    skills = models.ManyToManyField(
        Skill,
        related_name="resumes",
        blank=True,
    )

    profile_picture = models.ImageField(
        upload_to="resume/profile/",
        blank=True,
        null=True,
    )

    background_image = models.ImageField(
        upload_to="resume/background/",
        blank=True,
        null=True,
    )

    is_public = models.BooleanField(
        default=True,
    )

    objects = ResumeManager()

    class Meta:
        ordering = ["-created_at"]

        verbose_name = "Resume"

        verbose_name_plural = "Resumes"

        indexes = [
            models.Index(fields=["full_name"]),
            models.Index(fields=["slug"]),
            models.Index(fields=["created_at"]),
        ]

    def __str__(self):
        return self.full_name