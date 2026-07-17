from django.db import models
from apps.common.models import TimeStampedModel
from apps.resume.models import Resume

# Create your models here.
class ResumePDF(TimeStampedModel):

    resume = models.OneToOneField(
        Resume,
        on_delete=models.CASCADE,
        related_name="pdf",
    )

    file = models.FileField(
        upload_to="pdf/resumes/",
        blank=True,
        null=True,
    )

    generated_at = models.DateTimeField(
        blank=True,
        null=True,
    )

    is_generating = models.BooleanField(
        default=False,
    )