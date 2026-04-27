import network
import time
import socket
from machine import ADC, Pin

ldr = ADC(Pin(1))
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

sta_if.connect('PEIXE_195_2G','casabrandelli')

while not sta_if.isconnected():
    print("conectandoo...")
    time.sleep(1)
    
print('conectado')
print('configuraacoes de rede : '+str(sta_if.ifconfig()))

valor_ldr = ldr.read()

def web_page():
    valor = ldr.read()
    html = """<html><head><meta charset="utf-8"><title>ESP32 Lab</title></head>
    <body><h1>Laboratório Embarcados Tutoria - Gustavo Brandelli</h1>
    <p>Valor do ldr: <strong>{}</strong></p>
    <script>setTimeout(function(){{location.reload();}}, 2000);</script>
    </body></html>""".format(valor)
    return html



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
    
    
