  # CMPS 6610 Problem Set 02
## Answers

**Name:** Abby Ortego


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

- $T(n) = 7T(\frac{n}{7}) + n$
  - $C\texttt{(Root)} = n$
  - $C\texttt{(1st Level)} = 7(7T(\frac{n}{14}) + \frac{n}{7}) + n$
    - $= 7^2T(\frac{n}{14}) + n + n$
  - The cost is neither increasing nor decreasing so this is balanced.
    - Number of levels is $\log_7 n$ and the max cost per level is $n$
  - $\mathcal{O}(n \log_7 n)$
<br>

- $T(n) = 9T(\frac{n}{4}) + n^2$
  - $C\texttt{(Root)} = n^2$
  - $C\texttt{(1st Level)} = 9(9T(\frac{n}{8}) + (\frac{n}{4})^2) + n^2$
    - $= 9^2T(\frac{n}{8}) + \frac{9n^2}{16} + n^2$
  - Cost is decreasing so this is root dominated.
  - $\mathcal{O}(n^2)$
<br>

- $T(n) = 4T(\frac{n}{2}) + n^3$
  - $C\texttt{(Root)} = n^3$
  - $C\texttt{(1st Level)} = 4(4T(\frac{n}{4}) + (\frac{n}{2})^3) + n^3$
    - $= 4^2T(\frac{n}{4}) + \frac{4n^3}{8} + n^3$
  - Cost is decreasing so this is root dominated. 
  - $\mathcal{O}(n^3)$
<br>

- $T(n) = 49T(\frac{n}{25}) + n^{\frac{3}{2}} \log n$
  - $C\texttt{(Root)} = n^{\frac{3}{2}} \log n$
  - $C\texttt{(1st Level)} = 49(49T(\frac{n}{25^2}) + (\frac{n}{25})^{\frac{3}{2}}\log \frac{n}{25}) + n^{\frac{3}{2}} \log n$
    - $= 49^2T(\frac{n}{25^2}) + \frac{49n^\frac{3}{2}}{125}\log \frac{n}{25} + n^{\frac{3}{2}} \log n$
  - Cost is decreasing so this is root dominated. 
  - $\mathcal{O}(n^{\frac{3}{2}} \log n)$
<br>

- $T(n) = T(n-1) + 2$
  - $C\texttt{(Root)} = 2$
  - $C\texttt{(1st Level)} = T(n-2) + 2 + 2$
  - Cost is neither increasing nor decreasing so this is balanced.
    - Number of levels is $n$ and max cost is $2$
  - $\mathcal{O}(n)$
<br>

- $T(n) = T(n-1) + n^c$
  - $C\texttt{(Root)} = n^c$
  - $C\texttt{(1st Level)} = T(n-2) + n^c + n^c$
  - Cost is neither increasing nor decreasing so this is balanced. 
    - Number of levels is $n$ and the max cost is $n^c$
  - $\mathcal{O}(n^{c+1}) \rightarrow \mathcal{O}(n^c)$
<br>

- $T(n) = T(\sqrt n) + 1$
  - $C\texttt{(Root)} = 1$
  - $C\texttt{(1st Level)} = T(n^{\frac{1}{4}}) + 1 + 1$
  - Cost is neither increasing nor decreasing so this is balanced. 
    - Number of levels is $\log \log n$ and the max cost per level is $1$
  - $\mathcal{O}(\log \log n)$ 
<br>

3. **More Algorithm Selection** 

a. Work and Span: $T(n) = 2T(\frac{n}{5}) + n^2$ 
- $W(n) = 2W(\frac{n}{5}) + n^2$
  - $C\texttt{(Root)} = n^2$
  - $C\texttt{(1st Level)} = 2(2T(\frac{n}{25}) + (\frac{n}{5})^2) + n^2$
    - $= 2^2T(\frac{n}{25}) + \frac{2n^2}{25} + n^2$
  - Cost is decreasing so this is root dominated. 
  - $\mathcal{O}(n^2)$
- $S(n) = S(\frac{n}{5}) + n^2$
  - $C\texttt{(Root)} = n^2$
  - $C\texttt{(1st Level)} = T(\frac{n}{25}) + (\frac{n}{5})^2 + n^2$
    - $= T(\frac{n}{25}) + \frac{2n^2}{25} + n^2$
  - Cost is decreasing so this is root dominated. 
  - $\mathcal{O}(n^2)$

b. Work and Span: $T(n) = T(n-1) + \log n$
- $W(n) = W(n-1) + \log n$
  - $C\texttt{(Root)} = \log n$
  - $C\texttt{(1st Level)} = W(n-2) + \log n + \log n$
  - Cost is neither increasing nor decreasing so this is balanced.
    - Number of levels is $n$ and the max cost per level is $\log n$ 
  - $\mathcal{O}(n \log n)$
- $S(n) = S(n-1) + \log n$
  - $C\texttt{(Root)} = \log n$
  - $C\texttt{(1st Level)} = S(n-2) + \log n + \log n$
  - Cost is neither increasing nor decreasing so this is balanced.
    - Number of levels is $n$ and the max cost per level is $\log n$ 
  - $\mathcal{O}(n \log n)$

