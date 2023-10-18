from typing import Any, Dict, Union

import pytest

from immutabledict import ImmutableOrderedDict, immutabledict


class TestImmutableDict:
    def test_covariance(self) -> None:
        """Not a real unit test, but test covariance
        as mypy runs on the tests.
        """

        class Base:
            pass

        class One(Base):
            pass

        class Two(Base):
            pass

        # Value test
        my_dict: immutabledict[str, Union[Base, One]] = immutabledict()
        second_dict: immutabledict[str, Two] = immutabledict({"t": Two()})
        my_dict = second_dict
        assert my_dict == second_dict

    def test_new_init_methods(self) -> None:
        assert "__new__" in immutabledict.__dict__
        assert "__init__" not in immutabledict.__dict__

    def test_cannot_assign_value(self) -> None:
        with pytest.raises(AttributeError):
            immutabledict().setitem("key", "value")  # type: ignore

    def test_from_keys(self) -> None:
        keys = ["a", "b", "c"]
        immutable_dict: immutabledict[str, Any] = immutabledict.fromkeys(keys)
        assert "a" in immutable_dict
        assert "b" in immutable_dict
        assert "c" in immutable_dict

    def test_init_and_compare(self) -> None:
        normal_dict = {"a": "value", "b": "other_value"}
        immutable_dict: immutabledict[str, str] = immutabledict(normal_dict)
        assert immutable_dict == normal_dict

    def test_get_existing(self) -> None:
        immutable_dict: immutabledict[str, str] = immutabledict({"a": "value"})
        assert immutable_dict["a"] == "value"

    def test_get_not_existing(self) -> None:
        immutable_dict: immutabledict[str, str] = immutabledict({"a": "value"})
        with pytest.raises(KeyError):
            immutable_dict["b"]

    def test_contains(self) -> None:
        immutable_dict: immutabledict[str, str] = immutabledict({"a": "value"})
        assert "a" in immutable_dict

    def test_contains_not_existing(self) -> None:
        immutable_dict: immutabledict[str, str] = immutabledict({"a": "value"})
        assert "b" not in immutable_dict

    def test_copy(self) -> None:
        original: immutabledict[str, str] = immutabledict({"a": "value"})
        copy = original.copy()
        assert original == copy
        assert id(original) != id(copy)

    def test_iter(self) -> None:
        immutable_dict: immutabledict[str, str] = immutabledict(
            {"a": "value", "b": "other_value"}
        )
        itered_keys = set(immutable_dict)
        assert immutable_dict.keys() == itered_keys

    def test_len(self) -> None:
        immutable_dict: immutabledict[str, str] = immutabledict(
            {"a": "value", "b": "other_value"}
        )
        assert len(immutable_dict) == 2

    def test_len_empty(self) -> None:
        immutable_dict: immutabledict[str, str] = immutabledict({})
        assert len(immutable_dict) == 0

    def test_repr(self) -> None:
        immutable_dict: immutabledict[str, str] = immutabledict(
            {"a": "value", "b": "other_value"}
        )
        repr_ret = repr(immutable_dict)
        assert repr_ret.startswith("immutabledict")
        assert repr_ret.endswith(")")

    def test_repr_should_eval(self) -> None:
        immutable_dict: immutabledict[str, str] = immutabledict(
            {"a": "value", "b": "other_value"}
        )
        eval_ret = eval(repr(immutable_dict))  # noqa: S307
        assert immutable_dict == eval_ret

    def test_hash(self) -> None:
        first_dict: immutabledict[str, str] = immutabledict(
            {"a": "value", "b": "other_value"}
        )
        second_dict: immutabledict[str, str] = immutabledict(
            {"a": "value", "b": "other_value"}
        )

        assert hash(first_dict) == hash(second_dict)

    def test_union_operator_merge(self) -> None:
        first_dict: immutabledict[str, str] = immutabledict({"a": "a", "b": "b"})
        second_dict: immutabledict[str, str] = immutabledict({"a": "A", "c": "c"})
        merged_dict = first_dict | second_dict
        assert isinstance(merged_dict, immutabledict)
        assert merged_dict == {
            "a": "A",
            "b": "b",
            "c": "c",
        }
        assert first_dict == {"a": "a", "b": "b"}
        assert second_dict == {"a": "A", "c": "c"}

    def test_union_operator_merge_with_dict_first(self) -> None:
        first_dict: Dict[str, str] = dict({"a": "a", "b": "b"})
        second_dict: immutabledict[str, str] = immutabledict({"a": "A", "c": "c"})
        merged_dict = first_dict | second_dict
        assert isinstance(merged_dict, dict)
        assert merged_dict == {
            "a": "A",
            "b": "b",
            "c": "c",
        }
        assert first_dict == {"a": "a", "b": "b"}
        assert second_dict == {"a": "A", "c": "c"}

    def test_union_operator_merge_with_dict_second(self) -> None:
        first_dict: immutabledict[str, str] = immutabledict({"a": "a", "b": "b"})
        second_dict: Dict[str, str] = dict({"a": "A", "c": "c"})
        merged_dict = first_dict | second_dict
        assert isinstance(merged_dict, immutabledict)
        assert merged_dict == {
            "a": "A",
            "b": "b",
            "c": "c",
        }
        assert first_dict == {"a": "a", "b": "b"}
        assert second_dict == {"a": "A", "c": "c"}

    def test_union_operator_merge_fail(self) -> None:
        first_dict: immutabledict[str, str] = immutabledict({"a": "a", "b": "b"})

        with pytest.raises(TypeError):
            first_dict | 0

        with pytest.raises(TypeError):
            0 | first_dict

    def test_union_operator_update(self) -> None:
        first_dict: immutabledict[str, str] = immutabledict({"a": "a", "b": "b"})
        second_dict: immutabledict[str, str] = immutabledict({"a": "A", "c": "c"})

        with pytest.raises(TypeError):
            first_dict |= second_dict

    def test_union_operator_update_with_dict_first(self) -> None:
        first_dict: Dict[str, str] = dict({"a": "a", "b": "b"})
        second_dict: immutabledict[str, str] = immutabledict({"a": "A", "c": "c"})

        first_dict |= second_dict
        assert isinstance(first_dict, dict)
        assert first_dict == {
            "a": "A",
            "b": "b",
            "c": "c",
        }
        assert second_dict == {"a": "A", "c": "c"}

    def test_union_operator_update_with_dict_second(self) -> None:
        first_dict: immutabledict[str, str] = immutabledict({"a": "a", "b": "b"})
        second_dict: Dict[str, str] = dict({"a": "A", "c": "c"})

        with pytest.raises(TypeError):
            first_dict |= second_dict
        assert isinstance(first_dict, immutabledict)
        assert first_dict == {"a": "a", "b": "b"}
        assert second_dict == {"a": "A", "c": "c"}

    @pytest.mark.parametrize(
        "statement",
        [
            "for k, v in d.items(): s += 1",
            "for v in d.values(): s += 1",
            "for k in d.keys(): s += 1",
        ],
    )
    def test_performance(self, statement: str) -> None:
        from timeit import timeit

        time_standard = timeit(
            statement,
            number=3,
            setup="s=0; d = {i:i for i in range(1000000)}",
        )

        time_immutable = timeit(
            statement,
            globals=globals(),
            number=3,
            setup="s=0; d = immutabledict({i:i for i in range(1000000)})",
        )

        assert time_immutable < 1.2 * time_standard

    def test_set_delete_update(self) -> None:
        d: immutabledict[str, int] = immutabledict(a=1, b=2)

        assert d.set("a", 10) == immutabledict(a=10, b=2) == dict(a=10, b=2)
        assert d.delete("a") == immutabledict(b=2) == dict(b=2)

        with pytest.raises(KeyError):
            d.delete("c")

        assert d.update({"a": 3}) == immutabledict(a=3, b=2) == dict(a=3, b=2)

        assert (
            d.update({"c": 17}) == immutabledict(a=1, b=2, c=17) == dict(a=1, b=2, c=17)
        )

        # Make sure d doesn't change
        assert d == immutabledict(a=1, b=2) == dict(a=1, b=2)

    def test_new_kwargs(self) -> None:
        immutable_dict: immutabledict[str, int] = immutabledict(a=1, b=2)
        assert immutable_dict == {"a": 1, "b": 2} == dict(a=1, b=2)


class TestImmutableOrderedDict:
    def test_ordered(self) -> None:
        ordered: ImmutableOrderedDict[str, str] = ImmutableOrderedDict(
            {
                "a": "1",
                "b": "2",
                "c": "3",
            }
        )
        itered_keys = list(ordered)
        assert itered_keys[0] == "a"
        assert itered_keys[1] == "b"
        assert itered_keys[2] == "c"
