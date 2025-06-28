
def ligar(device):
    print(f"{device} ligado!")

def desligar(device):
    print(f"{device} desligado!")

def alerta(device, msg):
    print(f"{device} recebeu o alerta:")
    print(msg)

def alerta(device, msg, var):
    print(f"{device} recebeu o alerta:")
    print(f"{msg} {var}")
temperatura = 40
potencia = 90

alerta('Termometro', "Temperatura em", temperatura)
alerta('ventilador', "Temperatura em", temperatura)
if temperatura > 30:
    ligar('ventilador')
potencia = 90
temperatura = 40