c. Work and Span: $T(n) = T(\frac{n}{3}) + T(\frac{2n}{3}) + c_1n^{1.1} + c_2$
- $W(n) = W(\frac{n}{3}) + W(\frac{2n}{3}) + c_1n^{1.1} + c_2$
  - $C\texttt{(Root)} = c_1n^{1.1} + c_2$
  - $C\texttt{(1st Level)} = [W(\frac{n}{9}) + W(\frac{2n}{9}) + c_1(\frac{n}{3})^{1.1} + c_2] + [W(\frac{2n}{9}) + W(\frac{4n}{9}) + c_1(\frac{2n}{3})^{1.1} + c_2] + c_1n^{1.1} + c_2$
    - $ = W(\frac{n}{9}) + 2W(\frac{2n}{9}) + W(\frac{4n}{9}) + (\frac{1}{3^{1.1}}+ \frac{2^{1.1}}{3^{1.1}})c_1n^{1.1}+c_2 + c_1n^{1.1} + c_2$
  - Cost is decreasing so this is root dominated.
  - $\mathcal{O}(n^{1.1})$
- $S(n) = S(\frac{n}{3}) + S(\frac{2n}{3}) + c_1n^{1.1} + c_2$
  - $C\texttt{(Root)} = c_1n^{1.1} + c_2$
  - $C\texttt{(1st Level)} = [S(\frac{n}{9}) + S(\frac{2n}{9}) + c_1(\frac{n}{3})^{1.1} + c_2] + [S(\frac{2n}{9}) + S(\frac{4n}{9}) + c_1(\frac{2n}{3})^{1.1} + c_2] + c_1n^{1.1} + c_2$
    - $ = S(\frac{n}{9}) + 2S(\frac{2n}{9}) + S(\frac{4n}{9}) + (\frac{1}{3^{1.1}}+ \frac{2^{1.1}}{3^{1.1}})c_1n^{1.1}+c_2 + c_1n^{1.1} + c_2$
  - Cost is decreasing so this is root dominated.
  - $\mathcal{O}(n^{1.1})$

Between 3a - 3c, I would choose the algorithm presented in 3b. It has the most efficient span and work out of the three. 

4. **Even More Algorithm Selection** 

a. Work and Span: $T(n) = 5T(\frac{n}{2}) + n$
- $W(n) = 5W(\frac{n}{2}) + n$
  - $C\texttt{(Root)} = n$
  - $C\texttt{(1st Level)} = 5(5W(\frac{n}{2^2}) + \frac{n}{2}) + n$
    - $5^2W(\frac{n}{2^2}) + \frac{5n}{2} + n$
  - Cost is increasing so this is leaf dominated. 
    - Number of leaves $5^{\log_2 n} = n^{\log_2 5}$
  - $\mathcal{O}(n^{\log_2 5})$
- $S(n) = S(\frac{n}{2}) + n$
  - $C\texttt{(Root)} = n$
  - $C\texttt{(1st Level)} = S(\frac{n}{2^2}) + \frac{n}{2} + n$
  - Cost is decreasing so this is root dominated. 
  - $\mathcal{O}(n)$

b. Work and Span: $T(n) = 2T(n-1) + c$
- $W(n) = 2W(n-1) + c$
  - $C\texttt{(Root)} = c$
  - $C\texttt{(1st Level)} = 2(2W(n-2) + c) + c$
    - $= 2^2W(n-2) + 2c + c$
  - Cost is increasing so this is leaf dominated. 
    - Number of leaves is $2n$
  - $\mathcal{O}(n)$
- $S(n) = S(n-1) + c$
  - $C\texttt{(Root)} = c$
  - $C\texttt{(1st Level)} = S(n-2) + c + c$
  - Cost is neither increasing nor decreasing so this is balanced. 
    - Number of levels is $n$ and the max cost per level is  c. 
  - $\mathcal{O}(n)$

c. Work and Span: $T(n) = 9T(\frac{n}{3}) + c_1n^2 + c_2$
- $W(n) = 9W(\frac{n}{3}) + c_1n^2 + c_2$
  - $C\texttt{(Root)} = c_1n^2 + c_2$
  - $C\texttt{(1st Level)} = 9(9W(\frac{n}{3^2}) + c_1(\frac{n}{3})^2 + c_2) + c_1n^2 + c_2$
    - $= 9^2W(\frac{n}{3^2}) + c_1\frac{9n^2}{3^2} + 9c_2 + c_1n^2 + c_2$
    - $= 9^2W(\frac{n}{3^2}) + c_1n^2 + 9c_2 + c_1n^2 + c_2$
  - Cost is neither increasing or decreasing so this is balanced.
    - Number of levels is $\log_9 n$ and max cost per level is $n^2$
  - $\mathcal{O}(n^2 \log_9 n)$
- $S(n) = S(\frac{n}{3}) + c_1n^2 + c_2$
  - $C\texttt{(Root)} = c_1n^2 + c_2$
  - $C\texttt{(1st Level)} = S(\frac{n}{3^2}) + c_1(\frac{n}{3})^2 + c_2 + c_1n^2 + c_2$
    - $= S(\frac{n}{3^2}) + c_1\frac{n^2}{3^2} + c_2 + c_1n^2 + c_2$
  - Cost is decreasing so this is root dominated.
  - $\mathcal{O}(n^2)$

Between 4a-4c, I would be between choosing either the algorithm presented in 4a or 4b. They have similar spans, but since 4b also has better work, I'd most likely choose that algorithm. 

4. **Integer Multiplication Timing Results**

5. **Black Hats and White Hats**
