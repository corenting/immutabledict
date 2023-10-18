# immutabledict

![PyPI](https://img.shields.io/pypi/v/immutabledict) ![Conda](https://img.shields.io/conda/vn/conda-forge/immutabledict) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/immutabledict)

![License](https://img.shields.io/pypi/l/immutabledict) ![Build](https://img.shields.io/github/actions/workflow/status/corenting/immutabledict/ci.yml?branch=master) ![Codecov](https://img.shields.io/codecov/c/github/corenting/immutabledict) ![PyPI - Downloads](https://img.shields.io/pypi/dm/immutabledict)

An immutable wrapper around dictionaries. immutabledict implements the complete mapping interface and can be used as a drop-in replacement for dictionaries where immutability is desired.

It's a fork of slezica's [frozendict](https://github.com/slezica/python-frozendict). This library is a pure Python, MIT-licensed alternative to the new LGPL-3.0 licensed [frozendict](https://github.com/Marco-Sulla/python-frozendict).

## Installation

Official release in [on pypi](https://pypi.org/project/immutabledict/) as `immutabledict`.

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

## Donations

If you wish to support the app, donations are possible [here](https://corenting.fr/donate).
