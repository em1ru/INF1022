# Analisador Sintático ObsAct → Python

## Como usar

1. Instale o PLY:
   ```
   pip install ply
   ```

2. Execute o analisador:
   ```
   python main.py exemplos/exemplo.obsact saida.py
   ```

3. O arquivo `saida.py` conterá o código Python gerado.

## Sobre

- O analisador lê um programa ObsAct e gera um programa Python equivalente.
- Suporta broadcast, condições, atribuições, ligar/desligar, alerta, etc.
- As funções obrigatórias já são geradas no início do código Python. 