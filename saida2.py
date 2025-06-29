
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

movimento = 0
umidade = 0
potencia = 100

if movimento == True:
    ligar('lampada')
else:
    desligar('lampada')
if umidade < 40:
    alerta('Monitor', "Ar seco detectado")
potencia = 100