"""File utility functions."""

from fastapi import UploadFile
from config.settings import Settings


async def validate_file(file: UploadFile) -> bool:
    """Validate uploaded file."""
    content = await file.read()
    file_size_mb = len(content) / (1024 * 1024)
    
    if file_size_mb > Settings.MAX_FILE_SIZE_MB:
        return False
    
    await file.seek(0)
    return True
