from .core_pool    import CorePool
from reqio.toolkit import NamingFunctions






class HTMLpool(CorePool):
    _DEF_POOL_SIZE   = 4
    _DEF_NAMING_FUNC = NamingFunctions(file_extension='.html').by_order
