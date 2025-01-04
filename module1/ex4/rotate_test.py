import numpy as np
from matplotlib import pyplot as plt
from load_image import ft_load
from PIL import Image

GRAYSCALE = [0.2989, 0.5870, 0.1140]


def zoom(img: np.ndarray) -> np.ndarray:
    """Slice and grayscale the image."""

    sliced = img[100:500, 450:850]

    # [..., :3] used to remove the alpha channel if it exists
    gray = np.dot(sliced[..., :3], GRAYSCALE)

    return gray


def rotate(img: np.ndarray) -> np.ndarray:
    """Transpose the image."""

    rows, cols = img.shape
    transposed = [[img[j][i] for j in range(rows)] for i in range(cols)]

    return np.array(transposed)


def format_row(row):
    """Helper function to format a single row."""

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
    """
    Main function that loads an image, slices it, converts it to grayscale,
    rotates it and displays the final image.
    """

    img = ft_load("animal.jpeg")

    try:
        assert img is not None
    except AssertionError:
        print("Image loading failed.")
        return

    try:
        zoomed = zoom(img)
    except Exception as e:
        print(f"Image zooming failed: {e}")
        return

    # [..., np.newaxis] used to add new axis to the array
    gray_3D = zoomed[..., np.newaxis]

    # Set the ellipsis threshold to 6, and floats as integers
    np.set_printoptions(
        threshold=6,
        formatter=dict(float=lambda x: f"{x:.0f}")
    )
    print(f"The shape of the image is: {gray_3D.shape} or {zoomed.shape}")
    print(gray_3D[:1])

    try:
        rotated = rotate(zoomed)
    except Exception as e:
        print(f"Image rotating failed: {e}")
        return

    np.set_printoptions(
        threshold=1,
        formatter=dict(float=lambda x: f"{x:.0f}")
    )
    print(f"New shape after Transpose: {rotated.shape}")
    custom_print(rotated)

    plt.imshow(Image.fromarray(rotated))
    plt.axis('on')
    plt.show()


if __name__ == "__main__":
    main()
