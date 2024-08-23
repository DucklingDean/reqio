from requests import request, Response
from fake_useragent import UserAgent 





class ReadyRequest:
    order:int

    def __init__(self, 
                 url:str,
                 method:str   = "GET",
                 **kwargs,
                ) -> None:
        self._req         = None
        self.url          = url
        self.method       = method
        self._kwargs:dict = kwargs


    @property
    def response(self) -> Response:
        if self._req is None:
            self._req = request(
                self.method,
                self.url,
                **self._kwargs
            )
        return self._req

    def gen_headers() -> dict[str,str]:
        return {
                    "user-agent":UserAgent().random,
               }

