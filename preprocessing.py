import numpy as np
import cv2
import glob

dir_test = "./data"  # 前処理が終わった画像を入れるディレクトリ
# dir_test_height = "./data"
data = cv2.imread(glob.glob('./question/*')[0], cv2.IMREAD_GRAYSCALE)

hei = data[1000:3000]
height = []

# 高さ情報取得
hei = np.reshape(hei, -1)
hei = hei[31440: 2016144] 

for k in range(0, 1986400, 3056):
    for i in range(k, k+1360, 2):
        height.append(hei[i] + 256 * hei[i+1])

height = np.array(height).reshape([650, 680])

# 台座減算 
height = np.where(height > 12500, height - 12500, 0)

height = height.astype('float32')
height /= 2 ** 5

# np.save(dir_test + '/pic', pic)
np.save(dir_test + '/height', height)
