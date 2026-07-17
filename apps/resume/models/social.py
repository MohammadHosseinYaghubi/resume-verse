from .resume import Resume
from django.db import models
from apps.common.models import TimeStampedModel

# ==========================================================
# Social Links
# ==========================================================

class SocialPlatform(models.TextChoices):
    WEBSITE = "website", "Website"
    GITHUB = "github", "GitHub"
    LINKEDIN = "linkedin", "LinkedIn"
    TWITTER = "twitter", "Twitter"
    TELEGRAM = "telegram", "Telegram"
    INSTAGRAM = "instagram", "Instagram"
    FACEBOOK = "facebook", "Facebook"
    YOUTUBE = "youtube", "YouTube"


class SocialLink(TimeStampedModel):
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name="social_links",
    )

    platform = models.CharField(
        max_length=30,
        choices=SocialPlatform.choices,
    )

    url = models.URLField()
    
    display_order = models.PositiveIntegerField(
        default=0,
    )

    class Meta:
        ordering = ["display_order", "platform"]

        verbose_name = "Social Link"

        verbose_name_plural = "Social Links"

        constraints = [
            models.UniqueConstraint(
                fields=["resume", "platform"],
                name="unique_social_platform",
            ),
        ]

    def __str__(self):
        return f"{self.resume.full_name} - {self.platform}"
