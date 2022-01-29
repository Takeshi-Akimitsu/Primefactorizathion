# Primefactorizathon
ロボットシステム学の授業の課題として入力された0以上の整数を素因数分解するプログラムを製作した。  
primenumber.pyでは2以上の数が入力された場合は入力された数以下の素数、0と1が入力された場合はそれぞれ0と1のリストを出力する。なお、出力されたリストの最後の要素は入力された数である。  


# 動作環境
|OS|Ubuntu Server 20.04.3 LTS|
|---|---|
|ハードウェア|Raspberry Pi 3 ModelB|
  
# インストール方法
```
git clone git@github.com:Takeshi-Akimitsu/Motor_RaspberryPi.git
cd Motor_RaspberryPi
make
sudo insmod mymotor.ko  
sudo chmod 666 /dev/mymotor0  
```

# 実行

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
