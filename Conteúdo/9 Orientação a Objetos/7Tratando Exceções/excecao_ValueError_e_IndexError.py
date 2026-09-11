try:
    num = int(input("Entre com um número inteiro: "))
    print(num)
except ValueError:
    print("Mensagem 1")
except IndexError:
    print("Mensagem 2")
except Exception:
    print("Mensagem 3")