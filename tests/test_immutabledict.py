import pytest

from immutabledict import ImmutableOrderedDict, immutabledict


class TestImmutableDict:
    def test_covariance(self):
        assert immutabledict.__parameters__[0].__covariant__ is False
        assert immutabledict.__parameters__[1].__covariant__ is True

    def test_cannot_assign_value(self):
        with pytest.raises(AttributeError):
            immutabledict().setitem("key", "value")

    def test_copy(self):
        original = immutabledict({"a": "value"})
        copy = original.copy()
        assert original == copy
        assert id(original) != id(copy)


    def test_from_keys(self):
        keys = ("a", "b", "c")
        immutable_dict = immutabledict.fromkeys(keys)
        assert "a" in immutable_dict
        assert "b" in immutable_dict
        assert "c" in immutable_dict

    def test_init_and_compare(self):
        normal_dict = {"a": "value", "b": "other_value"}
        immutable_dict = immutabledict(normal_dict)
        assert immutable_dict == normal_dict

    def test_get_existing(self):
        immutable_dict = immutabledict({"a": "value"})
        assert immutable_dict["a"] == "value"

    def test_get_not_existing(self):
        immutable_dict = immutabledict({"a": "value"})
        with pytest.raises(KeyError):
            immutable_dict["b"]

    def test_contains(self):
        immutable_dict = immutabledict({"a": "value"})
        assert "a" in immutable_dict

    def test_contains_not_existing(self):
        immutable_dict = immutabledict({"a": "value"})
        assert "b" not in immutable_dict

    def test_iter(self):
        immutable_dict = immutabledict({"a": "value", "b": "other_value"})
        itered_keys = {x for x in immutable_dict}
        assert immutable_dict.keys() == itered_keys

    def test_len(self):
        immutable_dict = immutabledict({"a": "value", "b": "other_value"})
        assert len(immutable_dict) == 2

    def test_len_empty(self):
        immutable_dict = immutabledict({})
        assert len(immutable_dict) == 0

    def test_repr(self):
        immutable_dict = immutabledict({"a": "value", "b": "other_value"})
        repr_ret = repr(immutable_dict)
        assert repr_ret.startswith("immutabledict")
        assert repr_ret.endswith(")")

    def test_repr_should_eval(self):
        immutable_dict = immutabledict({"a": "value", "b": "other_value"})
        eval_ret = eval(repr(immutable_dict))
        assert immutable_dict == eval_ret

    def test_hash(self):
        first_dict = immutabledict({"a": "value", "b": "other_value"})
        second_dict = immutabledict({"a": "value", "b": "other_value"})

        assert hash(first_dict) == hash(second_dict)

    def test_union_operator_merge(self):
        first_dict = immutabledict({"a": "a", "b": "b"})
        second_dict = immutabledict({"a": "A", "c": "c"})
        merged_dict = first_dict | second_dict
        assert isinstance(merged_dict, immutabledict)
        assert merged_dict == {
            "a": "A",
            "b": "b",
            "c": "c",
        }
        assert first_dict == {"a": "a", "b": "b"}
        assert second_dict == {"a": "A", "c": "c"}

    def test_union_operator_merge_with_dict(self):
        first_dict = dict({"a": "a", "b": "b"})
        second_dict = immutabledict({"a": "A", "c": "c"})
        merged_dict = first_dict | second_dict
        assert isinstance(merged_dict, dict)
        assert merged_dict == {
            "a": "A",
            "b": "b",
            "c": "c",
        }
        assert first_dict == {"a": "a", "b": "b"}
        assert second_dict == {"a": "A", "c": "c"}

        first_dict = immutabledict({"a": "a", "b": "b"})
        second_dict = dict({"a": "A", "c": "c"})
        merged_dict = first_dict | second_dict
        assert isinstance(merged_dict, immutabledict)
        assert merged_dict == {
            "a": "A",
            "b": "b",
            "c": "c",
        }
        assert first_dict == {"a": "a", "b": "b"}
        assert second_dict == {"a": "A", "c": "c"}

    def test_union_operator_merge_fail(self):
        first_dict = immutabledict({"a": "a", "b": "b"})

        with pytest.raises(TypeError):
            first_dict | 0

        with pytest.raises(TypeError):
            0 | first_dict

    def test_union_operator_update(self):
        first_dict = immutabledict({"a": "a", "b": "b"})
        second_dict = immutabledict({"a": "A", "c": "c"})

        with pytest.raises(TypeError):
            first_dict |= second_dict

    def test_union_operator_update_with_dict(self):
        first_dict = dict({"a": "a", "b": "b"})
        second_dict = immutabledict({"a": "A", "c": "c"})

        first_dict |= second_dict
        assert isinstance(first_dict, dict)
        assert first_dict == {
            "a": "A",
            "b": "b",
            "c": "c",
        }
        assert second_dict == {"a": "A", "c": "c"}

        first_dict = immutabledict({"a": "a", "b": "b"})
        second_dict = dict({"a": "A", "c": "c"})

        with pytest.raises(TypeError):
            first_dict |= second_dict
        assert isinstance(first_dict, immutabledict)
        assert first_dict == {"a": "a", "b": "b"}
        assert second_dict == {"a": "A", "c": "c"}


class TestImmutableOrderedDict:
    def test_ordered(self):
        ordered = ImmutableOrderedDict(
            {
                "a": "1",
                "b": "2",
                "c": "3",
            }
        )
        itered_keys = [x for x in ordered]
        assert itered_keys[0] == "a"
        assert itered_keys[1] == "b"
        assert itered_keys[2] == "c"
