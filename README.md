# PumpkinPI_3

WIP current project will be updated and edited regulaly 

Instructions for creating the PumpkinPi a Raspberry Pi based Wireless MiTM device using the Pumkin Framework


 $ sudo apt install libssl-dev libffi-dev build-essential hoatapd libpcap-dev
 $ git clone https://github.com/P0cL4bs/wifipumpkin3.git
 $ cd wifipumpkin3
now, we need to install the PyQt5, it very easy:
sudo apt install python3-pyqt5
or check if the pyqt5 is installed successful:
python3 -c "from PyQt5.QtCore import QSettings; print('done')"

Edit requirements.txt and comment out the following lines
PyQt5==5.14
PyQt5-sip==12.7.2

From <https://github.com/P0cL4bs/wifipumpkin3/issues/15> 


now, if you got the message done, nice. the next step is install the wp3:
 $ sudo python3 setup.py install

From <https://wifipumpkin3.github.io/docs/getting-started> ![image](https://user-images.githubusercontent.com/60553334/126320139-72ff57e7-51b7-4609-98ac-0589b0bafb42.png)
