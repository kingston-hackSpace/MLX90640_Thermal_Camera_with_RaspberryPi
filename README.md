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

``` source virtualEnv/bin/activate ```
