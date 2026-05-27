import math

def calcular(form):
    try:
        operacao = form.get("operacao")
        num1 = float(form.get("num1"))

        # num2 só é necessário em algumas operações
        if operacao not in ["sqrt", "log"]:
            num2 = float(form.get("num2"))
        else:
            num2 = None

        if operacao == "somar":
            resultado = num1 + num2
            conta = f"{num1} + {num2}"

        elif operacao == "subtrair":
            resultado = num1 - num2
            conta = f"{num1} - {num2}"

        elif operacao == "multiplicar":
            resultado = num1 * num2
            conta = f"{num1} * {num2}"

        elif operacao == "dividir":
            if num2 == 0:
                return None, "Erro: divisão por zero!"
            resultado = num1 / num2
            conta = f"{num1} / {num2}"

        elif operacao == "potencia":
            resultado = num1 ** num2
            conta = f"{num1} ^ {num2}"

        elif operacao == "sqrt":
            if num1 < 0:
                return None, "Erro: raiz de número negativo!"
            resultado = math.sqrt(num1)
            conta = f"√{num1}"

        elif operacao == "log":
            if num1 <= 0:
                return None, "Erro: logaritmo só para números positivos!"
            resultado = math.log(num1)
            conta = f"log({num1})"

        else:
            return None, "Operação inválida!"

        return f"{conta} = {resultado}", None

    except ValueError:
        return None, "Erro: insira valores válidos!"