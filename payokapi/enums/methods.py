from enum import Enum

class Methods(str, Enum):
    CARD = "card"
    CARD_UAH = "card_uah"
    CARD_FOREIGN = "card_foreign"
    TINKOFF = "tinkoff"
    SBP = "sbp"
    QIWI = "qiwi"
    YOOMONEY = "yoomoney"
    PAYEER = "payeer"
    ADVCASH = "advcash"
    PERFECTMONEY = "perfect_money"
    WEBMONEY = "webmoney"
    BITCOIN = "bitcoin"
    LITECOIN = "litecoin"
    TETHER = "tether"
    TRON = "tron"
    DOGECOIN = "dogecoin"
    ETHEREUM = "ethereum"
    RIPPLE = "ripple"
    
    def __str__(self) -> str:
        return self.value
    