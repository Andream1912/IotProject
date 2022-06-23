from bsp import board
import peripherals.rfid as RFID
import gpio
import pwm
from networking import wifi
import credentials
from protocols import mqtt

rfid_rst = D21
rfid_cs = D15
servo = D23
period = 20000

gpio.mode(servo, OUTPUT)
#----------SPI RFID initialization-----------------------#
###############################################
#               3.3 -> 3.3                    #
#               GND -> GND                    #
#               SDA -> D15                    #
#               SCK -> D14                    #
#               Mosi -> D13                   #
#               Miso -> D12                   #
###############################################
rdr = RFID.RFID(rfid_rst, rfid_cs)

# Function to rotate the servo motor 90 °
def rotate():
    global pulse
    pulse = 2500
    pwm.write(servo, period, pulse, MICROS)

# Function to rotate the servo motor -90 °
def rotateBack():
    global pulse
    pulse = 1500
    pwm.write(servo, period, pulse, MICROS)

#function to start client loop of MQTT
def run():
    try:
        client.loop()
    except Exception as e:
        sleep(6000)

try:
    wifi.configure(ssid = credentials.SSID, password= credentials.PASSWORD)
    wifi.start()
    #initialization of MQTT client 
    client = mqtt.MQTT("test.mosquitto.org","exit")
    client.connect()
    thread(run)
    
    while True:
        sleep(5000)        
        if client.is_connected():
            break


    while True:
            (stat, tag_type) = rdr.request(rdr.REQIDL)
            if stat == rdr.OK:
                (stat, raw_uid) = rdr.anticoll()
                if stat == rdr.OK:
                    card_id = "0x%02x%02x%02x%02x" % (
                        raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
                    try:
                        #publishing of card_id on the topic /IoT2022/SmartAcces
                        client.publish("/IoT2022/SmartAcces", card_id, qos=2, retain=False)
                        print("publishing")
                    #Otherwise rise an exception
                    except Exception as e:
                        print(e)
                    #motion of the servo
                    rotate()
                    sleep(2500)
                    rotateBack()
        
#exception for the WI-FI
except WifiBadPassword:
    print("Bad Password")
except WifiBadSSID:
    print("Bad SSID")
except WifiException:
    print("Generic Wifi Exception")
except Exception as e:
    raise e
