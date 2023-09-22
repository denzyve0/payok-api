import ssl
import asyncio
import platform
from http import HTTPStatus
from typing import Optional

from aiohttp import ClientSession, TCPConnector
from aiohttp.typedefs import StrOrURL

from .exceptions import PayOkAPIError, InternalServerError

class BaseClient:
    """Base aiohttp client"""
    
    def __init__(self) -> None:
      self._loop = asyncio.get_event_loop()
      self._session: Optional[ClientSession] = None
      
      if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
      
    def _get_session(self, **kwargs) -> ClientSession:
        """Get one session per instance.
        If you get first time it will create new session.
        If you get second time it will use an existing session.

        Returns:
            ClientSession: aiohttp session.
        """
        if isinstance(self._session, ClientSession) and not self._session.closed:
            return self._session
        
        ssl_context = ssl.create_default_context()
        conn = TCPConnector(ssl=ssl_context)
        
        self._session = ClientSession(connector=conn, **kwargs)
        return self._session
      
    async def _request(self, method: str, url: StrOrURL, **kwargs: any) -> dict:
        """Make a request using aiohttp.ClientSession.

        Args:
            method (str): Name of HTTP Method.
            url (StrOrURL): endpoint link.
            **kwargs (any): any other data.
        Returns:
            dict: response from server.
        """
        
        session = self._get_session()
        
        async with session.request(method, url, **kwargs) as resp:
            response = resp
            resp = await resp.json(content_type=None)
        
        return self._validate(resp, response)
    
    @staticmethod
    def _validate(resp: dict, response) -> dict:
        """Validate a response. Check on errors, etc"""
        if HTTPStatus.OK <= response.status <= HTTPStatus.IM_USED and response.ok:
            if resp.get('status') == 'error':
                error_code = resp.get('error_code')
                error_text = resp.get('error_text', resp.get('text'))
                raise PayOkAPIError(code=error_code, message=error_text)
            return resp
        
        if response.status == HTTPStatus.INTERNAL_SERVER_ERROR:
            raise InternalServerError(method=response.method, message=response.reason)
        
        
    async def close(self) -> None:
        """Close the session"""
        
        if not isinstance(self._session, ClientSession):
            return
        
        if self._session.closed:
            return
        await self._session.close()
        await asyncio.sleep(0.250) # For full close a session
        
    def __del__(self):
        if self._session and not self._session.closed:
            self._loop.run_until_complete(self._session.close())
            self._loop.run_until_complete(asyncio.sleep(0.250))
            self._loop.close()
