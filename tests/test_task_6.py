import pytest
import random as rnd
import tasks.task_6 as task_6


@pytest.mark.task_6
def test_add_value():
    text_data = [
        "asd",
        'azxc',
        'vev',
        'ewgvsd',
        'qer32tf43g'
    ]
    task_6.data.clear()
    for i in range(100):
        first = rnd.randint(0, 199)
        second = text_data[rnd.randint(0, len(text_data) - 1)]
        third = None if first >= 100 else True
        task_6.add_value(first)
        task_6.add_value(second)
        task_6.add_value(third)
        assert task_6.data[i * 3 + 0] == first
        assert task_6.data[i * 3 + 1] == second
        assert task_6.data[i * 3 + 2] == third
    task_6.data.clear()


@pytest.mark.task_6
def test_sum_values():

    res = task_6.sum_values(1, 2, 3, 4)
    assert res == (1 + 2 + 3 + 4, 4)

    numbers = [(rnd.randint(0, 100)) ** 2 for x in range(1000) if x % 2 == 0]
    for i in range(100):
            count = rnd.randint(3, len(numbers) - 1)
            sample = rnd.sample(numbers, count)
            test_sum, test_count = task_6.sum_values(*sample)
            assert test_count == count
            assert sum(sample) == test_sum

