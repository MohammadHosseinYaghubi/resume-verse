from pathlib import Path
from django.conf import settings
from .constants import (
    PDF_DIRECTORY,
    PDF_EXTENSION,
)


def pdf_directory() -> Path:

    return Path(
        settings.MEDIA_ROOT,
        PDF_DIRECTORY,
    )


def resume_pdf_path(resume) -> Path:

    return pdf_directory() / (
        f"{resume.slug}{PDF_EXTENSION}"
    )


def resume_pdf_exists(resume) -> bool:

    return resume_pdf_path(
        resume,
    ).exists()


def resume_pdf_url(resume):

    return (
        f"{settings.MEDIA_URL}"
        f"{PDF_DIRECTORY}/"
        f"{resume.slug}{PDF_EXTENSION}"
    )