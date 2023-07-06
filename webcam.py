from dronekit import connect, VehicleMode
import time
connection_string = 'COM7' # Replace with the serial port of your Pixhawk
baud_rate = 57600 # Replace with the baud rate that your Pixhawk is configured to use
vehicle = connect(connection_string, baud=baud_rate, wait_ready=True)
def arm_and_set_guided_mode():
    print("Arming motors...")
    vehicle.mode = VehicleMode("MANUAL")
    vehicle.armed = True
    time.sleep(1)
    print(vehicle.armed)
    vehicle.flush()
    # vehicle.mode = VehicleMode("GUIDED")

arm_and_set_guided_mode()
vehicle.channels.overrides['3'] = 1800 # Throttle
time.sleep(1)
vehicle.channels.overrides['1'] = 1500
vehicle.channels.overrides['3'] = 1500
time.sleep(1)