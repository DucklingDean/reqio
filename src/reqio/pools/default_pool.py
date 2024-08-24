from .core_pool    import CorePool
from reqio.toolkit import NamingFunctions





class DefaultPool(CorePool):
    _DEF_POOL_SIZE   = 4
    _DEF_NAMING_FUNC = NamingFunctions.by_order_zfill


