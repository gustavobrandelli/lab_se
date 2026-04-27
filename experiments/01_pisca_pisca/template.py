# Experimento 1 — Pisca-pisca com LEDs
# Professor: Prof. Me. João Miguel Lac Roehe
# Aluno: Gustavo Brandelli Data: 20/04/2026
#
# ---------------------------------------------------------------
# ETAPA 1 (Intermediária): Faça apenas o LED Azul (D12) piscar.
# ETAPA 2 (Final): Faça os LEDs D12 e D13 piscarem alternadamente.
# ---------------------------------------------------------------

# REFLEXÃO (Obrigatório):
# Por que o comando 'sleep' é em um loop infinito que controla LEDs?
# O que aconteceria com o consumo de CPU e a percepção visual se ele fosse removido?
# Resposta: ele induz o atraso entre execucoes. sem o loop o seu efeito visual seria muito rapido e o uso da cpu seria o maixo devido esforco continuo
from machine import Pin
from time import sleep

# TODO: Configure os pinos 12 e 13 como saída
led_azul = Pin(12, Pin.OUT)
led_vermelho = Pin(13, Pin.OUT)

while True:
    # --- Início da Etapa 1 ---
    led_vermelho.off()
    led_azul.on()      
    sleep(0.5)         

    led_azul.off()     
    sleep(0.5)         
    
    led_vermelho.off()
    led_azul.on()      
    sleep(0.5)         

    led_azul.off()     
    sleep(0.5)         
    
    
    
    # --- Início da Etapa 2 ---
    led_azul.on() 
    led_vermelho.off()
    sleep(0.5)
    
    led_azul.off()#
    led_vermelho.on()
    sleep(0.5)
    
    led_azul.on()
    led_vermelho.off()
    sleep(0.5)
    
    led_azul.off()
    led_vermelho.on()
    sleep(0.5)
