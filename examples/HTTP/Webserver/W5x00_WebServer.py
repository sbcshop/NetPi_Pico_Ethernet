import board
import busio
import digitalio
import time

import adafruit_requests as requests
from adafruit_wiznet5k.adafruit_wiznet5k import *
from adafruit_wsgi.wsgi_app import WSGIApp
import adafruit_wiznet5k.adafruit_wiznet5k_wsgiserver as server
import adafruit_wiznet5k.adafruit_wiznet5k_socket as socket
import time
import board
import usb_hid
import digitalio
import board
import busio
import terminalio
import displayio
from adafruit_display_text import label
from adafruit_st7789 import ST7789
import time


# First set some parameters used for shapes and text
BORDER = 12
FONTSCALE = 3
BACKGROUND_COLOR = 0xFF0000  # red
FOREGROUND_COLOR = 0xFFFF00  # Purple
TEXT_COLOR = 0x000000

# Release any resources currently in use for the displays
displayio.release_displays()

tft_clk = board.GP10 # must be a SPI CLK
tft_mosi= board.GP11 # must be a SPI TX
tft_rst = board.GP12
tft_dc  = board.GP8
tft_cs  = board.GP9
tft_bl  = board.GP13
spi = busio.SPI(clock=tft_clk, MOSI=tft_mosi)

led_1  = board.GP14
tft_bl  = board.GP13
led = digitalio.DigitalInOut(tft_bl)
led_1 = digitalio.DigitalInOut(led_1)
led.direction = digitalio.Direction.OUTPUT
led_1.direction = digitalio.Direction.OUTPUT
led.value=True
led_1.value=False

# Make the displayio SPI bus and the GC9A01 display
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)
display = ST7789(display_bus, rotation=270, width=240, height=240, rowstart=80)

# Make the display context
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(display.width, display.height, 1)
color_palette = displayio.Palette(1)
color_palette[0] = BACKGROUND_COLOR

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

def inner_rectangle():
    # Draw a smaller inner rectangle
    inner_bitmap = displayio.Bitmap(display.width - BORDER * 2, display.height - BORDER * 2, 1)
    inner_palette = displayio.Palette(1)
    inner_palette[0] = FOREGROUND_COLOR
    inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER)
    splash.append(inner_sprite)
inner_rectangle()

# Draw a label
text = "PICO"
text_area = label.Label(terminalio.FONT, text=text, color=TEXT_COLOR)
text_group = displayio.Group(scale=FONTSCALE,x=80,y=50,)
text_group.append(text_area)  # Subgroup for text scaling
splash.append(text_group)

text1 = "ETHERNET"
text_area1 = label.Label(terminalio.FONT, text=text1, color=TEXT_COLOR)
text_group1 = displayio.Group(scale=FONTSCALE,x=50,y=90,)
text_group1.append(text_area1)  # Subgroup for text scaling
splash.append(text_group1)

text2 = "SERVER"
text_area2 = label.Label(terminalio.FONT, text=text2, color=TEXT_COLOR)
text_group2 = displayio.Group(scale=FONTSCALE,x=70,y=130,)
text_group2.append(text_area2)  # Subgroup for text scaling
splash.append(text_group2)

##SPI0
SPI0_SCK = board.GP18
SPI0_TX = board.GP19
SPI0_RX = board.GP16
SPI0_CSn = board.GP17

##reset
W5x00_RSTn = board.GP20

print("WebServer Test(DHCP)")

# Setup your network configuration below
# random MAC, later should change this value on your vendor ID
MY_MAC = (0x00, 0x01, 0x02, 0x03, 0x04, 0x05)
IP_ADDRESS = (192, 168, 1, 100)
SUBNET_MASK = (255, 255, 255, 0)
GATEWAY_ADDRESS = (192, 168, 1, 1)
DNS_SERVER = (8, 8, 8, 8)

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

