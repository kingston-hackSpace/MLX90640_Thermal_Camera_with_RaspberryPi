# MLX90640 Thermal Camera with Raspberry Pi

Getting data from a MLX90640 Thermal Camera with a Raspberry Pi using Python.

---

## How to set up your Raspberry Pi (If installing from scratch)

Install the Raspberry Pi's operating system using the **Raspberry Pi Imager** software:

1. [Download Raspberry Pi Imager](https://www.raspberrypi.com/software/)
2. Insert the SD card into the computer.
3. Choose device, OS (use recommended settings) and select storage.

---

## How to log in to a Raspberry Pi

1. Power up the Raspberry Pi.
2. If prompted for a username and password, enter them in the login screen.

---

## How to download Python scripts

1. From this GitHub page, press the **Code** button and **Download ZIP**.
2. Unzip the folder and save it in an easy-to-access location (for example, Desktop).
3. Rename the folder to `thermal_camera`.

---

## Wiring the Thermal Camera

| Camera Pin | Raspberry Pi Pin |
|------------|----------------|
| GND        | Pin 39 (GPIO GND) |
| 3V         | Pin 1 (GPIO 3V3) |
| SDA        | Pin 3 (GPIO2) |
| SCL        | Pin 5 (GPIO3) |

---

## Open the Terminal

We'll use the Raspberry Pi Terminal to navigate to our scripts, install dependencies, and run Python scripts.

- Open the Terminal using the bar at the top-left of the Raspberry Pi desktop.

---

## Virtual Environments

We need to create a virtual environment to install Python packages for our camera.  
In your Terminal, type:

` python3 -m venv virtualEnv `

` source virtualEnv/bin/activate `

Learn more about virtual environments here:
https://www.w3schools.com/python/python_virtualenv.asp

## Installing Dependencies

Type the following commands in your Terminal:

```
sudo apt-get update
sudo apt-get upgrade   
pip3 install matplotlib
pip3 install scipy
pip3 install numpy
sudo apt-get install -y python3-smbus
sudo apt-get install -y i2c-tools
sudo nano /boot/firmware/config.txt
```
Edit the file that is now open by uncommenting the line "Add dtparam=i2c_arm=on" and modify it as follows:
  
  `Add dtparam=i2c_arm=on, i2c_arm_baudrate=400000 `
  
This enables the I2C interface and set the baud rate for faster data transfer.

To save and close, typle
**Save** -> Ctrl + O
Enter
**Close** -> Ctrl + X

You would be back at your main Terminal window. 
Now reboot your Raspberry Pi:

` sudo reboot `

Once the Raspberry Pi restarts, run the following command to scan and display devices connected on the I2C bus 1, helpful for verifying connectivity.

`sudo i2cdetect -y 1`

## Running Python Scripts
```
cd Desktop/thermal_camera
sudo python3 thermal_test_1.py
```
## More on Installation

Step-by-step guide for installing software and hooking up the MLX90640:
https://how2electronics.com/diy-thermal-imaging-camera-with-mlx90640-raspberry-pi/

## Troubleshooting

Cannot pip install Adafruit CircuitPython MLX90640

ImportError: No module named 'board'

## Purchasing: Thermal Camera MLX90640

https://shop.pimoroni.com/products/mlx90640-thermal-camera-breakout?variant=12549161746515
