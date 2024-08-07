import pyfirmata as pf
import time

# Setup communication with Arduino
port = 'COM3'  # Specify the port where the Arduino is connected
board = pf.Arduino(port)
it = pf.util.Iterator(board)  # Create an iterator to read data from the board
it.start()  # Start the iterator to avoid missing data

# Enable reporting for analog pins
board.analog[1].enable_reporting()  # Enable reporting for analog pin A1
board.analog[2].enable_reporting()  # Enable reporting for analog pin A2

# Constants
power = 1.1  # Assumed reference voltage (in volts)
R1 = 300  # Resistance value R1 (in ohms)
R0 = 100  # Resistance value R0 (in ohms)
T0 = 0  # Reference temperature T0 (in degrees Celsius), if needed
alpha = 0.00385  # Temperature coefficient of resistance (for the sensor)

# Main loop
while True:
    # Read from analog pins
    pin1_value = board.analog[1].read()  # Read the analog value from pin A1
    pin2_value = board.analog[2].read()  # Read the analog value from pin A2

    # Check if readings are ready
    if pin1_value is None or pin2_value is None:
        print("Waiting for sensor data...")  # Output message if data is not ready
        time.sleep(0.5)  # Wait for 0.5 seconds before retrying
        continue  # Skip the rest of the loop and start over

    # Convert readings to voltages
    volts1 = power * pin1_value  # Calculate the voltage from the analog value for A1
    volts2 = power * pin2_value  # Calculate the voltage from the analog value for A2

    # Calculate Vm, Vb, Ru
    Vm = power - (volts1 - volts2)  # Calculate Vm based on voltage readings
    Vb = power  # Vb is the reference voltage (assumed as power)
    Ru = (R1 * (Vb - Vm)) / Vm  # Calculate the resistance value Ru

    # Calculate temperature (T)
    try:
        T = (Ru / (R0 * alpha)) - (1 / alpha)  # Calculate temperature in Celsius
        print(f"Temperature: {T:.2f}")  # Print the temperature
    except ZeroDivisionError:
        print("Error: Division by zero encountered in temperature calculation.")  # Error handling

    time.sleep(1)  # Wait for 1 second before the next loop iteration
