# Changelog

## Version 4.3.0

- Add typed `__new__` overloads for type-safe constructor calls. Thanks to [@mfigurnov](https://github.com/mfigurnov) for the [PR](https://github.com/corenting/immutabledict/pull/418).
- Fix: correct ImmutableOrderedDict _dict_cls so that it works correctly. It actually silently used plain `dict` due to the issue (which actually do preserve order on Python 3.7+, so the bug was not noticed). Thanks to [@mfigurnov](https://github.com/mfigurnov) for the [PR](https://github.com/corenting/immutabledict/pull/418).

## Version 4.2.2

No code changes.

- Update classifiers, Github Actions... for Python 3.14
- Update metadatas for PEP 639

## Version 4.2.1

- Published with attestation
- Update classifiers, Github Actions... for Python 3.13 (no code changes)

## Version 4.2.0

- Add `discard` method which return a new immutabledict without the item at the given key, if present. Thanks to [@matthiasdiener](https://github.com/matthiasdiener) for the [PR #307](https://github.com/corenting/immutabledict/pull/307)

## Version 4.1.0

- Do not store cached hash value when pickling. Thanks to [@matthiasdiener](https://github.com/matthiasdiener) for the [PR #287](https://github.com/corenting/immutabledict/pull/287)

## Version 4.0.0

- Replace `__init__` by `__new__`. Thanks to [@spacether](https://github.com/spacether) for the [PR #263](https://github.com/corenting/immutabledict/pull/263)
- Add explicit items()/keys()/values() methods to speedup these methods. Thanks to [@matthiasdiener](https://github.com/matthiasdiener) for the [PR #265](https://github.com/corenting/immutabledict/pull/265)
- Add set/delete/update functions. Thanks to [@matthiasdiener](https://github.com/matthiasdiener) for the [PR #271](https://github.com/corenting/immutabledict/pull/271)
- Add documentation at [immutabledict.corenting.fr](https://immutabledict.corenting.fr)

## Version 3.0.0

- `copy()` (**breaking change**): remove the option to pass keyword arguments (which were present as key/value pairs in the copy). Now the method doesn't take any arguments (it behaves the same as a normal `dict`).
- Python versions: drop Python 3.7 support
- Typing: fixes
  - Make the key covariant. Thanks to [@spacether](https://github.com/spacether) for the [PR #244](https://github.com/corenting/immutabledict/pull/244)
  - Fix key/value typing missing for ImmutableOrderedDict

## Version 2.2.5

- Fix hard-coded class reference in fromkeys() resulting in always using `dict` for `fromkeys()` (instead of OrderedDict in ImmutableOrderedDict for example). Thanks to [@cthoyt](https://github.com/cthoyt) for the [PR #234](https://github.com/corenting/immutabledict/pull/234)

## Version 2.2.4

- Include tests in sdist for easier packaging

## Version 2.2.3

- Fix TypeError message when using `|=`. Thanks to [@ronshapiro](https://github.com/ronshapiro) for the [PR #66](https://github.com/corenting/immutabledict/pull/66)
- Update docstring for ImmutableOrderedDict to indicate that is not needed anymore for Python >= 3.7 but kept for compatibility purposes
- Use postponed evaluation of annotations ([PEP 563](https://peps.python.org/pep-0563/)) for the typing

## Version 2.2.2

- Update classifiers, Github Actions... for Python 3.11 (no code changes)

## Version 2.2.1

- Update classifiers, Github Actions... for Python 3.10 (no code changes)

## Version 2.2.0

- Use `poetry-core` instead of poetry for build-system. Thanks to [@mweinelt](https://github.com/mweinelt) for reporting [the issue](https://github.com/corenting/immutabledict/issues/56).

## Version 2.1.0

- Fix type annotation on keyword argument in copy(**add_or_replace). Thanks to [@techsy730](https://github.com/techsy730) for the [PR #54](https://github.com/corenting/immutabledict/pull/54).

## Version 2.0.0

- Support more typing (fix [issue #47](https://github.com/corenting/immutabledict/issues/47))
- ⚠️ Remove `*args, **kwargs` from the `fromkeys()` method.

## Version 1.3.0

- Add typing. Thanks to [@aecay](https://github.com/aecay) for the [PR #45](https://github.com/corenting/immutabledict/pull/45).

## Version 1.2.0

- Support [PEP 584 union operators](https://www.python.org/dev/peps/pep-0584/). Thanks to [@lambdalisue](https://github.com/lambdalisue) for the [PR #34](https://github.com/corenting/immutabledict/pull/34).

## Version 1.1.0

- Add Python 3.9 to supported versions, remove Python 3.5
- Bump dev dependencies
- Improve README

## Version 1.0.0

- Initial stable release
