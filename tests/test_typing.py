# pyright: reportUnnecessaryTypeIgnoreComment=true
"""Typing tests for immutabledict, validated via ``make style`` (pyright).

``reportUnnecessaryTypeIgnoreComment=true`` (above) ensures that
``# type: ignore`` comments stay necessary, i.e. the suppressed
errors are genuinely produced.
"""

from typing import ItemsView, KeysView, ValuesView

from immutabledict import ImmutableOrderedDict, immutabledict


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

    def test_getitem_returns_value_type(self) -> None:
        d: immutabledict[str, int] = immutabledict(a=1)
        _v: int = d["a"]

    def test_view_types(self) -> None:
        d: immutabledict[str, int] = immutabledict(a=1, b=2)
        _k: KeysView[str] = d.keys()
        _vals: ValuesView[int] = d.values()
        _itms: ItemsView[str, int] = d.items()

    def test_iteration_yields_key_type(self) -> None:
        d: immutabledict[str, int] = immutabledict(a=1)
        for key in d:
            _k: str = key

    def test_mutation_methods_return_immutabledict(self) -> None:
        d: immutabledict[str, int] = immutabledict(a=1, b=2)
        _d_set: immutabledict[str, int] = d.set("c", 3)
        _d_del: immutabledict[str, int] = d.delete("a")
        _d_upd: immutabledict[str, int] = d.update({"c": 3})
        _d_disc: immutabledict[str, int] = d.discard("a")
        _d_copy: immutabledict[str, int] = d.copy()

    def test_or_returns_immutabledict(self) -> None:
        d: immutabledict[str, int] = immutabledict(a=1, b=2)
        _d_or: immutabledict[str, int] = d | {"c": 3}


class TestImmutableOrderedDictTyping:
    def test_construct_mapping(self) -> None:
        _d: ImmutableOrderedDict[str, int] = ImmutableOrderedDict({"a": 1})

    def test_construct_kwargs(self) -> None:
        _d: ImmutableOrderedDict[str, int] = ImmutableOrderedDict(a=1, b=2)

    def test_construct_wrong_value_kwargs(self) -> None:
        _d: ImmutableOrderedDict[str, int] = ImmutableOrderedDict(a="oops")  # type: ignore[arg-type]

    def test_construct_wrong_value_mapping(self) -> None:
        _d: ImmutableOrderedDict[str, int] = ImmutableOrderedDict({"a": "oops"})  # type: ignore[arg-type]
