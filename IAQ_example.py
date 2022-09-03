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

while True:
            
    if bme.aqi < 0:
        AQI_SCORE = "ERROR"

    if 0 < bme.aqi <=50:
        AQI_SCORE = "EXCELLENT"
      
    if 50 < bme.aqi <= 100:
        AQI_SCORE = "GOOD"
        
    if 100 < bme.aqi <= 150:
        AQI_SCORE = "LIGHTLY POLLUTED"
        
    if 150 < bme.aqi <= 200:
        AQI_SCORE = "MODERATELY POLLUTED"
        
    if 200 < bme.aqi <= 250:
        AQI_SCORE = "HEAVILY POLLUTED"
        
    if 250 < bme.aqi <= 350:
        AQI_SCORE = "SEVERELY POLLUTED"

    if  bme.aqi > 350:
        AQI_SCORE = "EXTREMELY POLLUTED"
        
    time.sleep(3)
    
    print("Temp :",bme.temperature)
    print("%RH :",bme.humidity)
    print("Pressure :",bme.pressure)
    print("Gas Resistance :",bme.gas)
    print("AQI :",bme.aqi)
    print(AQI_SCORE)
    print("---------------------------")
