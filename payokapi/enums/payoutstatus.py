from enum import Enum

class Status(int, Enum):
    WAITING = 0
    PAID = 1
    BAD = 2