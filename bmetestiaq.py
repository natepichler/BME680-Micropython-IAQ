from bme680iaq import *
from machine import I2C, Pin
import math
import time
i2c = I2C(0, scl=Pin(13), sda=Pin(12))
bme = BME680_I2C(i2c=i2c)

gas_max=50000

for _ in range(5):
    print(bme.comp_gas)
    time.sleep(3)
    
while True:
    if bme.comp_gas > gas_max:
        gas_max = bme.comp_gas
            
    AQ = min((bme.comp_gas/gas_max)**2,1)*100
    IAQ = (1 - (AQ/100))*500
    print(bme.temperature, bme.humidity, bme.pressure, bme.comp_gas, IAQ)
    time.sleep(3)






