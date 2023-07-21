from __future__ import annotations

from collections import OrderedDict
from typing import Any, Dict, Iterable, Iterator, Mapping, Optional, Type, TypeVar

__version__ = "3.0.0"

_K = TypeVar("_K")
_V = TypeVar("_V", covariant=True)


class immutabledict(Mapping[_K, _V]):
    """
    An immutable wrapper around dictionaries that implements
    the complete :py:class:`collections.Mapping` interface.
    It can be used as a drop-in replacement for dictionaries
    where immutability is desired.
    """

    dict_cls: Type[Dict[Any, Any]] = dict

    @classmethod
    def fromkeys(
        cls, seq: Iterable[_K], value: Optional[_V] = None
    ) -> immutabledict[_K, _V]:
        return cls(cls.dict_cls.fromkeys(seq, value))

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self._dict = self.dict_cls(*args, **kwargs)
        self._hash: Optional[int] = None

    def __getitem__(self, key: _K) -> _V:
        return self._dict[key]

    def __contains__(self, key: object) -> bool:
        return key in self._dict

    def copy(self) -> immutabledict[_K, _V]:
        return self.__class__(self)

    def __iter__(self) -> Iterator[_K]:
        return iter(self._dict)

    def __len__(self) -> int:
        return len(self._dict)

    def __repr__(self) -> str:
        return "{}({!r})".format(self.__class__.__name__, self._dict)

    def __hash__(self) -> int:
        if self._hash is None:
            h = 0
            for key, value in self.items():
                h ^= hash((key, value))
            self._hash = h

        return self._hash

    def __or__(self, other: Any) -> immutabledict[_K, _V]:
        if not isinstance(other, (dict, self.__class__)):
            return NotImplemented
        new = dict(self)
        new.update(other)
        return self.__class__(new)

    def __ror__(self, other: Any) -> Dict[Any, Any]:
        if not isinstance(other, (dict, self.__class__)):
            return NotImplemented
        new = dict(other)
        new.update(self)
        return new

    def __ior__(self, other: Any) -> immutabledict[_K, _V]:
        raise TypeError(f"'{self.__class__.__name__}' object is not mutable")


class ImmutableOrderedDict(immutabledict[_K, _V]):
    """
    An immutabledict subclass that maintains key order.
    """

    dict_cls = OrderedDict
