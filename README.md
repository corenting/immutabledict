# immutabledict

![PyPI](https://img.shields.io/pypi/v/immutabledict) ![Conda](https://img.shields.io/conda/vn/conda-forge/immutabledict) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/immutabledict)

![License](https://img.shields.io/pypi/l/immutabledict) ![Build](https://img.shields.io/github/checks-status/corenting/immutabledict/master?label=build) ![Codecov](https://img.shields.io/codecov/c/github/corenting/immutabledict) ![PyPI - Downloads](https://img.shields.io/pypi/dm/immutabledict)

A fork of the original [frozendict](https://github.com/slezica/python-frozendict), an immutable wrapper around dictionaries.
This library is an MIT-licensed alternative to the new LGPL-3.0 licensed [frozendict](https://github.com/Marco-Sulla/python-frozendict).

It implements the complete mapping interface and can be used as a drop-in replacement for dictionaries where immutability is desired.
The immutabledict constructor mimics dict, and all of the expected interfaces (iter, len, repr, hash, getitem) are provided. Note that an immutabledict does not guarantee the immutability of its values, so the utility of hash method is restricted by usage.

The only difference is that the copy() method of immutable takes variable keyword arguments, which will be present as key/value pairs in the new, immutable copy.

## Installation

Available as `immutabledict` on :
- pypi
- conda-forge (community-maintained, not an official release)
- alpine as [py3-immutabledict](https://pkgs.alpinelinux.org/packages?name=py3-immutabledict)  (community-maintained, not an official release)

## Example

```python
from immutabledict import immutabledict

my_item = immutabledict({"a": "value", "b": "other_value"})
print(my_item["a"]) # Print "value"
```

## Differences with the old original frozendict package

- Dropped support of EOL Python versions (version 1.0.0 supports Python 3.5, versions <= 2.2.1 supports Python 3.6)
- Fixed `collections.Mapping` deprecation warning
- Typing
- [PEP 584 union operators](https://www.python.org/dev/peps/pep-0584/)
