import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """create slice of 2d array and prints it's shape"""
    try:
        assert type(family) is list, "family must be a list"
        assert all(type(element) is list for element in family), \
            "elements of family must be list"
        assert family[0] is not None, \
            "family is not 2D array if no sub list found"
        first_row_len = len(family[0])
        assert all(len(row) == first_row_len for row in family), \
            "all sub lists must have same list length"
        assert all(
            all(isinstance(num, (int, float)) for num in row) for row in family
        ), "all element of sub lists must be int or float"
        assert type(start) is int and type(end) is int, \
            "start and end argument must be int or float"
        family_lst = np.array(family)
        assert family_lst.ndim == 2, "family must be a 2D array"
    except AssertionError as e:
        print("AssertionError:", e)
        return
    print("My shape is :", family_lst.shape)
    sliced_lst = family_lst[start:end]
    print("My new shape is :", sliced_lst.shape)
    return sliced_lst.tolist()
