# Arduino-Temp-Test
This project demonstrates how to measure temperature using an Arduino and the pyFirmata library. It reads analog signals from a temperature sensor, calculates the corresponding temperature, and displays the results in real-time.


## Introduction
This project is designed to interface an Arduino with a temperature sensor (such as a thermistor or RTD) to measure temperature. The analog signals from the sensor are read by the Arduino, which then communicates the data to a Python script via the pyFirmata library. The script processes the data and outputs the temperature.


## Hardware Requirements
* Arduino Board (e.g., Uno, Mega)
* Temperature Sensor (e.g., thermistor or RTD)
* Resistors (for voltage divider circuit, e.g., R1 = 300 ohms, R0 = 100 ohms)
* Connecting Wires
* USB Cable (to connect Arduino to your computer)


## Software Requirements
* Python 3.x
* pyFirmata library
* Arduino IDE (to upload the Firmata firmware to the Arduino)


## Setup and Installation
1. Install Firmata on the Arduino:
 * Open the Arduino IDE.
 * Go to File > Examples > Firmata > StandardFirmata.
 * Select your Arduino board and port, then upload the code to the board.

2. Install Python and pyFirmata:
 * Ensure Python 3.x is installed on your system.
 * Install the pyFirmata library by running the following command:
   ```bash
   pip install pyfirmata

3. Clone the Repository:
   ```bash
   git clone https://github.com/yourusername/arduino-temperature-measurement.git
   cd arduino-temperature-measurement

4. Connect the Circuit:
 * Connect the temperature sensor and resistors according to the circuit diagram section.


> **Note**:  
> The code and setup appear to be functioning correctly, but the temperature readings may be inaccurate due to a potentially faulty or outdated sensor and board. If you're experiencing unexpected results, consider verifying the sensor's condition or replacing it with a new one. Additionally, ensure that all connections are secure and that the sensor is properly calibrated for accurate measurements.
