import pytest
import random as rnd
import tasks.task_5 as task_5


@pytest.mark.task_5
def test_add_new_elem():

    # TODO: добавьте в конец списока container новый элемент со значением переменной new_data
    #  запишите в переменную result значение нового размера списка

    size = 100
    data = [x for x in range(size)]
    rnd.shuffle(data)
    old_data = data.copy()
    new_data = rnd.randbytes(10)
    test_new_size = task_5.add_new_elem(data, new_data)
    assert test_new_size == size + 1
    assert data[-1] == new_data
    assert old_data == data[:size]


@pytest.mark.task_5
def test_change_elem():
    # TODO: измените в списке container элемент под индексом index на значение переменной new_data
    #  старое значение запишите в переменную result
    #  если new_data имеет тип, отличный от int - не выполняйте замену значения и не записывайте ничего в result.

    data = [x for x in range(100)]
    rnd.shuffle(data)
    new_data = 123
    index = rnd.randint(0, len(data) - 1)
    sample_old = data[index]
    old = task_5.change_elem(data, index, new_data)
    assert data[index] == new_data
    assert sample_old == old

    wrong_data = "new data"
    sample_old = data[index]
    old = task_5.change_elem(data, index, wrong_data)
    assert data[index] == sample_old
    assert old is None


@pytest.mark.task_5
def test_delete_elem():
    # TODO: удалите из списка container каждый элемент, значение которого будет четным.
    #  Размер списка после удаления одного элемента уменьшается на 1.
    #  После удаления по индексу index будет находиться элемент, ранее находившийся на позиции index + 1


    data = [x for x in range(100)]
    data.extend(data)
    old_size = len(data)
    rnd.shuffle(data)
    sample_data = data.copy()
    i = 0
    while i < len(sample_data):
        if sample_data[i] % 2 == 0:
            del sample_data[i]
            i -= 1
        i += 1
    task_5.remove_even_elems(data)
    assert data == data


def gen_key(index: int) -> str:
    return f"key {index}"


def gen_value(index: int) -> str:
    return f"value {index} {rnd.randint(0, 100)}"


@pytest.mark.task_5
def test_get_sub_dict_elem():
    # TODO: получите из подсловаря словаря container по ключу key элемент по ключу subkey.
    #  Запишите его в переменную result

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



