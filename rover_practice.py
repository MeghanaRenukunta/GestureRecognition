from dronekit import connect, VehicleMode
import time
import socket


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

# Initialize the rover control
rover = vehicle  # Replace with your rover control class or logic

# Start a TCP/IP server to listen for gesture commands
host = '172.168.0.164'  # Replace with the IP address or hostname of the rover
port = 7  # Replace with the port number the rover is listening on
gesture_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
gesture_socket.bind((host, port))
gesture_socket.listen(1)

print(f"Listening for gesture commands on {host}:{port}...")
c=0
while True:
    conn, addr = gesture_socket.accept()
    print(f"Connected to gesture recognition at {addr[0]}:{addr[1]}")

    while True:
        data = conn.recv(1024)

        #print(data)
        
        if not data:
            break
        
        command = data.decode()
        print(command)
        if(not(command=='rstop')):
            continue
        c+=1
        
        if command == 'rforward':
            vehicle.channels.overrides['3'] = 1800 # Throttle
            time.sleep(1)
            vehicle.channels.overrides['1'] = 1500
            vehicle.channels.overrides['3'] = 1500
            time.sleep(1)
            # rover.move_forward()
        elif command == 'rstop':
            vehicle.channels.overrides['1'] = 1500
            vehicle.channels.overrides['3'] = 1500 # Throttle
            time.sleep(2)
        elif command== 'rright':
            vehicle.channels.overrides['1'] = 1300
            vehicle.channels.overrides['3'] = 1500
            time.sleep(0.9)
            vehicle.channels.overrides['1'] = 1500
            vehicle.channels.overrides['3'] = 1500
            time.sleep(0.1)
        elif command== 'rleft':
            vehicle.channels.overrides['1'] = 1700
            vehicle.channels.overrides['3'] = 1500
            time.sleep(1)
            vehicle.channels.overrides['1'] = 1500
            vehicle.channels.overrides['3'] = 1500
            time.sleep(0.1)
        elif command == 'rbackward':
            vehicle.channels.overrides['3'] = 1300 # Throttle
            time.sleep(1)
            vehicle.channels.overrides['1'] = 1500
            vehicle.channels.overrides['3'] = 1500
            time.sleep(1)
        elif command=='astop':
            pass
        elif command=='aforward':
            pass
        elif command=='abackward':
            pass
        elif command=='aleft':
            pass
        elif command=='aright':
            pass
        
            #vehicle.channels.overrides['3'] = 1700 
	        
	        # vehicle.channels.overrides['3'] = 2000 # Throttle
            # time.sleep(2)
        
        
	

    
    conn.close()




vehicle.flush()
# # Disarm vehicle
print("Disarming motors...")
vehicle.armed = False
vehicle.flush()

# Close connection
vehicle.close()




