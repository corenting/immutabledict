import pytest

from immutabledict import ImmutableOrderedDict, immutabledict


class TestImmutableDict:
    def test_cannot_assign_value(self):
        with pytest.raises(AttributeError):
            immutabledict().setitem("key", "value")

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
            test_get = immutable_dict["b"]

    def test_contains(self):
        immutable_dict = immutabledict({"a": "value"})
        assert "a" in immutable_dict

    def test_contains_not_existing(self):
        immutable_dict = immutabledict({"a": "value"})
        assert "b" not in immutable_dict

    def test_copy(self):
        original = immutabledict({"a": "value"})
        copy = original.copy()
        assert original == copy

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
        assert repr_ret.startswith('<immutabledict')
        assert repr_ret.endswith('>')

    def test_hash(self):
        first_dict = immutabledict({"a": "value", "b": "other_value"})
        second_dict = immutabledict({"a": "value", "b": "other_value"})

        assert hash(first_dict) == hash(second_dict)

class ImmutableOrderedDict:

    def test_ordered(self):
        ordered = ImmutableOrderedDict()
        ordered['a'] = '1'
        ordered['b'] = '2'
        ordered['c'] = '3'
        itered_keys = {x for x in immutable_dict}
        assert itered_keys[0] == 'a'
        assert itered_keys[1] == 'b'
        assert itered_keys[2] == 'c'
