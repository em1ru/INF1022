import ply.yacc as yacc
from obsact_lexer import tokens

devices = []
observations = {}
cmds_code = []

def p_program(p):
    'program : devices cmds'
    funcoes = '''
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

'''
    inits = ""
    for obs in observations:
        if not observations[obs]['set']:
            inits += f"{obs} = 0\n"
    for obs in observations:
        if observations[obs]['set']:
            inits += f"{obs} = {observations[obs]['value']}\n"
    p[0] = funcoes + inits + "\n" + "\n".join(cmds_code)

def p_devices(p):
    '''devices : device devices
               | device'''
    pass

def p_device(p):
    '''device : DISPOSITIVO DOISPT ABRECH ID FECHACH
              | DISPOSITIVO DOISPT ABRECH ID VIRG ID FECHACH'''
    if len(p) == 6:
        devices.append(p[4])
    else:
        devices.append(p[4])
        observations[p[6]] = {'set': False, 'value': 0}

def p_cmds(p):
    '''cmds : cmd PONTO cmds
            | cmd PONTO'''
    if len(p) == 4:
        cmds_code.append(p[1])
    else:
        cmds_code.append(p[1])

def p_cmd(p):
    '''cmd : atrib
           | obsact
           | act'''
    p[0] = p[1]

def p_atrib(p):
    'atrib : SET ID IGUAL var'
    observations[p[2]] = {'set': True, 'value': p[4]}
    p[0] = f"{p[2]} = {p[4]}"

def p_var(p):
    '''var : NUM
           | BOOL'''
    p[0] = p[1]

def p_obsact_se_entao(p):
    'obsact : SE obs ENTAO act'
    p[0] = f"if {p[2]}:\n    {p[4]}"

def p_obsact_se_entao_senao(p):
    'obsact : SE obs ENTAO act SENAO act'
    p[0] = f"if {p[2]}:\n    {p[4]}\nelse:\n    {p[6]}"

def p_obs_obs_oplogic_var(p):
    'obs : ID OPLOGIC var'
    p[0] = f"{p[1]} {p[2]} {p[3]}"

def p_obs_and(p):
    'obs : ID OPLOGIC var E obs'
    p[0] = f"({p[1]} {p[2]} {p[3]}) and ({p[5]})"

def p_act_ligar(p):
    'act : LIGAR ID'
    p[0] = f"ligar('{p[2]}')"

def p_act_desligar(p):
    'act : DESLIGAR ID'
    p[0] = f"desligar('{p[2]}')"

def p_act_enviar_alerta_msg_device(p):
    'act : ENVIAR ALERTA ABREPAR STRING FECHAPAR ID'
    p[0] = f"alerta('{p[6]}', \"{p[4]}\")"

def p_act_enviar_alerta_msg_var_device(p):
    'act : ENVIAR ALERTA ABREPAR STRING VIRG ID FECHAPAR ID'
    p[0] = f"alerta('{p[8]}', \"{p[4]}\", {p[6]})"

def p_act_enviar_alerta_msg_para_todos(p):
    'act : ENVIAR ALERTA ABREPAR STRING FECHAPAR PARA TODOS DOISPT id_list'
    ids = p[8]
    code = ""
    for dev in ids:
        code += f"alerta('{dev}', \"{p[4]}\")\n"
    p[0] = code.strip()

def p_act_enviar_alerta_msg_var_para_todos(p):
    'act : ENVIAR ALERTA ABREPAR STRING VIRG ID FECHAPAR PARA TODOS DOISPT id_list'
    ids = p[11]
    code = ""
    for dev in ids:
        code += f"alerta('{dev}', \"{p[4]}\", {p[6]})\n"
    p[0] = code.strip()

def p_id_list(p):
    '''id_list : ID VIRG id_list
               | ID'''
    if len(p) == 4:
        p[0] = [p[1]] + p[3]
    else:
        p[0] = [p[1]]

def p_error(p):
    if p:
        print(f"Erro de sintaxe na linha {p.lineno}: token '{p.value}'")
    else:
        print("Erro de sintaxe: final inesperado do arquivo.")

parser = yacc.yacc() 