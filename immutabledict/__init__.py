from collections import OrderedDict
from collections.abc import Mapping

__version__ = "1.0.0"


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


class ImmutableOrderedDict(immutabledict):
    """
    A frozendict subclass that maintains key order
    """

    dict_cls = OrderedDict
