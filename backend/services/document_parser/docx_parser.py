"""DOCX document parser."""

from docx import Document
import io
from fastapi import UploadFile


async def parse_docx(file: UploadFile) -> str:
    """Parse DOCX file and extract text."""
    try:
        content = await file.read()
        doc = Document(io.BytesIO(content))
        text = "\n".join([para.text for para in doc.paragraphs])
        return text
    except Exception as e:
        raise ValueError(f"Failed to parse DOCX: {str(e)}")
