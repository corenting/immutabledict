import pytest

from immutabledict import ImmutableOrderedDict, immutabledict


class TestImmutableDict:
    def test_cannot_assign_value(self):
        with pytest.raises(AttributeError):
            immutabledict().setitem('key', 'value')

    def test_init_and_compare(self):
        normal_dict = {
            'a': 'value',
            'b': 'other_value'
        }
        immutable_dict = immutabledict(normal_dict)
        assert immutable_dict == normal_dict

    def test_get_existing(self):
        immutable_dict = immutabledict({ 'a': 'value' })
        assert immutable_dict['a'] == 'value'

    def test_get_not_existing(self):
        immutable_dict = immutabledict({ 'a': 'value' })
        with pytest.raises(KeyError):
            test_get = immutable_dict['b']

    def test_contains(self):
        immutable_dict = immutabledict({ 'a': 'value' })
        assert 'a' in immutable_dict

    def test_contains_not_existing(self):
        immutable_dict = immutabledict({ 'a': 'value' })
        assert 'b' not in immutable_dict
