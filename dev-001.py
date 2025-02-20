import socket

# Replace with the IP address of your DI-710 device
DEVICE_IP = '192.168.1.100'
DEVICE_PORT = 2101  # Default port for DI-710

def main():
    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the DI-710 device
        s.connect((DEVICE_IP, DEVICE_PORT))
        print(f'Connected to DI-710 at {DEVICE_IP}:{DEVICE_PORT}')

        # Send a command to start data acquisition
        # Refer to the DI-710 protocol documentation for specific command formats
        start_command = b'START\r'  # Example command; replace with actual
        s.sendall(start_command)

        try:
            while True:
                # Receive data from the device
                data = s.recv(1024)
                if not data:
                    break
                # Process and display the received data
                print('Received:', data.decode())
        except KeyboardInterrupt:
            print('Data acquisition stopped.')

        # Send a command to stop data acquisition
        stop_command = b'STOP\r'  # Example command; replace with actual
        s.sendall(stop_command)
        print('Disconnected from DI-710.')

if __name__ == '__main__':
    main()