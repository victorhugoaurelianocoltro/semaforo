from machine import Pin
from utime import sleep

# LEDs conectados nos pinos
vermelho = Pin(15, Pin.OUT)
amarelo = Pin(16, Pin.OUT)
verde = Pin(17, Pin.OUT)

# Funções para cada cor do semáforo
def ligar_verde():
    print("LED VERDE LIGADO!")
    verde.on()
    sleep(20)
    verde.off()
    print("LED VERDE DESLIGADO!")

def ligar_amarelo():
    print("LED AMARELO LIGADO!")
    amarelo.on()
    sleep(10)
    amarelo.off()
    print("LED AMARELO DESLIGADO!")

def ligar_vermelho():
    print("LED VERMELHO LIGADO!")
    vermelho.on()
    sleep(7)
    vermelho.off()
    print("LED VERMELHO DESLIGADO!")

# Início do programa
print("Sistema de Semáforo Iniciado!")

while True:
    ligar_verde()
    sleep(0.5)
    
    ligar_amarelo()
    sleep(0.5)

    ligar_vermelho()
    sleep(0.5)
