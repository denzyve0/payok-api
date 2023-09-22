from enum import Enum

class Currency(str, Enum):
    RUB = "RUB" # Рубли
    USD = "USD" # Доллары
    EUR = "EUR" # Евро
    UAH = "UAH" # Гривны
    RUB2 = "RUB2" # Рубли (Альтернативный шлюз)

    def __str__(self) -> str:
        return self.value
