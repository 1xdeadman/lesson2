import collections.abc as abc

import pytest
import random as rnd
import tasks.task_7 as task_7


@pytest.mark.task_7
def test_gen_numbers():
    print(type(task_7.gen_numbers(0, 10, True)))
    assert isinstance(task_7.gen_numbers(0, 10, True), abc.Generator)
    assert [0, 2, 4, 6, 8, 10] == list(task_7.gen_numbers(0, 10, True))

    for i in range(10):
        numbers = (x for x in range(0, i**3 + 1) if x % 2 == 0)
        for test_number in task_7.gen_numbers(0, i**3, True):
            assert test_number == next(numbers)
            pass

        numbers = (x for x in range(0, i**3 + 1) if x % 2 == 1)
        for test_number in task_7.gen_numbers(0, i**3, False):
            assert test_number == next(numbers)
            pass
