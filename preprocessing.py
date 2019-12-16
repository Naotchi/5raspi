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
start_i = 31440 # 31440 = (10*1528+440)*2
i = 31440
while i < 2016144:# 2016144 = (659*1528+1120)*2 = (660*1528-408)*2
    height.append(hei[i] + 256 * hei[i+1])
    i += 2
    if (i - start_i) % 1360 == 0: # 1360 = 680*2
        i += 1696 # 1696 = ((1528-1120)+440)*2
        start_i = i
height = np.array(height).reshape([650, 680])

# 台座減算 
height = np.where(height > 12500, height - 12500, 0)

height = height.astype('float32')
height /= 2 ** 5

# np.save(dir_test + '/pic', pic)
np.save(dir_test + '/height', height)
