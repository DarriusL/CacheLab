# @Time   : 2024.01.15
# @Author : Darrius Lei
# @Email  : darrius.lei@outlook.com

from lib import util, glb_var
from collections.abc import Iterable, deque

logger = glb_var.get_value('log');

class Cache():
    '''Abstract Cache class to define the API methods
    '''
    def __init__(self, cache_cfg, type) -> None:
        if type.lower() not in ['fifo', 'lru', 'lfu']:
            logger.error('This function only supports FIFO/LRU/LFU.')
            raise RuntimeError;
        util.set_attr(self, cache_cfg);
        self.cache = deque(max = self.bs_storagy);

    def extend(self,  cache:deque, __iterable:Iterable, is_unique:bool) -> None:
        if is_unique:
            for item in __iterable:
                if item in cache:
                    cache.remove(item);
        cache.extend(__iterable);
    
    def check_unique(self, __iterable:Iterable) -> int:
        n = int(0);
        for item in __iterable:
            if item in self.cache:
                n += 1;
        return n;
    
    def update(self) -> None:
        logger.error('Method needs to be called after being implemented');
        raise NotImplementedError;