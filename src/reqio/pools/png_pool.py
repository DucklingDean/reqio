from .core_pool    import CorePool
from reqio.toolkit import NamingFunctions





class PNGpool(CorePool):
    _DEF_NAMING_FUNC = NamingFunctions(file_extension=".png").by_order_zfill
    _DEF_POOL_SIZE   = 6

