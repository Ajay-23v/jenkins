import pytest
from App import sum_list, count_negatives

@pytest.mark.parametrize("numbers, expected", [
    ([], 0),
    ([1, 2, 3], 6),
    ([-1, -2, -3], -6),
    ([2.5, 2.5], 5.0)
])
def test_sum_list(numbers, expected):
    assert sum_list(numbers) == expected

@pytest.mark.parametrize("numbers, expected", [
    ([], 0),
    ([1, 2, 3], 0),
    ([-1, 2, -3], 2),
    ([-5, -10], 1)
])
def test_count_negatives(numbers, expected):
    assert count_negatives(numbers) == expected
