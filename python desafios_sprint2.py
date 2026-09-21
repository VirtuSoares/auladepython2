---

### Ficheiro 2: `desafios_sprint2.py`

```python
"""
Desafio Sprint 2 - Exercícios Práticos da Semana 02
Estruturas de Controlo e Repetição em Python (PEP 8).
"""

def desafio_1_classificador_cliente():
    print("\n--- Desafio 1: Classificador de Cliente ---")
    idade = int(input("Digite a idade do cliente: "))
    renda = float(input("Digite a renda mensal do cliente (R$): "))

    if renda >= 10000 and idade >= 30:
        categoria = "Diamante"
    elif renda >= 5000:
        categoria = "Ouro"
    elif renda >= 2500:
        categoria = "Prata"
    else:
        categoria = "Bronze"

    print(f"O cliente tem {idade} anos, renda de R$ {renda:.2f} e foi classificado como: {categoria}")


def desafio_2_menu_operacoes():
    print("\n--- Desafio 2: Menu de Operações Matemáticas ---")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    print("\n[1] Soma (+)")
    print("[2] Subtração (-)")
    print("[3] Multiplicação (*)")
    print("[4] Divisão (/)")
    opcao = input("Escolha uma opção (1-4): ").strip()

    match opcao:
        case "1":
            resultado = num1 + num2
            print(f"Resultado da soma: {num1} + {num2} = {resultado:.2f}")
        case "2":
            resultado = num1 - num2
            print(f"Resultado da subtração: {num1} - {num2} = {resultado:.2f}")
        case "3":
            resultado = num1 * num2
            print(f"Resultado da multiplicação: {num1} * {num2} = {resultado:.2f}")
        case "4":
            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado da divisão: {num1} / {num2} = {resultado:.2f}")
            else:
                print("Erro: Não é possível dividir por zero!")
        case _:
            print("Opção inválida! Escolha um número entre 1 e 4.")


def desafio_3_analise_numeros():
    print("\n--- Desafio 3: Análise de Números ---")
    soma = 0
    maior = None
    menor = None
    total_numeros = 5

    for i in range(1, total_numeros + 1):
        numero = float(input(f"Digite o {i}º número: "))
        soma += numero

        if maior is None or numero > maior:
            maior = numero
        if menor is None or numero < menor:
            menor = numero

    media = soma / total_numeros

    print("\n--- Resultado da Análise ---")
    print(f"Soma total: {soma:.2f}")
    print(f"Média: {media:.2f}")
    print(f"Maior valor: {maior:.2f}")
    print(f"Menor valor: {menor:.2f}")


def desafio_4_sistema_autenticacao():
    print("\n--- Desafio 4: Sistema de Autenticação ---")
    senha_correta = "1234"
    tentativas = 0
    limite_tentativas = 3
    autenticado = False

    while tentativas < limite_tentativas and not autenticado:
        senha_digitada = input("Digite a sua palavra-passe: ")
        tentativas += 1

        if senha_digitada == senha_correta:
            autenticado = True
            print(f"Acesso concedido! Autenticado com sucesso na tentativa {tentativas}.")
        else:
            tentativas_restantes = limite_tentativas - tentativas
            if tentativas_restantes > 0:
                print(f"Palavra-passe incorreta! Restam {tentativas_restantes} tentativa(s).")
            else:
                print("Acesso bloqueado! Número máximo de tentativas atingido.")


def main():
    print("========================================")
    print("      ENTREGÁVEL - SPRINT 2 PYTHON      ")
    print("========================================")

    desafio_1_classificador_cliente()
    desafio_2_menu_operacoes()
    desafio_3_analise_numeros()
    desafio_4_sistema_autenticacao()

    print("\n========================================")
    print("   TODOS OS DESAFIOS FORAM CONCLUÍDOS   ")
    print("========================================")


if __name__ == "__main__":
    main()
