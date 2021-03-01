import pytest
import random as rnd
import src.task_7 as task_7


@pytest.mark.task_7
def test_gen_numbers():

    for i in range(100):
        numbers = (x for x in range(0, i**3) if x % 2 == 0)
        for test_number in task_7.gen_numbers(0, i**3, True):
            assert test_number == next(numbers)
            pass

        numbers = (x for x in range(0, i**3) if x % 2 == 1)
        for test_number in task_7.gen_numbers(0, i**3, False):
            assert test_number == next(numbers)
            pass
