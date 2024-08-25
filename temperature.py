import machine
import time

adcpin = 4
sensor = machine.ADC(adcpin)
  
def ReadTemperature():
    adc_value = sensor.read_u16()
    volt = (3.3/65535) * adc_value
    temperature = 27 - (volt - 0.706)/0.001721
    return round(temperature, 1)

print(round(ReadTemperature(),1),"°C")
averages = []
while True:
    temperature = ReadTemperature()
    averages.append(temperature)
    if(len(averages) > 20):
        print(round(sum(averages)/len(averages),1),"°C")
        averages = []
    time.sleep(0.5)

