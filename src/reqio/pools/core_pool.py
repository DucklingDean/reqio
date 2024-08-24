from threading import Thread, Lock
from time      import sleep
from typing    import Callable
from queue     import Queue
from reqio     import ReadyRequest




class CorePool:
    _DEF_POOL_SIZE   :int
    _DEF_NAMING_FUNC :Callable



    _POOL_LOCK    = Lock()
    _SAVE_LOCK    = Lock()
    _tasks_queue  = Queue()

    _response_dict = {}
    _response_list = []




    # _handle_img_error:Callable = lambda error: None # sorry but you need to monkey patch this function. :(






    def __init__(
        self,
        pool_size          : int|None = None, # how many images at the time.
        main_path          : str  = './',
        save_files         : bool = True,  # if you disable this option the pool will not write to the disk
        save_in_list       : bool = False, # if you enable this choice the pool will save all requests in a queue
        save_in_dict       : bool = False,
        naming_function    : Callable|None = None,
        order_start_value  : int = 0,
    ) -> None:

        # Pool
        if pool_size is None:
            pool_size = self._DEF_POOL_SIZE
        assert isinstance(pool_size, int), "'pool_size' should be an 'int'."
        assert pool_size>0               , "'pool_size' should be greater than 0"
        self._POOL = [True,]*pool_size

        # Order
        assert isinstance(order_start_value, int), "'order_start_value' should be an int"
        self._global_order = order_start_value

        # Monkey Patch Functions
        self._NAMING_FUNC = self._DEF_NAMING_FUNC if naming_function is None else naming_function

        # Path
        self._main_path  = main_path
        self._save_files   = save_files

        self._save_in_list = save_in_list
        self._save_in_dict = save_in_dict
            


    def is_alive(self) -> bool:
        """
        check if any task is still runing
        """
        self._SAVE_LOCK.acquire()
        while not self._tasks_queue.empty():
            task:Thread = self._tasks_queue.get()

            if task.is_alive():
                self._tasks_queue.put(task)
                break
                   
        else:
            return False
        return True





    def add(self, request:ReadyRequest|str, special_name:str|None=None, special_path:str|None=None) -> Thread:
        if type(request) == str:
            request = ReadyRequest(request)

        # Add order attr.
        request.order = self._global_order
        self._global_order += 1

        t = Thread(
            target = self._handle_response,
            args   = (request, special_name, special_path)
        )
        self._tasks_queue.put(t)
        t.start()
        return t




    def _handle_response(self, request:ReadyRequest, special_name:str|None, special_path:str|None) -> None:
        self._hold_pool(request)

        path = self._main_path
        if self._save_files:
            if not special_path:
                path += special_name if special_name else self._NAMING_FUNC(request)
            else:
                path = special_path

            with open(path, 'wb') as file:
                file.write(request.response.content)

        self._SAVE_LOCK.acquire()

        if self._save_in_list:
            self._response_list.append(request.response.content)

        if self._save_in_dict:
            self._response_dict[str(request.order).zfill(10)] = request.response.content

        self._SAVE_LOCK.release()





    def _hold_pool(self, request:ReadyRequest) -> None:
        found_empty_pool = False
        while not found_empty_pool:
            self._POOL_LOCK.acquire()
            # 'try': to make sure the lock is free in case of failure.
            # this is temporary.
            try:
                for partition, empty in enumerate(self._POOL.copy()):
                    if empty:
                        found_empty_pool       = True
                        pool_index             = partition
                        self._POOL[pool_index] = False
                        self._POOL_LOCK.release()
                        request.response
                        break

                else:
                    self._POOL_LOCK.release()
                    sleep(0.7)
            except Exception as ex:
                print(ex)
                self._POOL_LOCK.release()



        # empty the array partition for new images to download.
        #self._POOL_LOCK.acquire()
        self._POOL[pool_index] = True
        #self._POOL_LOCK.release()



    @property
    def dict(self) -> dict:
        if self._save_in_dict:
            return {
                key:self._response_dict[key] 
                for key in sorted(self._response_dict.keys())
            }
        raise AttributeError("You did not set 'save_in_dict' to True")


    @property
    def list(self) -> list:
        if self._save_in_list:return self._response_list
        raise AttributeError("You did not set 'save_in_list' to True")















