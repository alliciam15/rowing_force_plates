# rowing_force_plates
Code for my BME 402 project: force plates mounted to an ergometer

This repository holds all functional code for a rowing machine - mounted force plate system. Each force plate (right and left) contains 4 load cells which have an analog output of 20 mV/V and an excitation voltage of 5V. A printed circuit board was designed to amplify these voltage outputs and digitize them using a MCP3208 ADC. A Raspberry Pi Pico was used to interface with the two SPI outputs of the ADCs from each plate and print a json containing all 8 channel values to send them serially over USB to a laptop (MicroPython_MCP3208). A python jupyter notebook is run on a laptop, reading the data incoming on the serial port and processing it. There are two separate ipynb files we made for this project, one file shows a UI that allows for discrete or continuous data collection by saving the individual channel values to a csv (data_collection_GUI.ipynb), and the other ipynb file shows a UI that graphs the total right and left force for real-time data plotting (live_plotting_GUI.ipynb). The live plotting ipynb file does not save data to a csv, but this could be integrated into code. 

The files holding UI information were generated using Qt Designer (version 5.9.7) and converted to .py files. The original .ui files for each interface were included.

