# ANED_ERF



# Erf

**Boris OUYA**

*July 2024*

## Problem 1.4.1 Demailly

Soit \(x \geq 0\) ; on note \( F(x) = \frac{2}{\sqrt{\pi}} \int_{0}^{x} e^{-t^2} dt\).

### Encadrer F(x) par deux entiers consécutifs

Sur  \(\mathbb{R}_+ \), la fonction \(x \rightarrow e^{-t^2}\) est positive. Ainsi, la fonction \(F(x)\) est croissante sur \(\mathbb{R}_+\). Alors, on a pour tout \(x \geq 0\)
\[ 
F(0) \leq F(x) \leq \lim_{x \to \infty} F(x)
\]

Or, un résultat bien connu (intégrale de Gauss) est que 
\[ 
\lim_{x \to \infty}  \int_{0}^{x} e^{-t^2} dt = \frac{\sqrt{\pi}}{2}
\] 
Et 
\[ 
F(0) = \int_{0}^{0} e^{-t^2} dt = 0
\]
Alors, on a au final pour \(x \geq 0\)
\[ 
0 \leq F(x) \leq 1
\]

### En remplaçant \(e^{-t^2}\) par un développement en série entière de x, exprimez F(x) comme somme d'une série.

On a 
\[ 
e^{-t^2} = \sum_{n=0}^{\infty} (-1)^n\frac{x^{2n}}{n!}
\]

Alors, en intégrant, on a :
\[ 
F(x) = \sum_{n=0}^{\infty} (-1)^n \frac{2 x^{2n +1}}{\sqrt{\pi}(2n+1)n!}
\]

### On choisit x = 3 ; calculer les 10 premiers termes de la série. En déduire que pour \(x \geq 3\) on a un phénomène de compensation dans le calcul de la somme des premiers termes de la série.

On effectue les calculs avec un script Python. Voici les résultats:

- \(a_0 = 3.385137501286538\)
- \(a_1 = -10.155412503859614\)
- \(a_2 = 27.419613760420958\)
- \(a_3 = -58.756315200902044\)
- \(a_4 = 102.8235516015786\)
- \(a_5 = -151.43104872232485\)
- \(a_6 = 192.20094645525845\)
- \(a_7 = -214.16676890728797\)
- \(a_8 = 212.5920132535579\)
- \(a_9 = -190.21390659528868\)

Nous remarquons que nous retrouvons un maximum en terme de valeur absolue (vérifiable analytiquement) en \(a_7 = -214.16676890728797\). Cependant, nous savons que \(F(3)\) est compris entre 0 et 1. La différence d'échelle implique que nous avons un phénomène de compensation dans le calcul de la somme, ce qui nuit à la précision du calcul. Pour \(x \geq 3\), remarquons que les termes aux mêmes indices sont inévitablement supérieurs ou égaux à ceux pour \(x = 3\). Ainsi, le phénomène de compensation s'applique aussi.

### On définit \(g(x)\) par \(F(x) = e^{-x^2} g(x)\). Montrer que g est solution d'une équation différentielle.

Nous avons pour \(x \geq 0\)
\[ 
g(x) = F(x)e^{x^2}
\]

Ainsi, en dérivant, nous trouvons
\[ 
g'(x) = F'(x)e^{x^2} + 2xF(x)e^{x^2}
\]

Or
\[ 
F'(x) = \frac{2}{\sqrt{\pi}} e^{-x^2}
\]

et sachant que
\[ 
g(x) = F(x)e^{x^2}
\]

On a
\[ 
g'(x) = \frac{2}{\sqrt{\pi}} + 2x g(x)
\]

Ainsi, \(g\) est une solution de l'équation différentielle:
\[ 
y' = \frac{2}{\sqrt{\pi}} + 2xy
\]

### Exprimer g(x) comme somme d'une série entière en x.

La formule générale est
\[ 
g(x) = \sum_{n=0}^{\infty} \frac{ g^{(n)}(0)}{n!} x^n
\]

