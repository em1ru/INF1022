
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


if umidade < 40:
    alerta('Monitor', "Ar seco detectado")
else:
    alerta('Monitor', "Ar molhado detectado")