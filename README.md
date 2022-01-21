# mypkg
ロボットシステム学の授業で製作したデバイスドライバを参考にした２つのモータを制御するデバイスドライバを製作した

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
