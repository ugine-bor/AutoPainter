import cv2
import numpy as np
import pickle

import getcoords


def fieldsize(FIELD):
    height = FIELD['END'][0] - FIELD['START'][0]
    width = FIELD['END'][1] - FIELD['START'][1]
    return width, height


def convertimage(imagepath, FIELD):
    gray_image = cv2.imread(imagepath, cv2.IMREAD_GRAYSCALE)

    print(f"Initial| width: {gray_image.shape[1]}, height: {gray_image.shape[0]}")
    if any([gray_image.shape[i] > fieldsize(FIELD)[i] for i in range(2)]):
        print("Image is too big. Resizing...")
        width, height = [fieldsize(FIELD)[i] if gray_image.shape[i] > fieldsize(FIELD)[i] else gray_image.shape[i] for i in range(2)]
        gray_image = cv2.resize(src=gray_image, dsize=(height, width), interpolation=cv2.INTER_CUBIC)
    print(f"Resized| width: {gray_image.shape[1]}, height: {gray_image.shape[0]}")
    # save gray image as binary image
    cv2.imwrite(f"test/{imagepath.split(r'/')[-1].split('.')[0]}_gray.jpg", gray_image)

    _, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

    cv2.imwrite(f"test/{imagepath.split(r'/')[-1].split('.')[0]}_binary.jpg", binary_image)

    print(f"Final| width: {binary_image.shape[1]}, height: {binary_image.shape[0]}")

    binary_matrix = np.where(binary_image == 255, 1, 0)

    with open(f"matrix/{imagepath.split(r'/')[-1].split('.')[0]}_matrix.pkl", 'wb') as f:
        pickle.dump(binary_matrix, f)

    # test
    with open(f"matrix/{imagepath.split(r'/')[-1].split('.')[0]}_matrix.pkl", 'rb') as f:
        matrix_data = pickle.load(f)

    height, width = len(matrix_data), len(matrix_data[0])

    image = np.zeros((height, width, 3), dtype=np.uint8)

    for y in range(height):
        for x in range(width):
            if matrix_data[y][x] == 0:
                image[y, x] = (0, 0, 0)  # black
            else:
                image[y, x] = (255, 255, 255)  # white
    cv2.imwrite(f"test/{imagepath.split(r'/')[-1].split('.')[0]}_reverse.jpg", image)
