
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


alerta('Celular', "Hora de acordar!")