ethernetRst = digitalio.DigitalInOut(W5x00_RSTn)
ethernetRst.direction = digitalio.Direction.OUTPUT

# For Adafruit Ethernet FeatherWing
cs = digitalio.DigitalInOut(SPI0_CSn)

# cs = digitalio.DigitalInOut(board.D5)
spi_bus = busio.SPI(SPI0_SCK, MOSI=SPI0_TX, MISO=SPI0_RX)

# Reset W5500 first
ethernetRst.value = False
time.sleep(1)
ethernetRst.value = True

# Initialize ethernet interface without DHCP
# eth = WIZNET5K(spi_bus, cs, is_dhcp=False, mac=MY_MAC, debug=False)
# Initialize ethernet interface with DHCP
eth = WIZNET5K(spi_bus, cs, is_dhcp=True, mac=MY_MAC, debug=False)

# Set network configuration
# eth.ifconfig = (IP_ADDRESS, SUBNET_MASK, GATEWAY_ADDRESS, DNS_SERVER)

print("Chip Version:", eth.chip)
print("MAC Address:", [hex(i) for i in eth.mac_address])
print("My IP address is:", eth.pretty_ip(eth.ip_address))

# Initialize a requests object with a socket and ethernet interface
requests.set_socket(socket, eth)

# Here we create our application, registering the
# following functions to be called on specific HTTP GET requests routes
web_app = WSGIApp()

html_string = '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>RaspberryPi Pico Web server </title>
</head>
<body>
<div align="center">
<H1>RaspberryPi Pico Web server and PICO Ethernet HAT</H1>
<h2>Network Information</h2>
<p>
My IP address is $IPADDRESS<br>
</p>
<h2>Control LED</h2>
<p>
<label for="led_on"></label><a href="/led_on" id="led_on"> [ON] </a><br>
</p>
<p>
<label for="led_off"></label><a href="/led_off" id="led_off"> [OFF] </a><br>
</p>
</div>
</body>
</html>
'''

html_string = html_string.replace("$CHIPNAME",eth.chip)
html_string = html_string.replace("$IPADDRESS",eth.pretty_ip(eth.ip_address))

#HTTP Request handlers
@web_app.route("/led_on")
def led_on(request):  # pylint: disable=unused-argument
    inner_rectangle()
    print("LED on!")
    led_1.value = True
    text1 = "LED ON"
    text_area1 = label.Label(terminalio.FONT, text=text1, color=TEXT_COLOR)
    text_group1 = displayio.Group(scale=FONTSCALE,x=50,y=90,)
    text_group1.append(text_area1)  # Subgroup for text scaling
    splash.append(text_group1)
    #led.value = True
    return ("200 OK", [], " led on!")

@web_app.route("/led_off")
def led_off(request): # pylint: disable=unused-argument
    inner_rectangle()
    print("LED off!")
    led_1.value = False
    text1 = "LED OFF"
    text_area1 = label.Label(terminalio.FONT, text=text1, color=TEXT_COLOR)
    text_group1 = displayio.Group(scale=FONTSCALE,x=50,y=90,)
    text_group1.append(text_area1)  # Subgroup for text scaling
    splash.append(text_group1)
    #led.value = False
    return ("200 OK", [], " led off!")

@web_app.route("/")
def root(request):  # pylint: disable=unused-argument
    print("Root WSGI handler")
    # return ("200 OK", [], ["Root document"])
    return ("200 OK", [], [html_string])

# Here we setup our server, passing in our web_app as the application
server.set_interface(eth)
print(eth.chip)
wsgiServer = server.WSGIServer(80, application=web_app)

print("Open this IP in your browser: ", eth.pretty_ip(eth.ip_address))

# Start the server
wsgiServer.start()

while True:
    # Our main loop where we have the server poll for incoming requests
    wsgiServer.update_poll()
    # Maintain DHCP lease
    eth.maintain_dhcp_lease()
    # Could do any other background tasks here, like reading sensors

