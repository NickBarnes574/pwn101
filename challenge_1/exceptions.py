# exceptions.py
import os


class ClientError(Exception):
    """Base exception for client errors."""

    def __init__(self, message, error_code=os.EX_SOFTWARE):
        super().__init__(message)
        self.message = message
        self.error_code = error_code

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"


class ArgumentValidationError(ClientError):
    """Raised when argument validation fails."""

    def __init__(self, message="Invalid arguments provided."):
        super().__init__(message, os.EX_USAGE)
