# Dados números inteiros n e k, com k >= 0, calcular n elevado a k. Por exemplo, dados os números 3 e 4 o seu programa deve escrever o número 81.

def main():
    n = int(input("Digite o primeiro número: "))
    k = int(input("Digite o segundo número: "))
    r = 1
    i = 0
    
    while (i<k):
        r = r*n
        i = i+1
        
    print("O resultado eh: ", r)
  
main()
