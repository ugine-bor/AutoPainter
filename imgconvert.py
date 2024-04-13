import cv2
import numpy as np
import pickle


def convertimage(imagepath):
    gray_image = cv2.imread(imagepath, cv2.IMREAD_GRAYSCALE)

    _, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

    binary_matrix = np.where(binary_image == 255, 1, 0)

    with open(f"matrix/{imagepath.split(r'/')[-1].split('.')[0]}_matrix.pkl", 'wb') as f:
        pickle.dump(binary_matrix, f)
