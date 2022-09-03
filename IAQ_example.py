#     AQI REFERENCE
#-----------------------------------
#   0 - 50  | EXCELLENT
#  51 - 100 | GOOD
# 101 - 150 | LIGHTLY POLLUTED
# 151 - 200 | MODERATELY POLLUTED
# 201 - 250 | HEAVILY POLLUTED
# 251 - 350 | SEVERELY POLLUTED
# 351 +     | EXTREMELY POLLUTED

# REFERENCES
# https://github.com/G6EJD/BME680-Example (c) d.l.bird 2018
# https://github.com/robert-hh/BME680-Micropython
# https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme680-ds001.pdf
# https://forums.pimoroni.com/t/bme680-observed-gas-ohms-readings/6608/17
# https://github.com/thstielow/raspi-bme680-iaq
# My GitHub: https://github.com/natepichler

#----------------------------------------
from machine import Pin, I2C
from time import sleep
import math
from bme680iaq import *

#----------------------------------------

# BME680 I2C Interface
#----------------------------------------
i2c = I2C(0, scl=Pin(13), sda=Pin(12))
bme = BME680_I2C(i2c=i2c)
#----------------------------------------
gas_max=50000
for _ in range(10):
    print(bme.comp_gas)
    time.sleep(3)
            
while True:
            
    AQ = min((bme.comp_gas/gas_max)**2,1)*100
        IAQ = (1 - (AQ/100))*500
    
    if IAQ < 0:
        IAQ = "ERROR"

    if 0 < IAQ <=50:
        IAQ_SCORE = "EXCELLENT"
        
    if 50 < IAQ <= 100:
        IAQ_SCORE = "GOOD"
        
    if 100 < IAQ <= 150:
        IAQ_SCORE = "LIGHTLY POLLUTED"
        
    if 150 < IAQ <= 200:
        IAQ_SCORE = "MODERATELY POLLUTED"
        
    if 200 < IAQ <= 250:
        IAQ_SCORE = "HEAVILY POLLUTED"
        
    if 250 < IAQ <= 350:
        IAQ_SCORE = "SEVERELY POLLUTED"

    if  IAQ > 350:
        IAQ_SCORE = "EXTREMELY POLLUTED"
        
    time.sleep(3)
    
    print("Temp :",bme.temperature)
    print("%RH :",bme.humidity)
    print("Pressure :",bme.pressure)
    print("Gas Resistance :",bme.gas)
    print("AQI :",IAQ)
    print(IAQ_SCORE)
    print("---------------------------")
