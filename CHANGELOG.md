# Version 2.2.0

- Use `poetry-core` instead of poetry for build-system. Thanks to [@mweinelt](https://github.com/mweinelt) for reporting [the issue](https://github.com/corenting/immutabledict/issues/56).
# Version 2.1.0

- Fix type annotation on keyword argument in copy(**add_or_replace). Thanks to [@techsy730](https://github.com/techsy730) for the [PR #54](https://github.com/corenting/immutabledict/pull/54).

# Version 2.0.0

- Support more typing (fix [issue #47](https://github.com/corenting/immutabledict/issues/47))
- ⚠️ Remove `*args, **kwargs` from the `fromkeys()` method.

# Version 1.3.0

- Add typing. Thanks to [@aecay](https://github.com/aecay) for the [PR #45](https://github.com/corenting/immutabledict/pull/45).

# Version 1.2.0

- Support [PEP 584 union operators](https://www.python.org/dev/peps/pep-0584/). Thanks to [@lambdalisue](https://github.com/lambdalisue) for the [PR #34](https://github.com/corenting/immutabledict/pull/34).

# Version 1.1.0

- Add Python 3.9 to supported versions, remove Python 3.5
- Bump dev dependencies
- Improve README

# Version 1.0.0

- Initial stable release
