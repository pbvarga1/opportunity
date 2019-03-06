from typing import AnyStr, List, Tuple


class Redis:
    async def hexists(self, key: AnyStr, field: AnyStr) -> bool: ...
    async def hkeys(self, key: AnyStr) -> List[bytes]: ...
    async def hget(self, key: AnyStr, field: AnyStr) -> bytes: ...
    async def hset(self, key: AnyStr, field: AnyStr, value: AnyStr) -> int: ...
    async def hdel(self, key: AnyStr, field: AnyStr) -> int: ...
    async def delete(self, key: AnyStr) -> int: ...


async def create_redis(
    address: Tuple[str, int],
    *,
    db=None,
    password=None,
    ssl=None,
    encoding=None,
    commands_factory=Redis,
    parser=None,
    timeout=None,
    connection_cls=None,
    loop=None) -> Redis: ...
