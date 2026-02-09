# pyright: reportUnnecessaryTypeIgnoreComment=true
"""Typing tests for immutabledict, validated via ``make style`` (pyright).

``reportUnnecessaryTypeIgnoreComment=true`` (above) ensures that
``# type: ignore`` comments stay necessary, i.e. the suppressed
errors are genuinely produced.
"""

from immutabledict import immutabledict


class TestImmutableDictTyping:
    def test_construct_empty(self) -> None:
        _d: immutabledict[str, int] = immutabledict()

    def test_construct_kwargs(self) -> None:
        _d: immutabledict[str, int] = immutabledict(a=1, b=2)

    def test_construct_mapping(self) -> None:
        _d: immutabledict[str, int] = immutabledict({"a": 1})

    def test_construct_mapping_and_kwargs(self) -> None:
        _d: immutabledict[str, int] = immutabledict({"a": 1}, b=2)

    def test_construct_iterable(self) -> None:
        _d: immutabledict[str, int] = immutabledict([("a", 1)])

    def test_construct_iterable_and_kwargs(self) -> None:
        _d: immutabledict[str, int] = immutabledict([("a", 1)], b=2)

    def test_construct_wrong_value_kwargs(self) -> None:
        _d: immutabledict[str, int] = immutabledict(a="oops")  # type: ignore[arg-type]

    def test_construct_wrong_value_mapping(self) -> None:
        _d: immutabledict[str, int] = immutabledict({"a": "oops"})  # type: ignore[arg-type]

    def test_construct_wrong_kwarg_with_mapping(self) -> None:
        _d: immutabledict[str, int] = immutabledict({"a": 1}, b="oops")  # type: ignore[arg-type]

    def test_construct_wrong_value_iterable(self) -> None:
        _d: immutabledict[str, int] = immutabledict([("a", "oops")])  # type: ignore[arg-type]

    def test_construct_wrong_kwarg_with_iterable(self) -> None:
        _d: immutabledict[str, int] = immutabledict([("a", 1)], b="oops")  # type: ignore[arg-type]
