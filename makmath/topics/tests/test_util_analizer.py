import pytest
from topics.utils import *


# Analizator testing

@pytest.mark.parametrize("character, alphabet, expected",
                         [('3', ALPHABET, True),
                          ('h', ALPHABET, True), ])
def test_is_in_alphabet(character, alphabet, expected):
    assert Analizator.is_in_alphabet(character, alphabet) == expected


@pytest.mark.parametrize("text, min_length, max_length, expected",
                         [
                             ("hello", 6, 10, False),
                             ('aaaa', 5, 10, False),
                             ('', 0, 10, True),
                             ("0567", 4, 10, True),
                             ("0$№5670$№567", 4, 10, False)])
def test_is_correct_string(text, min_length, max_length, expected):
    assert Analizator.is_correct_string(text, min_length,
                                        max_length) == expected


@pytest.mark.parametrize("data, expected",
                         [
                             (['2', '3', '1'], ['1', '2', '3']),
                             (['333', '22', '1'], ['1', '22', '333']),
                             ([], []),
                             ([1, 2, 3, 5], [1, 2, 3, 5]),
                             ([1, 82, 3, -5], [-5, 1, 3, 82]),
                         ])
def test_insertion_sort(data, expected):
    assert Analizator.insertion_sort(data) == expected


@pytest.mark.parametrize("value, array, expected",
                         [
                             ('hello', [2, 'hello', 23], 1),
                             ('4', '123456sfdg', 3),
                             (8, [], None),
                             (10, [1, 2, 3, 5], None),
                             (1, [1, 82, 3, -5], 0),
                         ])
def test_find_index_of_value_in_array(value, array, expected):
    assert Analizator.find_index_of_value_in_array(value, array) == expected
