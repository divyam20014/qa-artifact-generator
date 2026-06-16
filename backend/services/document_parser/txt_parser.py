"""TXT document parser."""

from fastapi import UploadFile


async def parse_txt(file: UploadFile) -> str:
    """Parse TXT file and extract text."""
    try:
        content = await file.read()
        text = content.decode("utf-8")
        return text
    except Exception as e:
        raise ValueError(f"Failed to parse TXT: {str(e)}")
