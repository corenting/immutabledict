# immutabledict

![PyPI](https://img.shields.io/pypi/v/immutabledict) ![Conda](https://img.shields.io/conda/vn/conda-forge/immutabledict) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/immutabledict)

![License](https://img.shields.io/pypi/l/immutabledict) ![Build](https://img.shields.io/github/actions/workflow/status/corenting/immutabledict/ci.yml?branch=master) ![Codecov](https://img.shields.io/codecov/c/github/corenting/immutabledict) ![PyPI - Downloads](https://img.shields.io/pypi/dm/immutabledict)

A fork of the original [frozendict](https://github.com/slezica/python-frozendict), an immutable wrapper around dictionaries.
This library is a pure Python, MIT-licensed alternative to the new LGPL-3.0 licensed [frozendict](https://github.com/Marco-Sulla/python-frozendict).

It implements the complete mapping interface and can be used as a drop-in replacement for dictionaries where immutability is desired.
The immutabledict constructor mimics dict, and all of the expected interfaces (iter, len, repr, hash, getitem) are provided. Note that an immutabledict does not guarantee the immutability of its values, so the utility of hash method is restricted by usage.

## Installation

Official release in [on pypy](https://pypi.org/project/immutabledict/) as `immutabledict`.

**Community-maintained** releases are available:
- On [conda-forge](https://anaconda.org/conda-forge/immutabledict) as `immutabledict`
- On [various package repositories](https://repology.org/project/python:immutabledict/versions)

## Example

```python
from immutabledict import immutabledict

my_item = immutabledict({"a": "value", "b": "other_value"})
print(my_item["a"]) # Print "value"
```

## Differences with the old original frozendict package

- Dropped support of EOL Python versions (older versions of the library may support older Python versions)
- Fixed `collections.Mapping` deprecation warning
- Typing
- [PEP 584 union operators](https://www.python.org/dev/peps/pep-0584/)
- Keep the same signature for `copy()` as `dict` (starting with immutabledict 3.0.0), don't accept extra keyword arguments.
