from machine import ADC, Pin, PWM
from time import sleep
from utils import map_value

# Configura Potenciômetro
adc = ADC(Pin(A0))
adc.atten(ADC.ATTN_11DB)

# Configura LED Azul para PWM
led_pwm = PWM(Pin(12))
led_pwm.freq(1000)

print("Controle de brilho do LED Azul via Potenciômetro")

while True:
    valor = adc.read()  # 0..4095
    
    # Mapeia 0-4095 (ADC) para 0-1023 (PWM Duty)
    brilho = map_value(valor, 0, 4095, 0, 1023)
    
    led_pwm.duty(brilho)
    
    por = int((valor / 4095) * 100)
    print("Pot: {} | Brilho: {} | {}%".format(valor, brilho, por))
    
    sleep(0.05)
