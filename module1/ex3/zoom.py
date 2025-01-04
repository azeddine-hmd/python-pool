from load_image import ft_load
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


GRAYSCALE_WEIGHT = [0.2989, 0.5870, 0.1140]


def zoom(img_lst: np.ndarray) -> np.ndarray:
    """zoom on image and display it"""
    zoomed_lst = img_lst[100:500, 450:850]
    grayscaled2d_lst = np.dot(zoomed_lst, GRAYSCALE_WEIGHT)
    grayscaled3d_lst = grayscaled2d_lst[..., np.newaxis]
    print("New shape after slicing:",
          grayscaled3d_lst.shape,
          "or",
          grayscaled2d_lst.shape)

    np.set_printoptions(
        threshold=6,
        formatter=dict(float=lambda x: f"{int(x)}")
    )
    print(grayscaled3d_lst[:1])
    plt.imshow(Image.fromarray(grayscaled2d_lst))
    plt.axis("on")
    plt.show()

    return grayscaled2d_lst


def main():
    """load image and zoom in"""
    img_lst = ft_load("animal.jpeg")
    if img_lst is None:
        print("AssertionError: failed to load image")
        return
    print(img_lst[:1])
    try:
        zoom(img_lst)
    except Exception:
        print("Image Zooming failed")


if __name__ == "__main__":
    main()
