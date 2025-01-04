from load_image import ft_load
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


GRAYSCALE_WEIGHT = [0.2989, 0.5870, 0.1140]


def zoom(img_lst: np.ndarray) -> np.ndarray:
    """zoom on image and grayscale it"""
    zoomed_lst = img_lst[100:500, 450:850]
    return np.dot(zoomed_lst, GRAYSCALE_WEIGHT)


def rotate(img_lst: np.ndarray) -> np.ndarray:
    """rotate image"""
    rows, cols = img_lst.shape
    rotated_lst = np.array([
        [img_lst[row][col] for row in range(rows)] for col in range(cols)
    ])
    return rotated_lst


def format_row(row):
    """format a single row."""
    formatted = (
        '[' +
        ' '.join(f"{int(x)}" for x in row[:3]) +
        ' ... ' +
        ' '.join(f"{int(x)}" for x in row[-3:]) +
        ']'
    )
    return formatted


def custom_print(arr):
    """Display summarized version of large arrays."""
    print('[' + format_row(arr[0]))
    print('  ...')
    print(' ' + format_row(arr[-1]) + ']')


def main():
    """zoom in on the image, convert it to grayscale, and finally rotate it"""
    img_lst = ft_load("animal.jpeg")
    if img_lst is None:
        print("AssertionError: failed to load image")
        return

    try:
        zoomed_lst = zoom(img_lst)
    except Exception:
        print("Image zoom failed")

    zoomed3d_lst = zoomed_lst[..., np.newaxis]

    np.set_printoptions(
        threshold=6,
        formatter=dict(float=lambda x: f"{int(x)}")
    )
    print("The shape of the image is:",
          zoomed_lst.shape,
          "or",
          zoomed3d_lst.shape)
    print(zoomed3d_lst[:1])

    try:
        rotated_lst = rotate(zoomed_lst)
    except Exception:
        print("Image rotation failed")
    print("New shape after Transpose:", rotated_lst.shape)
    custom_print(rotated_lst)

    # display final image
    plt.imshow(Image.fromarray(rotated_lst))
    plt.axis('on')
    plt.show()


if __name__ == "__main__":
    main()
