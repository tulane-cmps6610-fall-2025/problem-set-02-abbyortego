  # CMPS 6610 Problem Set 02
## Answers

**Name:**_________________________


Place all written answers from `assignment-01.md` here for easier grading.

1. **Asymptotic notation**
- If $\log n! \in \theta(n \log n)$ then $\log n! \in \mathcal{O}(n \log n)$ AND $\log n! \in \mathcal{\Omega}(n \log n)$
  - $\log n! \in \mathcal{O}(n \log n)$ iff there exists $c>0, n_0 > 0$ such that $\log n! \leq c n \log n$ for all $n>0$
    - $\log n! \leq c n \log n$, Let $c=1, n_0=1$
    - $\log(1!) \leq 1 * 1 \log(1)$
    - $0 \leq 0$, True. Thus, $\log n! \in \mathcal{O}(n \log n)$.
  - $\log n! \in \mathcal{\Omega}(n \log n)$  iff there exists $c>0, n_0 > 0$ such that $\log n! \geq c n \log n$ for all $n>0$
    - $\log n! \geq c n \log n$, Let $c=1, n_0=1$
    - $\log(1!) \geq 1 * 1 \log(1)$
    - $0 \geq 0$, True. Thus, $\log n! \in \mathcal{\Omega}(n \log n)$.
  - Since $\log n! \in \mathcal{O}(n \log n)$ and $\log n! \in \mathcal{\Omega}(n \log n)$ are both true, $\log n! \in \theta(n \log n)$. 

2. **Algorithm Selection**
- $T(n) = 2T(\frac{n}{6}) + 1$
  - $C\texttt{(Root)} = 1$
  - $C\texttt{(1st Level)} = 2(2T(\frac{n}{12}) + 1) + 1$
    - $= 2^2T(\frac{n}{12}) + 2 + 1$
  - Cost is increasing so this is leaf dominated. 
    - Number of leaves is $2^{\log_6 n} = n^{log_6 2}$
  - $\mathcal{O}(n^{log_6 2})$
<br>

- $T(n) = 6T(\frac{n}{4}) + n$
  - $C\texttt{(Root)} = n$
  - $C\texttt{(1st Level)} = 6(6T(\frac{n}{16}) + \frac{n}{4}) + n$
    - $= 6^2T(\frac{n}{16}) + \frac{3n}{2} + n$
  - Cost is increasing so this is leaf dominated. 
    - Number of leaves is $6^{\log_4 n} = n^{\log_4 6}$
  - $\mathcal{O}(n^{\log_4 6})$
<br>

- 

3. **More Algorithm Selection** 
 
4. **Integer Multiplication Timing Results**

5. **Black Hats and White Hats**
