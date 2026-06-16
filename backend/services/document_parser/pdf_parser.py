"""PDF document parser."""

import pdfplumber
import io
from fastapi import UploadFile


async def parse_pdf(file: UploadFile) -> str:
    """Parse PDF file and extract text."""
    try:
        content = await file.read()
        with pdfplumber.open(io.BytesIO(content)) as pdf:
            text = "\n".join(
                [page.extract_text() for page in pdf.pages if page.extract_text()]
            )
        return text
    except Exception as e:
        raise ValueError(f"Failed to parse PDF: {str(e)}")
