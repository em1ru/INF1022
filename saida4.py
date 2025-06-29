
def ligar(device):
    print(f"{device} ligado!")

def desligar(device):
    print(f"{device} desligado!")

def alerta(device, msg, var=None):
    print(f"{device} recebeu o alerta:")
    if var is not None:
        print(f"{msg} {var}")
    else:
        print(msg)

potencia = 100

ligar('lampada')
potencia = 100