from collections import OrderedDict
from collections.abc import Mapping

__version__ = "1.2.0"


class immutabledict(Mapping):
    """
    An immutable wrapper around dictionaries that implements the complete :py:class:`collections.Mapping`
    interface. It can be used as a drop-in replacement for dictionaries where immutability is desired.
    """

    dict_cls = dict

    @classmethod
    def fromkeys(cls, seq, value=None, *args, **kwargs):
        return cls(dict.fromkeys(seq, value, *args, **kwargs))

    def __init__(self, *args, **kwargs):
        self._dict = self.dict_cls(*args, **kwargs)
        self._hash = None

    def __getitem__(self, key):
        return self._dict[key]

    def __contains__(self, key):
        return key in self._dict

    def copy(self, **add_or_replace):
        return self.__class__(self, **add_or_replace)

    def __iter__(self):
        return iter(self._dict)

    def __len__(self):
        return len(self._dict)

    def __repr__(self):
        return "%s(%r)" % (self.__class__.__name__, self._dict)

    def __hash__(self):
        if self._hash is None:
            h = 0
            for key, value in self.items():
                h ^= hash((key, value))
            self._hash = h
        return self._hash

    def __or__(self, other):
        if not isinstance(other, (dict, self.__class__)):
            return NotImplemented
        new = dict(self)
        new.update(other)
        return self.__class__(new)

    def __ror__(self, other):
        if not isinstance(other, (dict, self.__class__)):
            return NotImplemented
        new = dict(other)
        new.update(self)
        return new

    def __ior__(self, other):
        raise TypeError("'%s' object is not mutable", self.__class__.__name__)


class ImmutableOrderedDict(immutabledict):
    """
    A frozendict subclass that maintains key order
    """

    dict_cls = OrderedDict
