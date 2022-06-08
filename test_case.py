from main import *


def test_square_pairs():
    square_list = get_square_pairs((1, 1), (2, 3), (2,), (2,))
    assert square_list == [(1, 1), (1, 1), (2, 4), (3, 27), (2, 4), (2, 4)]
    square_list = get_square_pairs((1, 1, 5), (2, 3, 3), (2,), (2,))
    assert square_list == [(1, 1), (1, 1), (5, 3125), (2, 4), (3, 27), (3, 27), (2, 4), (2, 4)]

def test_uniq_list():
    square_list = get_square_pairs((1, 1), (2, 3), (2,), (2,))
    assert square_list == [(1, 1), (1, 1), (2, 4), (3, 27), (2, 4), (2, 4)]
    uniq_list = uniq_square(square_list)
    assert uniq_list == [1, 4, 27, 4]