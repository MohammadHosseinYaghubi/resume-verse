import logging
from celery import shared_task
from apps.resume.models import Resume
from apps.pdf.services import generate_resume_pdf

logger = logging.getLogger(__name__)


@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=True,
    retry_kwargs={
        "max_retries": 3,
    },
)
def generate_resume_pdf_task(self, resume_id):

    resume = Resume.objects.get(id=resume_id)
    generate_resume_pdf(resume=resume)

    logger.info(
        "Background PDF generated (%s)",
        resume.slug,
    )