from typing import Optional
from fastapi import UploadFile,HTTPException
from .base import BaseHandler
from helpers.config import get_settings,Settings
from exceptions import InvalidFileTypeException

class TypeHandler(BaseHandler):
    def __init__(self):
        super().__init__()
    
    async def handle(self, file: UploadFile) -> Optional[UploadFile]:
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            raise InvalidFileTypeException()
        return await super().handle(file)