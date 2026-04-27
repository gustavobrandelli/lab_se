# Experimento 5 — Sensor LM35
# Professor: Prof. Me. João Miguel Lac Roehe
# Aluno: Gustavo Brandelli Data: 27/04/2026
#
# ---------------------------------------------------------------
# ETAPA 1 (Intermediária): Converta 'leitura' em 'tensao' (V).
# ETAPA 2 (Final): Use media_amostras() e exiba em Celsius.
# ---------------------------------------------------------------

# REFLEXÃO (Obrigatório):
# Qual a importância de tirar a média de várias amostras (função media_amostras) 
# antes de exibir a temperatura final? O que acontece com a oscilação do valor?
# Resposta: reduzir a flutuacao mantendo a media e o valor mais proximo do real lido sem o "lixo" produzido pelo esp32 e seus calculos de memoria

from machine import Pin, ADC #importa config de pinos
from time import sleep #importa funcao sleep
from utils import media_amostras #importa utils com media_amostra da lib utils

lm35 = ADC(Pin(2)) #set sensor pino ADC 2 do shield

lm35.atten(ADC.ATTN_11DB)

print("Iniciando leitura do Sensor LM35...")
print("------------------------------------")

while True:
    #TODO:ETAPA 2: Obtém a média de 20 amostras para estabilizar a leitura
    leitura = media_amostras(lm35, 20)
    
    #TODO:ETAPA 1: Converte o valor binário (0-4095) em Voltagem (0V - 3.3V)
    tensao = (leitura / 4095) * 3.3
    # Dividir por 0.01 é o mesmo que multiplicar por 100
    temperatura = tensao / 0.1#coonversao tensao pela temperatura
    print("Temp: {:.1f} C".format(temperatura))#exibe temperatura
    print("Tensao: {:.1f} ".format(tensao))#exibe tensao lidaa 
    sleep(1)