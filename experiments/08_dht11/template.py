# Experimento 8 — Sensor DHT11 (Digital)
# Professor: Prof. Me. João Miguel Lac Roehe
# Aluno: gustavo braandelli  Data: 27/04/26
#
# ---------------------------------------------------------------
# ETAPA 1 (Intermediária): Leia e exiba Temp/Umid no Shell.
# ETAPA 2 (Final): Se a umidade for < 40%, acenda o LED Vermelho (D13).
# ---------------------------------------------------------------

# REFLEXÃO (Obrigatório):
# Por que sensores digitais como o DHT11 são considerados mais "robustos" 
# em relação a ruídos elétricos do que sensores analógicos como o LM35?
# Resposta: devido a resposta em valores 1 e 0 via rede ao inves de tensao conforme os outros, diminuindo o indice de erro de leitura
import dht
from machine import Pin
import time

sensor = dht.DHT11(Pin(4))#seta pino 4 do sensor de umidade
led_red = Pin(13, Pin.OUT)#seta saidaa led vermelho de alerta

while True:
    try:
        # ETAPA 1: Medição e leitura
        sensor.measure()#capta informacao do sensoor via lib do dht
        t = sensor.temperature()#guarda temperatura
        h = sensor.humidity()#guarda umidade
        print("Temp: {}°C  Umid: {}%".format(t, h))#imprime valor na tela
        # ETAPA 2: Controle do LED baseado na umidade
        if h < 40:# se menor que 40, liga led vermelho
            led_red.value(1) 
        else:
            led_red.value(0) #se maior, desliga led
    except OSError:
        print("Erro na leitura do sensor!")#defeito na leitura, printa mensagem
    time.sleep(2)