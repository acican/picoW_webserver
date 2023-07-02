import socket
import network

# Set up Wi-Fi connection
ssid = 'your_wifi_ssid'
password = 'your_wifi_password'

def connect_to_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Connecting to Wi-Fi...')
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print('Wi-Fi connected:', sta_if.ifconfig())

def handle_request(client_sock):
    request = client_sock.recv(1024)
    # Process the request and generate a response
    response = "HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\nHello, World!"
    client_sock.send(response.encode())
    client_sock.close()

def run_server():
    connect_to_wifi()
    
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind(('0.0.0.0', 80))
    server_sock.listen(1)
    print('Server listening on port 80...')
    
    while True:
        client_sock, client_addr = server_sock.accept()
        print('Client connected:', client_addr)
        handle_request(client_sock)

run_server()
