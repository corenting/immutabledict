# pyright: reportUnnecessaryTypeIgnoreComment=true
"""Typing tests for immutabledict, validated via ``make style`` (pyright + pyrefly).

``reportUnnecessaryTypeIgnoreComment=true`` (above) ensures that
``# type: ignore`` comments stay necessary, i.e. the suppressed
errors are genuinely produced.
"""

from typing import Any, ItemsView, KeysView, Union, ValuesView

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

    def test_construct_heterogeneous_kwargs(self) -> None:
        # Any because **kwargs uses Any for pytype/pyrefly compat
        _d: immutabledict[str, Any] = immutabledict(a=1, b="hello")

    def test_construct_heterogeneous_kwargs_three_types(self) -> None:
        # Any because **kwargs uses Any for pytype/pyrefly compat
        _d: immutabledict[str, Any] = immutabledict(a=1, b="hello", c=True)

    def test_construct_heterogeneous_mapping(self) -> None:
        _d: immutabledict[str, Union[int, str]] = immutabledict({"a": 1, "b": "hello"})

    def test_construct_heterogeneous_iterable(self) -> None:
        _d: immutabledict[str, Union[int, str]] = immutabledict(
            [("a", 1), ("b", "hello")]
        )

    def test_construct_heterogeneous_keys_mapping(self) -> None:
        _d: immutabledict[Union[int, str], str] = immutabledict({1: "a", "b": "c"})

    def test_construct_heterogeneous_mapping_and_kwargs(self) -> None:
        _d: immutabledict[str, Union[int, str]] = immutabledict(
            {"a": 1, "b": "hello"}, c=2
        )

    def test_construct_heterogeneous_iterable_and_kwargs(self) -> None:
        _d: immutabledict[str, Union[int, str]] = immutabledict(
            [("a", 1), ("b", "hello")], c=2
        )

    def test_construct_wrong_heterogeneous_mapping(self) -> None:
        _d: immutabledict[str, int] = immutabledict({"a": 1, "b": "oops"})  # type: ignore[arg-type, dict-item]

    def test_construct_wrong_value_mapping(self) -> None:
        _d: immutabledict[str, int] = immutabledict({"a": "oops"})  # type: ignore[arg-type, dict-item]

    def test_construct_wrong_value_iterable(self) -> None:
        _d: immutabledict[str, int] = immutabledict([("a", "oops")])  # type: ignore[arg-type, list-item]

    def test_fromkeys(self) -> None:
        _d: immutabledict[str, int] = immutabledict.fromkeys(["a", "b"], 0)

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
    def test_construct_empty(self) -> None:
        _d: ImmutableOrderedDict[str, int] = ImmutableOrderedDict()

    def test_construct_mapping(self) -> None:
        _d: ImmutableOrderedDict[str, int] = ImmutableOrderedDict({"a": 1})

    def test_construct_kwargs(self) -> None:
        _d: ImmutableOrderedDict[str, int] = ImmutableOrderedDict(a=1, b=2)

    def test_construct_iterable(self) -> None:
        _d: ImmutableOrderedDict[str, int] = ImmutableOrderedDict([("a", 1)])

    def test_construct_mapping_and_kwargs(self) -> None:
        _d: ImmutableOrderedDict[str, int] = ImmutableOrderedDict({"a": 1}, b=2)

    def test_construct_iterable_and_kwargs(self) -> None:
        _d: ImmutableOrderedDict[str, int] = ImmutableOrderedDict([("a", 1)], b=2)

    def test_construct_heterogeneous_kwargs(self) -> None:
        # Any because **kwargs uses Any for pytype/pyrefly compat
        _d: ImmutableOrderedDict[str, Any] = ImmutableOrderedDict(a=1, b="hello")

    def test_construct_wrong_value_mapping(self) -> None:
        _d: ImmutableOrderedDict[str, int] = ImmutableOrderedDict({"a": "oops"})  # type: ignore[arg-type, dict-item]
