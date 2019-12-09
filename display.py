# 推論時にこのファイルのdisplayメソッドを呼び出してください
import os


def display(name, prob):
    # 以下を実行時に画像が置いてあるフォルダのpathに変更してください
    path = "./question"
    # 指定したpathにあるファイル名をリストに格納するメソッド、画像名表示の際に使う
    file_name = os.listdir(path)
    # print(file_name)
    print("=====RESULT=====")

    # macで実行した際.DS_Storeがフォルダ内にあったため例外処理を書いている、Raspiで実行する際にはいらないので以下のif分は削除してください
    if file_name[0] == ".DS_Store":
        print("file name : %s" % file_name[1])
    else:
        print("file name : %s" % file_name[0])

    print("name : %s" % name)
    print("Probability: %f " % prob + "%")
    print("=======TIME(Predict)======")
