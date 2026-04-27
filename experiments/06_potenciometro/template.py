# Experimento 6 — Dimer com Potenciômetro
# Professor: Prof. Me. João Miguel Lac Roehe
# Aluno: Gustavo Brandelli  Data: 22/04/2026
#
# ---------------------------------------------------------------
# ETAPA 1 (Intermediária): Exiba no Shell o valor do pot. em % (0-100).
# ETAPA 2 (Final): Controle o brilho do LED Azul (D12) com PWM.
# ---------------------------------------------------------------

# REFLEXÃO (Obrigatório):
# Descreva o fluxo de dados deste experimento: como o valor analógico do 
# potenciômetro se transforma em brilho variável no LED?
# Resposta: leitura do pot é lida em formato adc e convertido pra pwm, controlando o brilho variavel conforme tensao
from machine import ADC, Pin, PWM
from time import sleep
from utils import map_value

# Configuração do Potenciômetro no GPIO 36 (VP)
pot = ADC(Pin(36))
pot.atten(ADC.ATTN_11DB) # Configura para ler até 3.3V

# Configuração do LED Azul no GPIO 12 com PWM
led_pin = Pin(12, Pin.OUT)
led = PWM(Pin(12), freq=1000)

while True:
    valor = pot.read() #Le valor do potenciometro
    porcento = (valor / 4095) * 100
    print(f"Potenciômetro: {porcento:.1f}%")#printa valor do potenciometro
    brilho = map_value(valor, 0, 4095, 0, 1023)#mapeia o range do led sendo convertido conforme formula do pwm
    led.duty(brilho)#muda o brilho do led
    
    sleep(0.05)