Sachant que pour \(x \geq 0\)
\[ 
g'(x) = \frac{2}{\sqrt{\pi}} + 2xg(x)
\]

On a pour \(n \geq 2\) en utilisant la formule de Leibnitz:
\[ 
g^{(n)}(x) = g'^{(n-1)}(x) = 2\sum_{k=0}^{n-1} \binom{n-1}{k} (x)^{(k)} g^{(n-1-k)}(x) = 2[x g^{(n-1)}(x) + (n-1)g^{(n-2)}(x)]
\]

On a
- \(g(0) = F(0)e^0 = 0\)
- \(g'(0) = \frac{2}{\sqrt{\pi}}\)
- \(g''(0) = 2[0 * \frac{2}{\sqrt{\pi}} + 1 *  0 ] = 0\)
- \(g^{(3)}(0) = 2 * 2 * \frac{2}{\sqrt{\pi}} = \frac{8}{\sqrt{\pi}}\)
- ...

Nous pouvons prouver par récurrence que pour \(n \in \mathbb{N}\)
- \(g^{(2n)}(0) = 0\)
- \(g^{(2n+1)}(0) = 4ng^{(2n-1)}(0)\)

On définit alors la suite \((v_n)_{n \in \mathbb{N}}\) par 
- \(v_0 =  \frac{2}{\sqrt{\pi}}\)
- \(v_n = 4nv_{n-1}\) pour \(n \geq 1\)

Donc, on a pour \(n \in \mathbb{N}\)
\[ 
v_n = \frac{2}{\sqrt{\pi}} 4^nn!
\]

Et ainsi, on a
\[ 
g(x) = \sum_{n=0}^{\infty} 2\frac{4^nn!}{\sqrt{\pi}(2n + 1)!} x^{2n+1}
\]

### En déduire l'expression  \(F(x) = \sum_{n=0}^{\infty} a_n(x)\) où les \(a_n(x)\) sont tous positifs. Déterminer \(a_0(x)\) et donner la solution de récurrence entre \(a_n(x)\) et \(a_{n-1}(x)\).

On a 
\[ 
F(x) = e^{-x^2}g(x)
\]

Donc
\[ 
F(x) =  \sum_{n=0}^{\infty} 2\frac{4^nn!}{\sqrt{\pi}(2n + 1)!}e^{-x^2} x^{2n+1}
\]

Et on pose
\[ 
a_n(x) := 2\frac{4^nn!}{\sqrt{\pi}(2n + 1)!}e^{-x^2} x^{2n+1}
\]

On a
- \(a_{0}(x) = \frac{2}{\sqrt{\pi}} e^{-x^2}x\)
- \(a_n(x) = \frac{4n}{(2n+1)(2n)} x^2 a_{n-1}\) pour \(n \geq 1\)

### Montrer l'inégalité \(\sum_{n = N+1}^{\infty} a_n(x) \leq a_N(x) \frac{x^2}{N - x^2}\) (\(N > x^2\))

On a 
\[ 
\sum_{n=N+1}^{\infty} a_n(x) = \sum_{n=N+1}^{\infty} \frac{4n}{(2n+1)(2n)} x^2 a_{n-1}(x) \leq  \sum_{n=N+1}^{\infty} \frac{x^2}{N} a_{n-1}(x)
\]

Soit la suite \((b_n(x))_{n \in \mathbb{N}, n \geq N}\) définie par
- \(b_N(x) = a_N(x)\)
- \(b_n(x) = \frac{x^2}{N} b_{n-1}(x)\) pour \(n > N\)

Ainsi, on
\[ 
\sum_{n=N+1}^{\infty} a_n(x) \leq \sum_{n=N+1}^{\infty} b_n(x) \leq  \sum_{n=N}^{\infty} \frac{x^2}{N} a_{n}(x) = \frac{x^2}{N} a_N(x) \frac{1}{1 - \frac{x^2}{N}} \leq a_N(x) \frac{x^2}{N - x^2}
\]
