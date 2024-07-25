import math

def naive_erf(x,N):
    approximation = 0

    terms = []
    for n in range(N+1):    
        u = 2 * n + 1
        term = (-1)**n * (2 * x**u) / (math.sqrt(math.pi)*u*math.factorial(n))
        approximation += term
        terms.append(term)

    return approximation,terms


def better_erf(x,k):
    ak = 2 / math.sqrt(math.pi) * x * math.exp(-x**2) 
    approximation = 0
    N = 0
    while True:
        approximation += ak
        if N > x**2 and ak * x**2 /(N - x**2) <= 10**(-k):
            break
        N += 1
        ak = ak * 4*N / ((2*N +1)*(2*N)) * x**2

    return approximation

        




if __name__ == "__main__":
    N = 150
    x = 10
    N_visual = x**2 +1 
    k = 15

    approximation,terms = naive_erf(x,N)

    print("===Naive Approximation (Compensation)===")
    print(f"Naive Approximation of Erf({x}) for  N = {N}: {approximation}")
    print(f"List of terms up until term  #{N_visual}: \\")
    print(terms[:N_visual])


    approximation = better_erf(x,k)

    print("===Approximation w/o compensation===")
    print(f"Approximation of Erf({x}) with precision 10^(-{k}) : {approximation}")


    print(f"Valeur python: {math.erf(x)}")
    print(f"Différence: {abs(math.erf(3) - approximation)}")
