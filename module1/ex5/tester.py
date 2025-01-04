from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


def display_image(array: np.ndarray) -> np.ndarray:
    plt.imshow(Image.fromarray(array))
    plt.show()


original = ft_load("landscape.jpg")

inverted = ft_invert(original)
reded = ft_red(original)
greened = ft_green(original)
blueded = ft_blue(original)
greyed = ft_grey(original)


print("original image with no effects")
display_image(original)
print(ft_invert.__doc__)
display_image(inverted)
print(ft_red.__doc__)
display_image(reded)
print(ft_green.__doc__)
display_image(greened)
print(ft_blue.__doc__)
display_image(blueded)
print(ft_grey.__doc__)
display_image(greyed)
