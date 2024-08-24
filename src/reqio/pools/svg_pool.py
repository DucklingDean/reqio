from .core_pool    import CorePool
from reqio.toolkit import NamingFunctions






class SVGpool(CorePool):
    _DEF_POOL_SIZE   = 8
    _DEF_NAMING_FUNC = NamingFunctions(file_extension='.svg').by_order
