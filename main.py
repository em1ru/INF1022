from obsact_parser import parser

def main():
    import sys
    if len(sys.argv) != 3:
        print("Uso: python main.py <arquivo.obsact> <saida.py>")
        return
    with open(sys.argv[1], encoding='utf-8') as f:
        data = f.read()
    result = parser.parse(data)
    with open(sys.argv[2], 'w', encoding='utf-8') as f:
        f.write(result)
    print(f"Código Python gerado em {sys.argv[2]}")

if __name__ == "__main__":
    main() 