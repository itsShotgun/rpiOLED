from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import busio
import digitalio
import board
import socket
import subprocess
import time
import psutil

# Define the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Define the Reset Pin
oled_reset = digitalio.DigitalInOut(board.D4)

# Create the SSD1306 OLED class.
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x3C, reset=oled_reset)

# Clear display.
disp.fill(0)
disp.show()

# Create blank image for drawing.
width = disp.width
height = disp.height
image = Image.new("1", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Load a clean font.
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
font_size = 10
font = ImageFont.truetype(font_path, font_size)

# Function to get CPU usage
def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

# Function to get CPU temperature
def get_cpu_temperature():
    try:
        cpu_temp = subprocess.check_output("vcgencmd measure_temp | egrep -o '[0-9]*\.[0-9]*'", shell=True).decode("utf-8").strip()
        return cpu_temp
    except subprocess.CalledProcessError:
        return "N/A"

# Function to get memory usage
def get_memory_usage():
    memory_usage = subprocess.check_output("free -m | grep 'Mem:' | awk '{print $3}'", shell=True).decode("utf-8").strip()
    return memory_usage

# Function to get storage usage
def get_storage_usage():
    storage_usage = subprocess.check_output("df -h / | awk 'NR==2 {print $5}'", shell=True).decode("utf-8").strip()
    return storage_usage

while True:
    hostname = socket.gethostname()
    cmd = "ip addr show eth0 | grep -Po 'inet \K[\d.]+'"
    Eth_IP = subprocess.check_output(cmd, shell=True).decode("utf-8").strip()

    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw.text((0, 0), "==================", font=font, fill=255)
    draw.text((0, 12), "               " + hostname, font=font, fill=255)
    draw.text((0, 24), "==================", font=font, fill=255)
    disp.image(image)
    disp.show()
    time.sleep(3)

    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw.text((0, 0), "==================", font=font, fill=255)
    draw.text((0, 12), "         IP : " + Eth_IP + " ", font=font, fill=255)
    draw.text((0, 24), "==================", font=font, fill=255)
    disp.image(image)
    disp.show()
    time.sleep(3)

    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw.text((0, 0), "==================", font=font, fill=255)
    draw.text((0, 12), "          STORAGE: " + get_storage_usage(), font=font, fill=255)
    draw.text((0, 24), "==================", font=font, fill=255)
    disp.image(image)
    disp.show()
    time.sleep(3)

    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw.text((0, 0), "==================", font=font, fill=255)
    draw.text((0, 12), "    CPU: " + str(get_cpu_usage()) + "%   |  " + get_cpu_temperature() + "C", font=font, fill=255)
    draw.text((0, 24), "==================", font=font, fill=255)
    disp.image(image)
    disp.show()
    time.sleep(3)

    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw.text((0, 0), "==================", font=font, fill=255)
    draw.text((0, 12), "       MEMORY:  " + get_memory_usage() + " MB", font=font, fill=255)
    draw.text((0, 24), "==================", font=font, fill=255)
    disp.image(image)
    disp.show()
    time.sleep(3)
