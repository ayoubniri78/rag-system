from .base import AppException
from models import ResponseSignal

class FileStorageException(AppException):
    def __init__(
            self,
            message: ResponseSignal.FILE_STORAGE_FAILED,
        ):
            super().__init__(
                  message=message,
                  code="FILE_STORAGE_FAILED",
                  status_code=500
            )
            