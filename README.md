# PumpkinPI_3
Instructions for creating the PumpkinPi a Raspberry Pi based Wireless MiTM device using the Pumpkin Framework


![pi](https://user-images.githubusercontent.com/60553334/128877154-ea2e4013-6b98-4673-89e9-1ab25084d7e6.jpg)

## Hardware

### Base

* Raspberry Pi zero w 
* Alfa Network AWUS036NHA (Others can work insure that the wireless card can go into monitoring mode)
* Screen optional ( I had to ditch it due to lack of space)

### Portable
* Battery (I used a LiPo)
* A case
* Charge controller for Battery type

If using a 3.7v Lipo you will need a 3v to 5v boost converter to feed the Pi 5v in. The Pi can run on 3v, however most Wireless cards will need the full 5v

<details>
  <summary>Images of my build</summary>
  
  ![20210810_140432](https://user-images.githubusercontent.com/60553334/128872558-a41210b5-33eb-4d6b-a193-0dae4d12ccc8.jpg)
![20210810_140437](https://user-images.githubusercontent.com/60553334/128872576-a500dcee-24d4-4f22-b854-0bbefd0c287f.jpg)
![20210810_140442](https://user-images.githubusercontent.com/60553334/128872584-450c2db4-f104-4743-aa10-8d562b91f8b1.jpg)

![20210810_140424](https://user-images.githubusercontent.com/60553334/128872543-77541c90-dfaf-4654-a071-6f06fb700ab0.jpg)
![20210810_140407](https://user-images.githubusercontent.com/60553334/128872525-51e6bfee-6b54-4c48-b34e-94186afef146.jpg)
![20210810_140501](https://user-images.githubusercontent.com/60553334/128872512-820a877f-e4fc-441c-b337-9fe0f3cc2a49.jpg)
</details>

## Video of hardware
https://www.youtube.com/watch?v=kuff6GiFd7M

<details>
  <summary>links to hardware</summary>
  https://shop.pimoroni.com/
 
 Pi Zero W
 https://shop.pimoroni.com/products/raspberry-pi-zero-w
 
 Pi Zero Case
 https://shop.pimoroni.com/products/pibow-zero-ver-1-3
 
 Battery 
 https://shop.pimoroni.com/products/lipo-battery-pack?variant=20429082247
 
 usb C charge contoller
 https://www.ebay.co.uk/itm/264334303561
 
 3v to 5v boost converter
 https://shop.pimoroni.com/products/adafruit-miniboost-5v-1a-tps61023
 
 Eink Screen
 https://shop.pimoroni.com/products/inky-phat?variant=12549254217811
 
</details>

## Building software. using Wifi Pumpkin3 framework 

```
 $ sudo apt install libssl-dev libffi-dev build-essential hoatapd libpcap-dev
 $ git clone https://github.com/P0cL4bs/wifipumpkin3.git
 $ cd wifipumpkin3
```
now, we need to install the PyQt5, it very easy:
```
sudo apt install python3-pyqt5
```
or check if the pyqt5 is installed successful:
```
python3 -c "from PyQt5.QtCore import QSettings; print('done')"
```
Edit requirements.txt and comment out the following lines
```
PyQt5==5.14
PyQt5-sip==12.7.2
```

From <https://github.com/P0cL4bs/wifipumpkin3/issues/15> 


now, if you got the message done, nice. the next step is install the wp3:
```
 $ sudo python3 setup.py install
```

Thats it! you can now start Wifi Pumpkin

```
sudo wifipumpkin3

```

For information on using Wifi Pumpkin see [here](https://wifipumpkin3.github.io/docs/getting-started#usage)
