# Dado um número inteiro n >= 0, calcular n!
def main():
    i = 1
    mult = 1
    n = int(input("Digite o número: "))
    
    while (i!=0):
        mult = n * mult
        n = n - 1
        
        if (n==1):
            i=0
        
    print("O valor do fatorial é:", mult)
  
main()
