# OLED Stats Display for Raspberry Pi

This project demonstrates how to set up an OLED stats display on a Raspberry Pi running either Raspberry Pi OS (Bullseye) or Kali Linux. The display shows various system stats such as hostname, IP address, CPU usage, CPU temperature, memory usage, and storage usage.

## Prerequisites

- Raspberry Pi with I2C interface enabled
- SSD1306 OLED display connected via I2C
- Python 3 and necessary libraries

## Installation

### Step 1: Enable I2C Interface

Ensure the I2C interface is enabled on your Raspberry Pi. 
This can be done using 
`raspi-config`:

```
sudo raspi-config
```

Navigate to Interfacing Options -> I2C and enable it.

### Step 2: Install Required Libraries
Install the necessary Python libraries:

```
sudo apt-get update
sudo apt-get install python3-venv
python3 -m venv ~/myenv
source ~/myenv/bin/activate

sudo pip3 install adafruit-circuitpython-ssd1306 pillow psutil
```

### Step 3: Create Python Script
Create a Python script named stats.py:
copy and paste the code from `stats.py` included alongside this repo


### Step 4: Create Systemd Service
Create a systemd service file to run the script on startup. Create a file named OLED_STATS.service in /etc/systemd/system/:
copy and paste the code from `OLED_STATS.service` included alongside this repo

### Step 5: Enable and Start the Service
Reload the systemd manager configuration, enable the service to start on boot, and then start the service:
```
sudo systemctl daemon-reload
sudo systemctl enable OLED_STATS.service
sudo systemctl start OLED_STATS.service
```

### Step 6: Verify the Service
Check the status of the service to ensure it's running correctly:

```
sudo systemctl status OLED_STATS.service
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Troubleshooting

Common Issues
- ModuleNotFoundError: Ensure all required Python libraries are installed.
- I2C Interface: Verify the I2C interface is enabled and properly configured.
- Service Not Starting: Check the service status and logs for any errors.

## Additional Resources
Add an OLED Stats Display to Raspberry Pi OS Bullseye: 
https://www.the-diy-life.com/add-an-oled-stats-display-to-raspberry-pi-os-bullseye/

Setting Up an OLED Display on Kali Linux for Your Raspberry Pi: 
https://tohfaakib.com/step-by-step-guide-to-setting-up-an-oled-display-on-kali-linux-for-your-raspberry-pi/

RASPBERRYPI 1U 3D PRINTED TRAY: 
https://www.printables.com/model/69176-1u-raspberry-pi-rack-with-moduler-trays

Feel free to open issues or submit pull requests for improvements and bug fixes.

### File Structure

```
rpiOLED/
├── LICENSE
├── README.md
├── stats.py
└── OLED_STATS.service
```
