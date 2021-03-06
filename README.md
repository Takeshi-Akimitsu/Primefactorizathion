# Primefactorizathon
ロボットシステム学の授業の課題として入力された0以上の整数を素因数分解するプログラムを製作した。  
  
primenumber.pyでは2以上の整数が入力された場合は入力された数以下の素数とリストの最後に入力された数を追加したリストを出力する。0と1が入力された場合はそれぞれ0と1とリストの最後に入力された数を追加したリストを出力する。  
  
primefactorizathion.pyではprimenumber.pyにおいて入力された整数が素数であるなら素数であると出力し、合成数であるならその数を素因数分解した結果を出力する。なお、0と1は素数でないが合成数でもないため素数ではないと出力する。

# 動作環境
 - OS　Ubuntu Server 20.04.3 LTS
- ハードウェア Raspberry Pi 3 ModelB
- ROS noetic
  
# インストール方法
このパッケージをROSのsrcフォルダ下にインストールする。
```
cd ~/catkin_ws/src
git clone git@github.com:Takeshi-Akimitsu/Primefactorizathion.git
cd ..
catkin_make  
```

# 実行
端末1でROSを立ち上げる。
```
roscore
```
端末2でprimenumber.pyを実行する。
```
rosrun Primefactorizathion primenumber.py
```
端末3でprimenumber.pyがPublishしたデータを取り出せるようにする。
```
rostopic echo /primenumber
```
端末4でprimefactorizathion.pyを実行する。
```
rosrun Primefactorizathion primefactorizathion.py
```
端末5でprimefactorizathion.pyがPublishしたデータを取り出せるようにする。
```
rostopic echo /primefactorizathion
```

# 実行結果
下記のリンクよりこのパッケージの動作が確認できる。  
https://youtu.be/0Oh3foGFxl4

# 参考
https://amateur-engineer-blog.com/prime/

# 謝辞
このパッケージのprimenumber.pyは[こちら](https://amateur-engineer-blog.com/prime/)の素数判定のコードを参考に製作しました。誠にありがとうございます。
