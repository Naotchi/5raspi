import numpy as np
import cv2
import glob

dir_test = "./data"  # 前処理が終わった画像を入れるディレクトリ
# dir_test_height = "./data"
data = cv2.imread(glob.glob('./question/*')[0], cv2.IMREAD_GRAYSCALE)

pic = data[0:1000]  # ここから前と同じ
hei = data[1000:3000]
height = []
for x in range(2000):
    for y in range(0, 1527, 2):
        a = hei[x][y] + 256 * hei[x][y + 1]
        height.append(a)
height = np.array(height)
height = np.reshape(height, (1000, 1528))
pic = pic[10: 660, 440: 1120]
height = height[10: 660, 440: 1120]  # ここまで前と同じ
for i in range(650):
    for j in range(680):
        if height[i][j] > 12500:
            height[i][j] -= 12500
        else:
            height[i][j] = 0
height = height.astype('float32')
height /= 2 ** 5

np.save(dir_test + '/pic', pic)
np.save(dir_test + '/height', height)
