import ply.lex as lex

tokens = (
    'NUM', 'BOOL', 'ID', 'STRING',
    'SET', 'SE', 'ENTAO', 'SENAO', 'DISPOSITIVO',
    'LIGAR', 'DESLIGAR', 'ENVIAR', 'ALERTA', 'PARA', 'TODOS',
    'OPLOGIC', 'E', 'IGUAL', 'VIRG', 'PONTO', 'DOISPT', 'ABRECH', 'FECHACH', 'ABREPAR', 'FECHAPAR'
)

reserved = {
    'set': 'SET',
    'se': 'SE',
    'entao': 'ENTAO',
    'senao': 'SENAO',
    'dispositivo': 'DISPOSITIVO',
    'ligar': 'LIGAR',
    'desligar': 'DESLIGAR',
    'enviar': 'ENVIAR',
    'alerta': 'ALERTA',
    'para': 'PARA',
    'todos': 'TODOS',
    'TRUE': 'BOOL',
    'FALSE': 'BOOL'
}

t_OPLOGIC = r'==|!=|>=|<=|>|<'
t_E = r'&&'
t_IGUAL = r'='
t_VIRG = r','
t_PONTO = r'\.'
t_DOISPT = r':'
t_ABRECH = r'\{' 
t_FECHACH = r'\}'
t_ABREPAR = r'\('
t_FECHAPAR = r'\)'

def t_STRING(t):
    r'"([^\\\n]|(\\.))*?"'
    t.value = t.value[1:-1]
    return t

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    if t.type == 'BOOL':
        t.value = True if t.value == 'TRUE' else False
    return t

t_ignore = ' \t\r'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caractere ilegal: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex() 