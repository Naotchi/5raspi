#!/bin/sh

## 推論してもらう画像はscpでサーバーから各ラズパイの./questionフォルダに配布する予定です
## 画像は一枚ずつ配布するためワイルドカードで画像のpathを指定している
# shellcheck disable=SC1068
# shellcheck disable=SC1068
# file_path=


## 以下を自分の実行環境ごとにいじってください
## (注意)echoの行は参加チーム間で結果表示を統一化したいため出来るだけ変えないようお願いします
## 実行時間を測るためにtimeコマンドを用いているのでそこもいじらないようお願いします

### 推論の際に画像を別のフォルダに移動させたい場合は以下を実行してください

# shellcheck disable=SC2224
# mv $file_path ##前処理、推論の際に画像を読み込むフォルダ


echo "========TIME(Preprocessing)========"

time python3 preprocessing.py ##前処理を行うpythonファイル実行


echo "==================================="

time python3 predict.py ##推論を行うpythonファイル実行

echo "==================================="



file_path2="./question/*" ## 推論で用いた画像までのpath

## チームごとに変更するのはここまで

## 推論が終わったファイルは./Finに入れてください
mv $file_path2 ./Fin

