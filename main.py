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

if __name__ == "__main__":
    N = 150
    x = 3
    N_visual = x**2

    approximation,terms = naive_erf(x,N)

    print("===Naive Approximation (Compensation)===")
    print(f"Naive Approximation of Erf({x}) for  N = {N}: {approximation}")
    print(f"List of terms up until term  #{N_visual}: \\")
    print(terms[:N_visual])
