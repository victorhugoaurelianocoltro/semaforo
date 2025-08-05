# 🚦 Projeto Semáforo com MicroPython

Este projeto simula um sistema de semáforo utilizando uma placa com suporte a MicroPython (como o ESP32 ou Raspberry Pi Pico), controlando três LEDs (verde, amarelo e vermelho) com tempos definidos.

## 📌 Objetivo

Criar um circuito que simula o funcionamento de um semáforo real:

- LED Verde acende por **20 segundos**
- LED Amarelo acende por **10 segundos**
- LED Vermelho acende por **7 segundos**

Entre cada troca, há um pequeno intervalo de **0,5 segundos** com todos os LEDs apagados.

---

## 🔧 Materiais Utilizados

- 1x ESP32 ou Raspberry Pi Pico
- 1x LED verde
- 1x LED amarelo
- 1x LED vermelho
- 3x resistores de 220Ω
- Jumpers (fios)
- Protoboard
- Cabo micro USB

---

## ⚙️ Conexões (Exemplo)

| Cor do LED | GPIO/PIN |
|------------|-----------|
| Verde      | 17        |
| Amarelo    | 16        |
| Vermelho   | 15        |

---

## 🧠 Lógica do Código

O código foi escrito em MicroPython e organiza o controle dos LEDs em funções, facilitando a manutenção e leitura do programa.

### Ciclo do semáforo:
1. Liga o LED verde por 20 segundos
2. Espera 0.5 segundos
3. Liga o LED amarelo por 10 segundos
4. Espera 0.5 segundos
5. Liga o LED vermelho por 7 segundos
6. Espera 0.5 segundos
7. Repete o ciclo

---

## 💻 Código Fonte

```python
from machine import Pin
from utime import sleep

vermelho = Pin(15, Pin.OUT)
amarelo = Pin(16, Pin.OUT)
verde = Pin(17, Pin.OUT)

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

print("Sistema de Semáforo Iniciado!")

while True:
    ligar_verde()
    sleep(0.5)

    ligar_amarelo()
    sleep(0.5)

    ligar_vermelho()
    sleep(0.5)
