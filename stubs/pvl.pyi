from io import BufferedReader

from typing import Union, MutableMapping, Any, Generator, Tuple, NamedTuple


class OrderedMultiDict(dict, MutableMapping):

    def __getitem__(self, key: Any) -> Any: ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def __iter__(self) -> Generator[Tuple[Any, Any], None, None]: ...
    def __len__(self) -> int: ...
    def copy(self) -> 'OrderedMultiDict': ...


class PVLModule(OrderedMultiDict):

    @property
    def valid(self) -> bool: ...
    def copy(self) -> 'PVLModule': ...


class PVLDecoder:

    def set_strict(self) -> None: ...
    def decode(self, stream: Union[bytes, BufferedReader]) -> PVLModule: ...


class Units(NamedTuple('Units', [('value', Any), ('units', Union[bytes, str])])):
    value: Any
    units: Union[bytes, str]


def loads(data: Union[bytes, str], cls: Any=PVLModule, strict: bool=False, **kwargs) -> PVLModule: ...
def dumps(module: PVLModule) -> bytes: ...