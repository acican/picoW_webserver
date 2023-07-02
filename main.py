import machine
import socket
import math
import utime
import network
import time
 
# led
led=machine.Pin(20,machine.Pin.OUT)

def read_html():
    page = open("index.html", "r")
    html = page.read()
    page.close()
    return(html)

def get_ip():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect("DIGI_45cb30","5932ba34")
    ip = None
 
    # Wait for connect or fail
    wait = 10
    while wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        wait -= 1
        print('waiting for connection...')
        time.sleep(1)
 
    # Handle connection error
    if wlan.status() != 3:
        raise RuntimeError('wifi connection failed')
    else:
        print('connected')
        ip=wlan.ifconfig()[0]
        print('IP: ', ip)
        
    return(ip)    

 
def handle_req(connection):
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        try:
            request = request.split()[1]
        except IndexError:
            pass
        
        value = ""
        if request == '/?on':
            led.high()
            value = 'ON'
        elif request == '/?off':
            led.low()
            value = 'OFF'
      
        html = read_html()
        
        client.send(html.encode())
        client.close()
 
def open_socket(ip):
    # Open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    print(connection)
    return(connection)
 
if __name__ == "__main__":
    ip = get_ip()
    try:
        if ip is not None:
            connection=open_socket(ip)
            handle_req(connection)
    except KeyboardInterrupt:
        machine.reset()