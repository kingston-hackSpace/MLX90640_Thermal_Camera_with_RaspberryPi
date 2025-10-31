# MLX90640 Thermal Camera with Raspberry Pi

Getting data from a MLX90640 Thermal Camera with a Raspberry Pi using Python.

---

## How to set up your Raspberry Pi (If installing from scratch)

Install the Raspberry Pi's operating system using the **Raspberry Pi Imager** software:

1. [Download Raspberry Pi Imager](https://www.raspberrypi.com/software/)
2. Insert the SD card into your computer.
3. At the Imager softare, choose:
   
    * **Device** – Select your Raspberry Pi model.

    * **Operating System** – Choose the 64-bit version (use the recommended settings).

    * **Storage** – Select your SD card.

---

## How to log-in to a Raspberry Pi

1. Power up the Raspberry Pi.
2. If prompted for a username and password, enter them in the login screen.

---
## TUTORIAL (see for reference)
This tutorial is based on the guide from **how2electronics.com**

If you have any enquiries regarding the steps that follow, please visit:
https://how2electronics.com/diy-thermal-imaging-camera-with-mlx90640-raspberry-pi/

---
## MLX90640 Library Documentation (see for reference)

Library Documentation : 
https://github.com/kingston-hackSpace/mlx90640-library 

Forked in Oct-2025 from :  
https://github.com/melexis/mlx90640-library/tree/master 


-------------------------------------
-------------------------------------
-------------------------------------
##LETS START! 
-------------------------------------
-------------------------------------
-------------------------------------
-------------------------------------


## Wiring the Thermal Camera

| Camera Pin | Raspberry Pi Pin |
|------------|----------------|
| GND        | Pin 39 (GPIO GND) |
| 3V         | Pin 1 (GPIO 3V3) |
| SDA        | Pin 3 (GPIO2) |
| SCL        | Pin 5 (GPIO3) |

RPi Pin Layout : https://github.com/kingston-hackSpace/MLX90640_Thermal_Camera_with_RaspberryPi/blob/main/GPIO.png 

---
## Download Python scripts

1. From this GitHub page, press the **Code** button and **Download ZIP**.
2. Unzip the folder and save it in an easy-to-access location (for example, Desktop).
3. Rename the folder to `thermal_camera`.

---

## Open the Terminal

We'll use the Raspberry Pi **Terminal** to navigate to our scripts, install dependencies, and run Python scripts.

- Open the Terminal using the bar at the top-left of the Raspberry Pi desktop.


---

## Virtual Environments

We need to create a virtual-environment to install Python packages for our camera. 
We will save our virtual-environment at our project folder, so we will always have to start coding from our folder location.

Type in your Terminal:

`cd Desktop/thermal_camera`

` python3 -m venv venv `

` source venv/bin/activate `

Learn more about virtual environments here:
https://www.w3schools.com/python/python_virtualenv.asp

## Installing Dependencies

Type the following commands in your Terminal:

```
sudo apt-get update
sudo apt-get upgrade -y   
pip3 install matplotlib
pip3 install scipy
pip3 install numpy
sudo apt-get install -y python3-smbus
sudo apt-get install -y i2c-tools
sudo nano /boot/firmware/config.txt
```

Reference image: https://github.com/kingston-hackSpace/MLX90640_Thermal_Camera_with_RaspberryPi/blob/main/nano.png

Edit the file that is now open by uncommenting the line "Add dtparam=i2c_arm=on" and modify it as follows:
  
  `Add dtparam=i2c_arm=on, i2c_arm_baudrate=400000 `
  
This enables the I2C interface and set the baud rate for faster data transfer.

To save and close, type

**Save** -> Ctrl + O

Enter

**Close** -> Ctrl + X

You would be back at your main Terminal window. 
Now reboot your Raspberry Pi:

` sudo reboot `

Once the Raspberry Pi restarts, run the following command to scan and display devices connected on the I2C bus 1, helpful for verifying connectivity.

`sudo i2cdetect -y 1`

Re-open your virtual environtment and install more dependancies:

```
python3 -m venv venv
source venv/bin/activate
pip3 install RPI.GPIO adafruit-blinka
pip3 install adafruit-circuitpython-mlx90640
```

## Running Python Scripts

Run the Script
```
cd Desktop/thermal_camera
python3 thermal_test_1.py
```

Close the Script
`Ctrl + C`

TEST1: Reads temperature-data from an MLX90640 thermal camera and prints the average temperature.

TEST2: Real-Time visualization of thermal images (on monitor via HDMI) using matplotlib and numpy.

TEST3: Save 'frame-shots" images (jpeg) every 100 cycles. 


## BONUS: TEST4: Real-Time visualization on your phone

STEP 1: Install required packages:
   hostapd → creates the Wi-Fi hotspot.
   dhcpcd5 → manages network interfaces (required for static IP).
   dnsmasq → acts as a DHCP server to assign IPs to connected devices.

```
sudo apt install hostapd dnsmasq -y
sudo systemctl stop hostapd
sudo systemctl stop dnsmasq
```
STEP 2: Enable and start dhcpcd
```
sudo apt install dhcpcd5 -y
sudo systemctl enable dhcpcd
sudo systemctl start dhcpcd
```
STEP 3: Check status

`sudo systemctl status dhcpcd`

sudo nano /etc/dhcpcd.conf

interface wlan0
    static ip_address=192.168.4.1/24
    nohook wpa_supplicant

sudo systemctl restart dhcpcd
```

## Raspberry Pi OverHeating Hazards
This project demands operating the Raspberry Pi's I2C bus at high speeds, necessary real-time thermal imaging with the MLX90640 sensor. This can lead to increased power consumption and heat generation. It’s crucial to ensure adequate cooling for the Raspberry Pi to prevent thermal throttling or damage. Proper ventilation or active cooling solutions, such as heatsinks or fans, are recommended to maintain stable operation and prevent overheating.

## Purchasing: 
Thermal Camera MLX90640
https://shop.pimoroni.com/products/mlx90640-thermal-camera-breakout?variant=12549161746515

Raspberry Pi - Model 5
https://shop.pimoroni.com/products/raspberry-pi-5?variant=41044580171859


