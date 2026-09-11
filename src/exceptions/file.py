from .base import AppException
from models import ResponseSignal


class InvalidFileTypeException(AppException):

    def __init__(
        self,
        message: str = ResponseSignal.FILE_TYPE_INVALID.value
    ):
        super().__init__(
            message=message,
            code="INVALID_FILE_TYPE",
            status_code=400
        )


class FileTooLargeException(AppException):

    def __init__(
        self,
        message: str = ResponseSignal.FILE_SIZE_INVALID.value
    ):
        super().__init__(
            message=message,
            code="FILE_TOO_LARGE",
            status_code=413
        )