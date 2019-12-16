import numpy as np
import keras
import cv2
from display import display

if __name__ == "__main__":
    model = keras.models.load_model('./model0.h5')

    # X_pic = np.load('./data/pic.npy')
    # X_pic = cv2.resize(X_pic, (256, 256))
    # X_pic = X_pic.reshape(1, X_pic.shape[0], X_pic.shape[1], 1)

    X_height = np.load('./data/height.npy')
    X_height = cv2.resize(X_height, (256, 256))
    X_height = X_height.reshape(1, X_height.shape[0], X_height.shape[1], 1)

    p = model.predict(X_height)

    categories = ['BALTAN', 'METRON', 'ULTRA', 'TAIGA', 'TARO']
    p *= 100
    label = np.argmax(p)
    name = categories[label]
    prob = p[0][label]

    display(name, prob)



