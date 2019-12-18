import numpy as np
import cv2
import glob
from multiprocessing import Pool
import itertools # ラズパイでimport出来るのか?

dir_test = "./data"  # 前処理が終わった画像を入れるディレクトリ
# dir_test_height = "./data"
data = cv2.imread(glob.glob('./question/*')[0], cv2.IMREAD_GRAYSCALE)

hei = data[1000:3000]
​
# 高さ情報取得
hei = np.reshape(hei, -1)
hei = hei[31440: 2016144] 
​
def append_height(x):
    h_list = []
    for i in range(x, x+1360, 2):
        h_list.append(hei[i] + 256 * hei[i+1])
    return h_list
​
pool = Pool(8) # or4　4コアだがあえて8プロセス並列の方が良い可能性があるらしい
# rangeの指定方法があってるのか分からない
callback = pool.map(append_height, range(0, 1986400, 3056))
​
# 二次元のリストを一次元に直したい
height = np.array(list(itertools.chain.from_iterable(callback))).reshape([650, 680])
​
# 台座減算 
height = np.where(height > 12500, height - 12500, 0)
​
height = height.astype('float32')
height /= 2 ** 5
​
# np.save(dir_test + '/pic', pic)
np.save(dir_test + '/height', height)