"""
Внимательно прочитайте код в этом файле и добавьте свой код везде, где встречается <YOUR CODE>.
Перед каждым заданием вы можете прочитать его описание, помеченное меткой TODO.
для проверки введите из папки с проектом: pytest -m task_5
"""
from typing import Any, Union, Optional


def add_new_elem(container: list, new_data: Any) -> Optional[int]:
    # TODO: добавьте в конец списока container новый элемент со значением переменной new_data
    #  запишите в переменную result значение нового размера списка

    result = None

    "<YOUR CODE>"

    return result


def change_elem(container: list, index: int, new_data: Any) -> Optional[int]:
    # TODO: измените в списке container элемент под индексом index на значение переменной new_data
    #  старое значение запишите в переменную result
    #  если new_data имеет тип, отличный от int - не выполняйте замену значения и не записывайте ничего в result.

    result = None

    "<YOUR CODE>"

    return result


def remove_even_elems(container: list) -> None:
    # TODO: удалите из списка container каждый элемент, значение которого будет четным.
    #  Размер списка после удаления одного элемента уменьшается на 1.
    #  После удаления по индексу index будет находиться элемент, ранее находившийся на позиции index + 1

    "<YOUR CODE>"


def get_sub_dict_elem(container: dict, key: str, subkey: Union[str, int]) -> Optional[int]:
    # TODO: получите из подсловаря словаря container по ключу key элемент по ключу subkey.
    #  Запишите его в переменную result
    result = None

    result = "<YOUR CODE>"

    return result

