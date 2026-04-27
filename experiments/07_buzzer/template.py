# Experimento 7 — Buzzer e Sons
# Professor: Prof. Me. João Miguel Lac Roehe
# Aluno:Gustavo Brandelli Data: 22/04/2026
#
# ---------------------------------------------------------------
# ETAPA 1 (Intermediária): Faça o buzzer emitir um som fixo por 1s.
# ETAPA 2 (Final): Crie dois tons diferentes, um para cada botão.
# ---------------------------------------------------------------

# REFLEXÃO (Obrigatório):
# Qual a diferença técnica entre controlar um LED (brilho) e um Buzzer (som) 
# usando PWM no MicroPython? O que o parâmetro 'freq' altera no som?
# Resposta: no led o pwm varia o tempo ligado controlando a media, no buzzer o pwm varia a frequencia pra controlar o tom

from machine import Pin, PWM
import time

# Configuração do Buzzer (GPIO 5) como PWM
buzzer = PWM(Pin(5))

# Configuração dos Botões
sw1 = Pin(18, Pin.IN, Pin.PULL_UP)
sw2 = Pin(19, Pin.IN, Pin.PULL_UP)

# ETAPA 1: Som fixo (1000Hz) por 1 segundo ao iniciar
buzzer.freq(1000)#liga som
buzzer.duty(1023)  #liga som
time.sleep(1)#sleep 1s
buzzer.duty(0)#desliga soom 
time.sleep(2)

while True:
    # ETAPA 2: Tons diferentes para cada botão
    if sw1.value() == 0:     # Botão 1 pressionado nota 1
        buzzer.freq(440)     
        buzzer.duty(1023)
    elif sw2.value() == 0:   # Botão 2 pressionado nota 2
        buzzer.freq(880)     
        buzzer.duty(1023)
    else:
        buzzer.duty(0)
    
    time.sleep(1)