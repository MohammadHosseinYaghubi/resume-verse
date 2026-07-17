from pathlib import Path

from apps.pdf.selectors import (
    pdf_directory,
)


def ensure_directory() -> Path:
    """
    Ensure PDF directory exists.
    """

    directory = pdf_directory()

    directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    return directory


def delete_file(
    path: Path,
) -> None:
    """
    Delete file if exists.
    """

    if path.exists():

        path.unlink()