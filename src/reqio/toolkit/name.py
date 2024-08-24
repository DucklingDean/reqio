from reqio    import ReadyRequest

from typing   import Callable
from hashlib  import md5, sha1, sha256, sha512
                





class NamingFunctions:
    def __init__(self, file_extension:str="", add_length:bool=False) -> None:
        self.file_extension = file_extension
        self.add_length     = add_length


    def _add_file_extension(func:Callable) -> Callable:
        def wrapper(*args, **kwargs) -> str:
            try:
                if type(args[0])==NamingFunctions:
                    # in case 'self' was in '*args' then 'file_extension' will be added to the end
                    # args[0] == self
                    # args[1] == request
                    name = func(args[1])
                    if args[0].add_length: name += f"${len(args[1].response.content)}"
                    return name + args[0].file_extension
                else:
                    # will pass just the normal args & kwargs.
                    return func(*args)
                
            except IndexError:
                raise TypeError(f"'{func.__name__}' missing 1 required positional argument")
        return wrapper



    @_add_file_extension
    def by_order(request:ReadyRequest) -> str:
        return str(request.order)



    @_add_file_extension 
    def by_order_zfill(request:ReadyRequest) -> str:
        return str(request.order).zfill(6)



    @_add_file_extension
    def response_md5sum(request:ReadyRequest) -> str:
        return md5(request.response.content).hexdigest()



    @_add_file_extension
    def response_sha1sum(request:ReadyRequest) -> str:
        return sha1(request.response.content).hexdigest()

    

    @_add_file_extension
    def response_sha256sum(request:ReadyRequest) -> str:
        return sha256(request.response.content).hexdigest()
    


    @_add_file_extension
    def response_sh512sum(request:ReadyRequest) -> str:
        return sh512(request.response.content).hexdigest()

    

    @_add_file_extension
    def url_md5sum(request:ReadyRequest) -> str:
        return md5(request.url.encode()).hexdigest()



    @_add_file_extension
    def url_sha1sum(request:ReadyRequest) -> str:
        return sha1(request.url.encode()).hexdigest()



    @_add_file_extension
    def url_sha256sum(request:ReadyRequest) -> str:
        return sha256(request.url.encode()).hexdigest()



    @_add_file_extension
    def url_sha512sum(request:ReadyRequest) -> str:
        return sha512(request.url.encode()).hexdigest()
