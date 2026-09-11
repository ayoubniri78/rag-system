from typing import Optional
from fastapi import UploadFile,HTTPException
from .base import BaseHandler
from helpers.config import get_settings,Settings
from exceptions import FileTooLargeException
 



class SizeHandler(BaseHandler):

    def __init__(self):
        super().__init__()
        self.size_scale = 1048576

    async def handle(self, file: UploadFile) -> Optional[UploadFile]:
        if file.size > self.app_settings.FILE_MAX_SIZE*self.size_scale:
            raise FileTooLargeException()
        return await super().handle(file)