import pytest
import random as rnd
import tasks.task_8 as task_8
import os


def gen_row_value(index: int) -> str:
    return f"data {index}"


def remove_file(path):
    if os.path.isfile(path):
        os.remove(path)


def read_file(path, data):
    data_iter = iter(data + data)
    with open(path, 'r', encoding='utf-8') as file:
        for test_row in data_iter:
            line = file.readline()
            # print(line)
            # for line in file:
            line = line.strip()
            #     test_row = next(data_iter)
            #     print(test_row)
            assert line == test_row


@pytest.fixture()
def getfile():
    if not os.path.isdir("Data"):
        os.mkdir("Data")
    path = "Data/test1.random_ext"
    yield path
    remove_file(path)


@pytest.fixture(params=[x for x in range(100)])
def rnd_filename(request):
    if not os.path.isdir("Data"):
        os.mkdir("Data")
    filename = f"filename {request.param}"
    yield filename
    remove_file(f"Data/{filename}")


@pytest.mark.task_8
def test_write_data(getfile):

    for i in range(10):
        remove_file(getfile)
        value_start = rnd.randint(0, 100)
        value_end = rnd.randint(value_start, value_start + 100)
        data = [gen_row_value(x) for x in range(value_start, value_end)]
        task_8.write_data(data)
        task_8.write_data(data)
        read_file(getfile, data)
        remove_file(getfile)


@pytest.mark.task_8
def test_find_data(rnd_filename):
    secret_subrow = "supersecretrow"
    rows = ["row " + str(x) for x in range(10)]

    rand_rows = [0] * rnd.randint(1, 9)
    for index in range(len(rand_rows)):
        rand_rows[index] = rnd.randint(0, len(rows) - 1)

    rand_rows = sorted(list(set(rand_rows)))
    for rand in rand_rows:
        rows[rand] += secret_subrow + 'asdcwe fdv'

    with open(f"Data/{rnd_filename}", 'w', encoding='utf-8') as file:
        file.writelines(list(map(lambda x: x + '\n', rows)))
    test_rows = task_8.find_data(rnd_filename, secret_subrow)

    for index, secret_rows_index in enumerate(rand_rows):
        assert rows[secret_rows_index] == test_rows[index]
    print(1)
    # remove_file(f"Data/{rnd_filename}")
