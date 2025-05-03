"""
MicroPython code for the MCP3208 8-channel ADC with SPI (12 bit), used on the Raspberry Pi Pico
Adapted code from @romilly for the MCP3008 ADC (10-bit version): https://github.com/romilly/pico-code/blob/master/src/pico_code/pico/mcp3008/mcp3008.py

Save code as main.py to the pico to have the code run on start-up

Note: Using 2 separate ADC chips (2 separate SPI busses) and 4 channels from each chip. 

"""


import machine
import time
from time import sleep
from machine import Pin

class MCP3208:
    def __init__(self, spi, cs, ref_voltage=3.3):
        """
        Create MCP3208 instance
        Args:
        spi: configured SPI bus
        cs: pin to use for chip select
        ref_voltage: r
        """
        self.cs = cs
        self.cs.value(1) # ncs on
        self._spi = spi
        self._out_buf = bytearray(3)
        self._in_buf = bytearray(3)
        self._ref_voltage = ref_voltage
        
    def reference_voltage(self) -> float:
        """Returns the MCP3xxx's reference voltage as a float."""
        return self._ref_voltage
    def read(self, pin, is_differential=False):
        self.cs.value(0) # select
        #under init
        self._out_buf = bytearray(3)
        #under read()
        bit0 = pin & 0b1 # Extract bit 0
        bit1 = (pin >> 1) & 0b1 # Extract bit 1
        bit2 = (pin >> 2) & 0b1 # Extract bit 2
        self._out_buf[0] = (0x01 << 2) | ((not is_differential) << 1) | (bit2)
        self._out_buf[1] = (bit1 << 7) | (bit0 << 6)
        self._spi.write_readinto(self._out_buf, self._in_buf)
        self.cs.value(1) # turn off
        return ((self._in_buf[1] & 0x0F) << 8) | self._in_buf[2]

# for plate 2 (left)
spi_2 = machine.SPI(0, sck=Pin(2),mosi=Pin(3),miso=Pin(4), baudrate=1000000)
cs_2 = machine.Pin(5, machine.Pin.OUT)


# for plate 1 (right)
spi_1 = machine.SPI(1, sck=Pin(10), mosi=Pin(11), miso=Pin(12), baudrate=1000000)
cs_1 = machine.Pin(13, machine.Pin.OUT)

chip_2 = MCP3208(spi_2, cs_2)
chip_1 = MCP3208(spi_1, cs_1)

# Sampling and                                                                                                                                                                                                                                                   printing intervals
#sampling_interval = 1  # 1 ms
#print_interval = 1000
print_interval = 1    # 40 ms
max_length = 20         # Number of values to average

# Variables for ADC channels
adc_values = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
last_sample_time = time.ticks_ms()
last_print_time = time.ticks_ms()
channel_names = ['A', 'B', 'C', 'D']

tare_vals_2 = [1946, 2003, 1946, 2041]
tare_vals_1 = [2059, 2072, 2130, 2006]

while True:
    current_time = time.ticks_ms()
    # Sample from chip_1
    for channel in range(4):
        adc_1 = chip_1.read(channel)  # Read from chip_1
        adc_values[channel].append(adc_1)
        if len(adc_values[channel]) > max_length:
            adc_values[channel].pop(0)

    # Sample from chip_2
    for channel in range(4):
        adc_2 = chip_2.read(channel)  # Read from chip_2
        adc_values[channel + 4].append(adc_2)
        if len(adc_values[channel + 4]) > max_length:
            adc_values[channel + 4].pop(0)

    # Check if it's time to print the averages
    if time.ticks_diff(current_time, last_print_time) >= print_interval:
        # Print averages for chip_1
        for channel in range(4):
            if adc_values[channel]:  # Ensure there are values to average
                average = round(sum(adc_values[channel]) / len(adc_values[channel])) - tare_vals_1[channel]
                print(f"1{channel_names[channel]}: {average}")

        # Print averages for chip_2
        for channel in range(4):
            if adc_values[channel + 4]:  # Ensure there are values to average
                average = round(sum(adc_values[channel + 4]) / len(adc_values[channel + 4])) - tare_vals_2[channel]
                #average = round(sum(adc_values[channel + 4]) / len(adc_values[channel + 4]))
                print(f"2{channel_names[channel]}: {average}")
        last_print_time = current_time



