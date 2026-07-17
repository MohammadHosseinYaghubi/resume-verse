from django.db import models

from apps.common.models import TimeStampedModel


class AnalyticsEventType(models.TextChoices):

    RESUME_VIEW = (
        "resume_view",
        "Resume View",
    )

    PDF_DOWNLOAD = (
        "pdf_download",
        "PDF Download",
    )

    CONTACT = (
        "contact",
        "Contact",
    )


class ResumeAnalytics(TimeStampedModel):

    resume = models.OneToOneField(
        "resume.Resume",
        on_delete=models.CASCADE,
        related_name="analytics",
    )

    total_views = models.PositiveIntegerField(
        default=0,
    )

    total_downloads = models.PositiveIntegerField(
        default=0,
    )

    total_contacts = models.PositiveIntegerField(
        default=0,
    )

    # unique_visitors = models.PositiveIntegerField(
    #     default=0,
    # )

    last_event = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:

        verbose_name = "Resume Analytics"

        verbose_name_plural = "Resume Analytics"

    def __str__(
        self,
    ):

        return self.resume.full_name


class AnalyticsEvent(TimeStampedModel):

    resume = models.ForeignKey(
        "resume.Resume",
        on_delete=models.CASCADE,
        related_name="events",
    )

    event = models.CharField(
        max_length=50,
        choices=AnalyticsEventType.choices,
    )

    ip_address = models.GenericIPAddressField(
        null=True,
        blank=True,
    )

    user_agent = models.TextField(
        blank=True,
    )

    class Meta:

        ordering = (
            "-created_at",
        )

        indexes = [

            models.Index(
                fields=(
                    "resume",
                    "event",
                ),
            ),

            models.Index(
                fields=(
                    "created_at",
                ),
            ),

        ]

    def __str__(
        self,
    ):

        return f"{self.resume.slug} - {self.event}"