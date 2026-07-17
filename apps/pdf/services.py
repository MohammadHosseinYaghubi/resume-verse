import logging
from apps.pdf.utils.generator import PDFGenerator
from apps.pdf.utils.storage import (
    ensure_directory,
    delete_file,
)

from apps.pdf.selectors import (
    resume_pdf_exists,
    resume_pdf_path,
    resume_pdf_url,
)

from apps.pdf.tasks import (
    generate_resume_pdf_task,
)

logger = logging.getLogger(__name__)

generator = PDFGenerator()


def generate_resume_pdf(*, resume):

    ensure_directory()

    output = resume_pdf_path(
        resume,
    )

    generator.generate(

        resume=resume,

        output_path=output,

    )

    logger.info(
        "Resume PDF generated (%s)",
        resume.slug,
    )

    return output


def delete_resume_pdf(*, resume):

    delete_file(

        resume_pdf_path(
            resume,
        )

    )


def regenerate_resume_pdf(*, resume):

    delete_resume_pdf(
        resume=resume,
    )

    return generate_resume_pdf(
        resume=resume,
    )


def enqueue_resume_pdf(*, resume):

    generate_resume_pdf_task.delay(
        str(
            resume.id,
        )
    )


def pdf_status(*, resume):

    if resume_pdf_exists(
        resume,
    ):

        return {

            "status": "ready",

            "download_url": resume_pdf_url(
                resume,
            ),

        }

    return {

        "status": "processing",

    }