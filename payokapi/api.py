from typing import Optional, Union

from .base import BaseClient
from .types import (
    Balance,
    Transaction,
)
from .exceptions import PayOkAPIError


class PayOk(BaseClient):
    _BASE_URL = "https://payok.io"
    _BASE_API = _BASE_URL + "/api"
    _BASE_PAY = _BASE_URL + "/pay"
    
    def __init__(self,
                 api_id: Union[int, str],
                 api_key: str,
                 secret_key: Optional[str] = None,
                 shop: Optional[int] = None
                 ) -> None:
        super().__init__()
        self.__api_id = api_id
        self.__api_key = api_key
        self.__secret_key = secret_key
        self._shop = shop
        
    async def get_balance(self) -> Balance:
        data = {"API_ID": self.__api_id, "API_KEY": self.__api_key}
        
        resp = await self._request("post", self._BASE_API+"/balance", data=data)
        
        return Balance(**resp)
    
    async def get_transaction(self,
                              payment: Optional[int] = None,
                              offset: Optional[int] = None) -> Union[Transaction, list[Transaction]]:
        data = {"API_ID": self.__api_id, "API_KEY": self.__api_key, "shop": self._shop}
        
        if not self._shop:
            raise PayOkAPIError("The `shop` parameter was not specified. Recreate the `PayOk` instance with this parameter.")
        
        if payment:
            data["payment"] = payment
        if offset:
            data["offset"] = offset
            
        resp = await self._request("post", self._BASE_API+"/transaction", data=data)
        
        if payment:
            return Transaction(**resp['1'])
        
        return [Transaction(**trans) for trans in resp.values()]
        