import numpy as np
from numpy.typing import NDArray


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """Calculate BMI values from lists of height and weight
    """
    try:
        assert type(height) is list and type(weight) is list, \
            "type of height or weight is not list"
        assert len(height) == len(weight), \
            "height and weight are not same size"
        assert len(height) != 0 and len(weight) != 0, \
            "height or weight length is 0"
        try:
            weight_arr = np.array(weight, dtype=np.float64)
            height_arr = np.array(height, dtype=np.float64)
        except ValueError:
            raise AssertionError(
                "invalid element in hegiht or weight, it must be int or float"
            )
        assert np.all(height_arr > 0) and \
            np.all(weight_arr > 0), \
            "invalid number in height or weight, it must be positive"
        bmi: NDArray[np.float64] = weight_arr / (height_arr ** 2)
        return bmi.tolist()
    except AssertionError as e:
        print("AssertionError:", e)


def apply_limit(
    bmi: list[int | float],
    limit: int
) -> list[bool]:
    try:
        assert type(bmi) is list, \
            "type of bmi is not list"
        assert len(bmi) != 0, \
            "height or weight length is 0"
        try:
            bmi_arr = np.array(bmi, dtype=np.float64)
        except ValueError:
            raise AssertionError(
                "invalid element in bmi, it must be int or float"
            )
        result: NDArray[np.float64] = bmi_arr > limit
        return result.tolist()
    except AssertionError as e:
        print("AssertionError:", e)
