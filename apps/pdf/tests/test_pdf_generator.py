from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from django.test import TestCase
from django.contrib.auth import get_user_model

from apps.resume.models import Resume
from apps.pdf.utils.generator import PDFGenerator

User = get_user_model()


class PDFGeneratorTestCase(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="admin",
            password="12345678",
        )

        self.resume = Resume.objects.create(
            user=self.user,
            full_name="Mohsen",
            slug="mohsen",
            title="Backend Developer",
            bio="Bio",
            email="admin@test.com",
            experience="Experience",
            education="Education",
        )

        self.generator = PDFGenerator()

    @patch("apps.pdf.generator.HTML")
    @patch("apps.pdf.generator.render_to_string")
    def test_generate_pdf(
        self,
        mock_render,
        mock_html,
    ):

        mock_render.return_value = "<html></html>"

        with TemporaryDirectory() as directory:

            output = Path(directory) / "resume.pdf"

            result = self.generator.generate(
                resume=self.resume,
                output_path=output,
            )

        mock_render.assert_called_once()

        mock_html.assert_called_once()

        mock_html.return_value.write_pdf.assert_called_once()

        self.assertEqual(
            result,
            output,
        )

    @patch("apps.pdf.generator.HTML")
    @patch("apps.pdf.generator.render_to_string")
    def test_template_used(
        self,
        mock_render,
        mock_html,
    ):

        mock_render.return_value = "<html></html>"

        with TemporaryDirectory() as directory:

            output = Path(directory) / "resume.pdf"

            self.generator.generate(
                resume=self.resume,
                output_path=output,
            )

        args = mock_render.call_args

        self.assertEqual(
            args.args[0],
            self.generator.template_name,
        )

    @patch("apps.pdf.generator.HTML")
    @patch("apps.pdf.generator.render_to_string")
    def test_resume_passed_to_template(
        self,
        mock_render,
        mock_html,
    ):

        mock_render.return_value = "<html></html>"

        with TemporaryDirectory() as directory:

            output = Path(directory) / "resume.pdf"

            self.generator.generate(
                resume=self.resume,
                output_path=output,
            )

        context = mock_render.call_args.args[1]

        self.assertEqual(
            context["resume"].id,
            self.resume.id,
        )