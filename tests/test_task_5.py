import pytest
import random as rnd
import src.task_5 as task_5


@pytest.mark.task_5
def test_add_new_elem():

    data = [x for x in range(100)]
    rnd.shuffle(data)
    new_data = rnd.randbytes(10)
    task_5.add_new_elems(data, new_data)
    assert data[-1] == new_data


@pytest.mark.task_5
def test_change_elem():

    data = [x for x in range(100)]
    rnd.shuffle(data)
    new_data = "new data"
    index = rnd.randint(0, len(data) - 1)
    task_5.change_elem(data, index, new_data)
    assert data[-1] == new_data


@pytest.mark.task_5
def test_delete_elem():

    data = [x for x in range(100)]
    data.extend(data)
    old_size = len(data)
    rnd.shuffle(data)
    index = rnd.randint(0, len(data) - 1)
    old_value = data[index]
    task_5.delete_elem(data, index)
    assert len(data) == old_size - 1
    assert data[index] == data


def gen_key(index: int) -> str:
    return f"key {index}"


def gen_value(index: int) -> str:
    return f"value {index} {rnd.randint(0, 100)}"


@pytest.mark.task_5
def test_get_sub_dict_elem():

    temp_keys = [[gen_key(x), gen_value(x)] for x in range(100)]
    rnd.shuffle(temp_keys)

    container = dict(temp_keys[0: len(temp_keys) // 2])
    sub_container = dict(temp_keys[len(container):])

    key = temp_keys[rnd.randint(0, len(container) - 1)][0]
    sub_key = temp_keys[len(container) + rnd.randint(0, len(sub_container) - 1)][0]

    container[key] = sub_container

    copy_container = container.copy()
    res = task_5.get_sub_dict_elem(copy_container, key, sub_key)
    assert copy_container == container
    assert res == sub_container[sub_key]



