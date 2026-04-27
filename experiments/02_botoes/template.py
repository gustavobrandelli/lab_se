# Experimento 2 — Botões
# Professor: Prof. Me. João Miguel Lac Roehe
# Aluno:Gustavo Brandelli  Data: _20/_04/2026
#
# ---------------------------------------------------------------
# ETAPA 1 (Intermediária): Imprima "Botão pressionado" ao apertar SW1.
# ETAPA 2 (Final): Use o botão SW1 para ligar/apagar o LED Azul (D12).
# ---------------------------------------------------------------

# REFLEXÃO (Obrigatório):
# O que aconteceria se não usássemos o 'sleep(0.2)' (debounce) após detectar 
# o pressionamento do botão? Como isso afetaria a lógica de 'Toggle'?
# Resposta: sem o intervalo, o comando pode ser interpretado como diversos clicks, executando o led varias vezes no mesmo pressionar

from machine import Pin
from time import sleep

sw1 = Pin(18, Pin.IN, Pin.PULL_UP)
led = Pin(12, Pin.OUT)

estado_led = False

while True:
    if sw1.value() == 0:
        # --- Etapa 1 ---
        print("Botão pressionado")

        # --- Etapa 2 ---
        estado_led = not estado_led   

        if estado_led:
            led.on()
        else:
            led.off()

        sleep(0.2)  

    sleep(0.01)