from typing import Optional

class PayOkError(Exception):
    pass

class PayOkAPIError(Exception):
    def __init__(self, message: str, code: Optional[int] = None) -> None:
        self.code = int(code) if code else None
        self.message = message
        super().__init__(self.code)
    
    def __str__(self) -> str:
        return f"{f'[{self.code}] ' if self.code else ''}{self.message}"

class PayOkServerError(PayOkAPIError):
    def __init__(self, method: str, message: str):
        super().__init__(message=message)
        self.method = method

class InternalServerError(PayOkServerError):
    pass

class InvalidToken(PayOkAPIError):
    pass

