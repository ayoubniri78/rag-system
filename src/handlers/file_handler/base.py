from abc import ABC,abstractmethod
from typing import Optional
from fastapi import UploadFile,HTTPException
from helpers.config import get_settings,Settings


class BaseHandler(ABC):
    def __init__(self):
        self.app_settings=get_settings()
        self._next_handler : Optional["BaseHandler"] = None

    

    def set_next(self,handler:"BaseHandler") -> "BaseHandler":
        self._next_handler = handler
        return handler

    @abstractmethod
    async def handle(self,file:UploadFile)->Optional[UploadFile]:
        if self._next_handler:
            return await self._next_handler.handle(file)
        return None

