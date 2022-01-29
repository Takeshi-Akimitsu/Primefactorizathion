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

# アンインストール
```
sudo rmmod mymotor 
```

# 実行結果
下記のリンクよりこのデバイスドライバの動作が確認できる  
https://youtu.be/cU3D8GxwP2c

# 参考
[Raspberry Pi 3 ModelB](https://datasheets.raspberrypi.com/rpi3/raspberry-pi-3-b-reduced-schematics.pdf)  

[TBTB6643KQデータシート](http://www.kyohritsu.jp/eclib/OTHER/DATASHEET/TOSHIBA/tb6643kq.pdf)

https://github.com/MibuchiYuta/Control_DCmotor_RaspberryPi

# 謝辞
このデバイスドライバは[三渕優太さん](https://github.com/MibuchiYuta/Control_DCmotor_RaspberryPi
)のコードを参考に製作しました。誠にありがとうございます。
