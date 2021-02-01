# Dada uma sequência de números inteiros diferentes de zero, terminada por um zero, calcular a sua soma. Por exemplo, para a sequência: 12   17   4   -6   8   0 o seu programa deve escrever o número 35.
def main():
    i = 1
    soma = 0
    
    while (i!=0):
        n = int(input("Digite o número: "))
        soma = n + soma
        
        if (n==0):
            i=0
        
    print("O resultado da soma dos números é: ", soma)
  
main()
