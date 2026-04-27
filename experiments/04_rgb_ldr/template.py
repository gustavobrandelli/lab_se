# Experimento 4 — RGB e PWM
# Professor: Prof. Me. João Miguel Lac Roehe
# Aluno: gustavo brandelli Data: _20/_04/_2026
#
# ---------------------------------------------------------------
# ETAPA 1 (Intermediária): Faça o LED Verde (GPIO 10) brilhar com 50% (duty 512).
# ETAPA 2 (Final): Use map_value para brilho proporcional ao LDR.
# ---------------------------------------------------------------

# REFLEXÃO (Obrigatório):
# Explique com suas palavras: Por que usamos a função map_value em vez de 
# apenas usar o valor direto do LDR no duty do PWM?
# Resposta: sem mapear,  o brilho do led nao apresentaria intensidade correta,  usando o map valued definimos

from machine import Pin, ADC, PWM
from time import sleep


def map_value(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

led_verde = PWM(Pin(10), freq=1000)
ldr = ADC(Pin(1))

while True:
    led_verde.duty(512)
    sleep(2)
    
    
    valor_ldr = ldr.read()
    
    brilho = map_value(valor_ldr, 0, 4095, 0, 1023)
    led_verde.duty(int(brilho))
    
    sleep(4)
    
    
    