import logging
from weasyprint import HTML
from django.template.loader import render_to_string
from apps.pdf.exceptions import PDFGenerationError
from apps.pdf.context import build_resume_context

logger = logging.getLogger(__name__)


class PDFGenerator:

    template_name = "pdf/resume.html"

    def generate(
        self,
        *,
        resume,
        output_path,
    ):

        try:
            context = build_resume_context(resume=resume)
            html = render_to_string(
                self.template_name,
                context,
            )

            HTML(
                string=html,
            ).write_pdf(
                output_path,
            )

            logger.info(
                "PDF generated: %s",
                output_path,
            )

            return output_path

        except Exception as exc:

            logger.exception(
                "PDF generation failed.",
            )

            raise PDFGenerationError(
                str(exc),
            ) from exc