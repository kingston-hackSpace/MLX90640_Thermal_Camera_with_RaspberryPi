# MLX90640_Thermal_Camera_with_RaspberryPi
Getting data from a MLX90640 Thermal Camera with a Raspberry Pi and Python

<h3>How to setup the device (If installing from scratch)</h3>
<h3>How to install the operating system image using Raspberry Pi imager</h3>
<ul>
<li>https://www.raspberrypi.com/software/</li>
<li>Insert the SD card into the computer.</li>
<li>Choose device, OS (use recommended settings) and select storage</li>
</ul>

<h3>How to login to a raspberry pi</h3>
<ul>
<li>Power up the raspberry pi.</li>
<li>If prompted for a username and password, enter these in the following screen.</li>
</ul>

<h3>How to download Python scripts</h3>
<ul>
<li>From this current GitHub webpage, press on the button "Code" and " Download ZIP"</li>
<li>Unzip your folder. Save this folder in an easy-to-access location. For this tutorial, keep your folder in Desktop.</li>
<li>Re-name your folder as: "thermal_camera"</li>  
</ul>

<h3>Wiring the Thermal Camera</h3>
<ul>
<li>Camera - RasPi
<li>GND - Pin39 (GPIO GND) </li>
<li>3V - Pin1 (GPIO 3V3)</li>
<li>SDA - Pin3 (GPIO2) </li>
<li>SCL - Pin5 (GPIO3) </li>
</ul>

<h3>How to use the terminal, introduction to linux commands.</h3>
We are now going to use the Raspberry Pi's Terminal to type commands that will locate our thermal-camera-Python-script, compile it and execute it: 
<ul>
<li> Open the Terminal using the bar at the top-left of the RaspberryPi main desktop window.
<li> Type the following commands:
<li> cd Desktop/thermal_camera </li>
<li> sudo python3 thermal_test_1.py</li>

</ul>

<h3>More on installation...</h3>

virtual environments in python
https://www.w3schools.com/python/python_virtualenv.asp

A step by step guide for installing software and hooking up the mlx90640 to the rpi:
https://how2electronics.com/diy-thermal-imaging-camera-with-mlx90640-raspberry-pi/

Trouble shooting 
https://raspberrypi.stackexchange.com/questions/113922/cannot-pip-install-adafruit-circuitpython-mlx90640
https://stackoverflow.com/questions/53196848/importerror-no-module-named-board-adafruit

Purchasing device
https://thepihut.com/products/wide-angle-110-mlx90640-thermal-camera-breakout?srsltid=AfmBOorKWaIf_uXfN9zlBELxZb7Ys6t_FNa97cda5I--NhM1RRhj3t2Z
