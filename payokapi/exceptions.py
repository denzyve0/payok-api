from typing import Optional

class PayOkError(Exception):
    pass

class PayOkAPIError(Exception):
    def __init__(self, message: str, code: Optional[int] = None) -> None:
        super().__init__(message)
        
        if code:
            self.code = code
        self.message = message
        
    def __str__(self) -> str:
        message = self.message
        if self.code:
            return f"[{self.code}] " + message
        return message

class PayOkServerError(PayOkAPIError):
    def __init__(self, method: str, message: str):
        super().__init__(message=message)
        self.method = method

class InternalServerError(PayOkServerError):
    pass

class InvalidToken(PayOkAPIError):
    pass

