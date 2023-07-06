import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('Connected to server')

if __name__ == '__main__':
    server_ip = '172.168.0.164'
    sio.connect('http://{}:5000'.format(server_ip))
    
    while True:
        message = input('Enter a message (or type "exit" to quit): ')
        if message == 'exit':
            break
        sio.emit('message', message)

    sio.disconnect()
