import numpy as np


def ft_invert(array: np.ndarray) -> np.ndarray:
    """invert the color of image"""
    return 255 - array


def ft_red(array: np.ndarray) -> np.ndarray:
    """image with only red channel"""
    new_array = array.copy()
    new_array[:, :, 1] = 0
    new_array[:, :, 2] = 0
    return new_array


def ft_green(array: np.ndarray) -> np.ndarray:
    """image with only green channel"""
    new_array = array.copy()
    new_array[:, :, 0] = 0
    new_array[:, :, 2] = 0
    return new_array


def ft_blue(array: np.ndarray) -> np.ndarray:
    """image with only blue channel"""
    new_array = array.copy()
    new_array[:, :, 0] = 0
    new_array[:, :, 1] = 0
    return new_array


def ft_grey(array: np.ndarray) -> np.ndarray:
    """grey the image"""
    new_array = array.copy()
    new_array[:, :, 0] = new_array[:, :, 1]
    new_array[:, :, 1] = new_array[:, :, 1]
    return new_array
