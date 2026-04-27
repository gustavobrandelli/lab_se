# Experimento 3 — LDR e Histerese
# Professor: Prof. Me. João Miguel Lac Roehe
# Aluno: gustavo brandelli  Data: _20/_04/2026
#
# ---------------------------------------------------------------
# ETAPA 1 (Intermediária): Leia o LDR e imprima o valor bruto no Shell.
# ETAPA 2 (Final): Implemente a Histerese (Limiar Alto e Limiar Baixo).
# ---------------------------------------------------------------

# REFLEXÃO (Obrigatório):
# Como a utilização de dois limiares (Histerese) melhora a estabilidade 
# do sistema em comparação a um limiar único?
# Resposta: evita a variacao aleatoria, com dois parametreos ha uma faixa de trabalho


from machine import Pin, ADC
from time import sleep

ldr = ADC(Pin(1))
ldr.atten(ADC.ATTN_11DB)
led = Pin(13, Pin.OUT)

# Definição dos limiares (ajuste conforme seu ambiente)
LIMIAR_ALTO = 2500
LIMIAR_BAIXO = 1500

while True:
    valor = ldr.read()
    
    # --- Etapa 1 ---
    print(valor)
    
    # --- Etapa 2 ---
    if valor > LIMIAR_ALTO:
        led.on()
    elif valor < LIMIAR_BAIXO:
        led.off()
    
    sleep(0.1)