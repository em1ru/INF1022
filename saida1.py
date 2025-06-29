
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
temperatura = 31

if temperatura > 30:
    alerta('monitor', "Temperatura em ", temperatura)
alerta('celular', "Temperatura em ", temperatura)
temperatura = 31