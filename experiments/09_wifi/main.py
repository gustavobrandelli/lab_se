import network
import socket
from machine import ADC, Pin
import time

# Configurações de Wi-Fi
SSID = "PEIXE_195_2G"
PASSWORD = "casabrandelli"

# Componentes
led_azul = Pin(12, Pin.OUT)

def conecta_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Conectando ao Wi-Fi...')
        wlan.connect(SSID, PASSWORD)
        while not wlan.isconnected():
            pass
    print('Conectado! IP:', wlan.ifconfig()[0])
    return wlan.ifconfig()[0]

def web_page():
    valor = pot.read()
    html = """<html><head><meta charset="utf-8"><title>ESP32 Lab</title></head>
    <body><h1>Laboratório IoT - Prof. João Miguel</h1>
    <p>Valor do Potenciômetro: <strong>{}</strong></p>
    <script>setTimeout(function(){{location.reload();}}, 2000);</script>
    </body></html>""".format(valor)
    return html

ip = conecta_wifi()

# Inicia Server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    print('Conexão de %s' % str(addr))
    request = conn.recv(1024)
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
