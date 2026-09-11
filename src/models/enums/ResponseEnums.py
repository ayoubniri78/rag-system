from enum import Enum


class ResponseSignal(Enum):
    # Type validation
    FILE_TYPE_VALID = "FILE_TYPE_VALID"
    FILE_TYPE_INVALID = "FILE_TYPE_INVALID"

    # Size validation
    FILE_SIZE_VALID = "FILE_SIZE_VALID"
    FILE_SIZE_INVALID = "FILE_SIZE_INVALID"

    # Global validation
    FILE_VALIDATION_SUCCESS = "FILE_VALIDATION_SUCCESS"
    FILE_VALIDATION_FAILED = "FILE_VALIDATION_FAILED"
    FILE_STORAGE_FAILED = "Unable to store file"