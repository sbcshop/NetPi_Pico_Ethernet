# NetPi_Pico_Ethernet

NetPi is the perfect solution for your Raspberry Pi Pico's connectivity needs. It's an Ethernet HAT that enables your Pico to easily connect to the internet. With support for various internet protocols such as TCP, UDP, WOL over UDP, ICMP, IPv4, and more, NetPi can create IoT devices, robots, home automation systems, and industrial control systems.

<img src="https://github.com/sbcshop/NetPi_Pico_Ethernet/blob/main/images/NetPi_img.jpg" width="649" height="376">

### NetPi Features:
  - Support Hardwired Internet protocols: TCP, UDP, WOL over UDP, ICMP, IGMPv1/v2, IPv4, ARP, PPPoE
  - Perform SOCKET-less commands: ARP-Request, PING-Request
  - 10Base-T/100Base-TX Ethernet PHY with auto-negotiation for full and half duplex with 10 and 100-based connections
  - 3.3V operation with 5V I/O signal tolerance
  - Network indicator LEDs for full/half duplex, link, 10/100 speed, and active status
  - Female pin header for direct attachment to Raspberry Pi Pico and breakout key pins for use with other host boards
  - 1.3" TFT LCD with 240 x 240 pixels RGB and a 5-way joystick for user experience

### Pinouts: 
<img src="https://github.com/sbcshop/NetPi_Pico_Ethernet/blob/main/images/NetPi_Pinout.jpg" width="436" height="512">

## Setup NetPi
1. Download and Install Thonny IDE for your respective OS from Link [Download Thonny](https://thonny.org/)
   
   <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img.JPG" />
   
2. Adding **CircuitPython** bootloader in NetPi 
  * For this first you need to *Press and Hold* the boot button of Pico on NetPi, without releasing the button connect it to USB port of PC/laptop. 
Then you see a new device named "RPI-RP2" as shown in figure, afte this download file ["firmware.uf2"](https://github.com/sbcshop/NetPi_Pico_Ethernet/blob/main/firmware.uf2) available in this repository , or you can download latest firmware from Circuitpython official website [click here](https://circuitpython.org/board/raspberry_pi_pico/)   
    <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img13.png" /> 
     
  * After downloading just copy and paste firmware file to "RPI-RP2" folder and then remove the device.
Now at this step bootloader installed properly inside Pico of NetPi. To verify remove device and re-insert into PC/Laptop, no need to press boot button. 
This time you will see a new device as shown in the below image:-
    <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img11.png" />

**Running First Code in NetPi**
1. Start Thonny IDE application, after this go to run->select interpreter, choose device and suitable com port
    <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img18.png" />
    <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img19.png" />
    
   Write simple python code and click on green run button
    <img src= "https://github.com/sbcshop/HackyPi-Software/blob/main/images/sample_hello_program.png" />

2. Now you are ready to try out your own codes. Even you can try some of below Example codes provided, for that just download all the files (library files) from [```lib```](https://github.com/sbcshop/NetPi_Pico_Ethernet/tree/main/lib) folder of this repository and copy those file inside the NetPi ```lib``` folder. 
3. [Checkout this step by step guide to move files from PC to Pico of NetPi](https://github.com/sbcshop/NetPi_Pico_Ethernet/blob/main/Documents/Move%20file%20inside%20Raspberry%20Pi%20Pico%20W%20of%20NetPi.pdf), Once you understood the process then you can start experimenting with below examples.

## Examples Codes  
 The example folder in repository includes ready to use and experimental code with NetPi 
   - [examples/DHCP](https://github.com/sbcshop/NetPi_Pico_Ethernet/tree/main/examples/DHCP) folder contains example about DHCP program.
   - [examples/DNS](https://github.com/sbcshop/NetPi_Pico_Ethernet/tree/main/examples/DNS) folder contains example about DNS code.
   - [examples/HTTP](https://github.com/sbcshop/NetPi_Pico_Ethernet/tree/main/examples/HTTP) folder contains example about webserver and client using HTTP.
   - and [Many more...](https://github.com/sbcshop/NetPi_Pico_Ethernet/tree/main/examples)

Play with it and create your own, **Happy Coding!** 

### Resources:
  - [NetPi Schematic](https://github.com/sbcshop/NetPi_Pico_Ethernet/blob/main/Design%20Data/SCH%20pico_ethernet.pdf)
  - [Product Dimension](https://github.com/sbcshop/NetPi_Pico_Ethernet/blob/main/Mechanical%20Data/DIM.pdf)
  - [Product Step File](https://github.com/sbcshop/NetPi_Pico_Ethernet/blob/main/Mechanical%20Data/Ethernet%20for%20pico.step)
  - [CircuitPython Getting Started](https://learn.adafruit.com/welcome-to-circuitpython/what-is-circuitpython)
  - [RP2040 Datasheet](https://github.com/sbcshop/HackyPi-Hardware/blob/main/Documents/rp2040-datasheet.pdf)
  - [Wiznet Datasheet](https://github.com/sbcshop/NetPi_Pico_Ethernet/blob/main/Documents/w5100s-q_datasheet.pdf)
  - [Wiznet References]( https://www.wiznet.io/product-item/w5100/)

## Related Products

* [SquaryFi](https://shop.sb-components.co.uk/collections/raspberry-pi-pico/products/squary?variant=40443840921683) - ESP8266-12E version of SquaryPi
   
   ![SquaryFi](https://cdn.shopify.com/s/files/1/1217/2104/products/2_12d19ffa-bcda-47bf-8ea9-bb76fc40aee3.png?v=1670307456&width=300)
 
 * [Roundy](https://shop.sb-components.co.uk/products/roundy?variant=39785171681363) - 1.28" Round LCD version based on ESP8266 and RP2040
   
   ![Roundy](https://cdn.shopify.com/s/files/1/1217/2104/products/roundypi.png?v=1650457581&width=300)

## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=300">
</p>
