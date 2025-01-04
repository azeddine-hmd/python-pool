from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """load image from a file and return RGB pixel data"""
    try:
        assert type(path) is str, "path must be string"
        img = Image.open(path)
        assert img.format == "JPEG", "Invalid image format"
        img_lst = np.array(img)
        img.close()
    except FileNotFoundError as e:
        print("AssertionError: file not found ", e.filename)
    except IOError:
        print("AssertionError: File is not valid image file")
    # print("The shape of the image is:", img_lst.shape)
    return img_lst
