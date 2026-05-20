# Proof

## Problem Statement

This is a problem coming from Yupei Huang and Xiaoqian Xu. Exponential lower bounds for the advection-
diffusion equation with shear flows. arXiv preprint arXiv:2511.14512, 2025.

Here we have the following theorem:
\begin{theorem}\label{main}
Consider the advection diffusion equation in $\mathbb{T}^2$:
\begin{equation}\label{shear}
    \partial_t \rho + U(t,y)\,\partial_x \rho = \Delta \rho.
\end{equation}
Assume that $\rho(0,\cdot) \in C^{\infty}_{x,y}$ is mean-zero and that 
\[
\|U\|_{L^{\infty}_t C^{\infty}_y} < \infty.
\]
Then there exist constants $0 < c_1 < c_2$, depending on $U$ and $\rho(0,\cdot)$, such that for all $t \ge 0$,
\begin{equation}
    \|\rho(0,\cdot)\|_{L^2_{x,y}}\, e^{-c_2 t}
    \;\le\;
    \|\rho(t,\cdot)\|_{L^2_{x,y}}
    \;\le\;
    \|\rho(0,\cdot)\|_{L^2_{x,y}}\, e^{-c_1 t}.
\end{equation}
\end{theorem}
For this theorem, before I give the full proof, here is a small lemma:

    \begin{lemma}\label{smalllemma}
Let $f:[0,\infty) \to (0,\infty)$ be non-increasing.
Then the following two statements are equivalent:
\begin{enumerate}
\item[(i)] There exist constants $c>0$ and $C>0$ such that
          $f(t) \ge C e^{-c t}$ for all $t \ge 0$.
\item[(ii)] $f$ does not decay faster than any exponential;
          i.e., it is \textbf{not} true that
          $\lim_{t\to\infty} e^{\beta t} f(t) = 0$
          for every $\beta > 0$.
\end{enumerate}
\end{lemma}

\begin{proof}
The implication (i)$\Rightarrow$(ii) is immediate:
if $f(t) \ge C e^{-c t}$ then for any $\beta>c$,
$e^{\beta t}f(t) \ge C e^{(\beta-c)t} \to \infty$, so the limit is not zero.

For the converse, suppose (ii) holds. Then there exists some $\beta_0>0$ such that
$\limsup_{t\to\infty} e^{\beta_0 t} f(t) > 0$.
Hence we can find a sequence $t_n\to\infty$ and a constant $\delta>0$ with
$e^{\beta_0 t_n} f(t_n) \ge \delta$ for all $n$.
Because $f$ is non-increasing, for any $t \in [t_n, t_{n+1}]$,
$$
f(t) \ge f(t_{n+1}) \ge \delta e^{-\beta_0 t_{n+1}}
     \ge \delta e^{-\beta_0 (t + (t_{n+1}-t_n))}.
$$
If the distances $t_{n+1}-t_n$ are uniformly bounded (which can always be arranged by passing to a subsequence), we obtain a uniform exponential lower bound. A simpler global argument (avoiding subsequences) uses the fact that if (i) fails, then for every $c>0$ and $C>0$ (say $C=f(0)/2$) there exists $t_c$ with $f(t_c) < C e^{-c t_c}$. By monotonicity, $f(t) \le f(t_c) < C e^{-c t_c}$ for all $t \ge t_c$. Choosing $c=2\beta$ and letting $\beta>0$ be arbitrary, we get $e^{\beta t} f(t) < C e^{-\beta t} \to 0$, contradicting (ii). Therefore (i) must hold.
\end{proof}
\begin{proof}[Proof of Theorem \ref{main}]
The upper bound follows from a standard energy estimate; we focus on the lower bound.

Assume, to the contrary, that there exists a non‑zero solution $\rho$ whose $L^2$ norm decays faster than any exponential.
Take the Fourier expansion in $x$:
$\rho(t,x,y)=\sum_{k\in\mathbb Z}\rho_k(t,y)e^{ikx}$.
By Plancherel,
$$
\|\rho(t)\|_{L^2_{x,y}}^2 = \sum_{k}\|\rho_k(t)\|_{L^2_y}^2 .
$$
Hence, if $\rho$ decays faster than any exponential, the same is true for every Fourier mode $\rho_k$.
Suppose some $k$ has $\rho_k\not\equiv 0$.  Then $\|\rho_k(t)\|_{L^2_y}$ decays faster than any exponential.
The equation for $\rho_k$ is
\begin{equation}\label{eq:rho_k}
\partial_t\rho_k + (k^2-\partial_{yy})\rho_k = -ik\,U(t,y)\,\rho_k , \qquad t\ge 0 .
\end{equation}
Choose a sequence of integers $m\ge 1$ and set
$$
\Lambda_m = k^2 + \frac{m^2+(m+1)^2}{2}.
$$
Define the lifted function
$$
h(t,y)=
\begin{cases}
e^{\Lambda_m t}\rho_k(t,y), & t\ge 0,\\[4pt]
e^{\Lambda_m t}\rho_k(0,y),   & t\le 0 .
\end{cases}
$$
Because $\rho_k$ decays faster than any exponential, $h$ and $U(t,y)h(t,y)1_{t>0}$ belong to
$L^1(\mathbb R, L^2(\mathbb T))$.  Moreover $h$ is a distributional solution of
\begin{equation}\label{eq:h_eq}
\partial_t h + (k^2-\partial_{yy}-\Lambda_m)h
= -ik\,U(t,y)h\,1_{t>0} + (k^2-\partial_{yy})\rho_k(0,\cdot)\,e^{\Lambda_m t}1_{t<0}
=: F_1 + F_2 .
\end{equation}

Expand $h$, $\rho_k(0,\cdot)$, $F_1$ and $F_2$ in Fourier series in $y$:
$$
h(t,y)=\sum_{l\in\mathbb Z} h^l(t)e^{ily},\qquad
\rho_k(0,y)=\sum_{l\in\mathbb Z} g_k^l e^{ily},\qquad
F_j(t,y)=\sum_{l\in\mathbb Z} F_j^l(t)e^{ily}.
$$
Equation \eqref{eq:h_eq} becomes
$$
\partial_t h^l + (k^2+l^2-\Lambda_m)h^l = F_1^l + 1_{t\le 0}\,e^{\Lambda_m t}(k^2+l^2)g_k^l .
$$
Now apply the Fourier transform in time with the convention
$\widehat{F}(\tau)=\int_{\mathbb R} F(t)e^{i\tau t}\,dt$,
so that $\widehat{\partial_t h^l}(\tau) = -i\tau\,\widehat{h^l}(\tau)$.
We obtain
\begin{equation}\label{eq:Fourier_solution}
\widehat{h^l}(\tau) =
(-i\tau + k^2+l^2-\Lambda_m)^{-1}\widehat{F_1^l}(\tau)
+ (-i\tau + k^2+l^2-\Lambda_m)^{-1}
   \frac{1}{\Lambda_m-i\tau}\,(k^2+l^2)\,g_k^l .
\end{equation}
(The sign in front of $i\tau$ is irrelevant for absolute values because $|-i\tau+A| = |i\tau+A|$.)

The key estimates are collected in the following lemma, in which $C$ denotes a constant independent of $m$ that may change from line to line.

\begin{lemma}\label{lemma1}
For any $k,l\in\mathbb Z$, $m\in\mathbb N$ and $\frac12<s<1$, let
$\Lambda_m = k^2+\frac{m^2+(m+1)^2}{2}$.  Then there exists $C>0$ such that
\begin{align}
\bigl(l^2-\tfrac{m^2+(m+1)^2}{2}\bigr)^2 &\ge C m^2, \label{claim0} \\
|(-i\tau + k^2+l^2-\Lambda_m)^{-1}| &\le \frac{C}{\sqrt{m^2+\tau^2}}, \label{claim1}\\
|(-i\tau + k^2+l^2-\Lambda_m)^{-1}| &\le \frac{C}{m^{1-s}|l|^s}, \qquad l\neq 0, \label{claim2}\\
|(-i\tau + k^2-\Lambda_m)^{-1}| &\le \frac{C}{\sqrt{\tau^2+m^4}}. \label{claim3}
\end{align}
\end{lemma}
The proof is identical to the one in the paper (with $|l|^s$ replacing $l^s$).

Using Lemma~\ref{lemma1} we estimate each term in \eqref{eq:Fourier_solution}.
For the zero mode of $F_1$ we have
\begin{equation}\label{est_F10}
|(-i\tau + k^2-\Lambda_m)^{-1}\widehat{F_1^0}(\tau)|
\le \frac{C}{\sqrt{m^4+\tau^2}}\,|\widehat{F_1^0}(\tau)|.
\end{equation}
For $l\neq0$,
\begin{equation}\label{est_F1l}
|(-i\tau + k^2+l^2-\Lambda_m)^{-1}\widehat{F_1^l}(\tau)|
\le \frac{C}{m^{1-s}|l|^s}\,|\widehat{F_1^l}(\tau)|.
\end{equation}
For the initial‑data terms, a calculation similar to the one in the paper gives
\begin{equation}\label{est_init}
\Bigl|(-i\tau + k^2+l^2-\Lambda_m)^{-1}\frac{1}{\Lambda_m-i\tau}(k^2+l^2)g_k^l\Bigr|
\le \frac{C}{\sqrt{m^2+\tau^2}}\,|g_k^l|,
\end{equation}
and for $l=0$ the better bound
\begin{equation}\label{est_init0}
\Bigl|(-i\tau + k^2-\Lambda_m)^{-1}\frac{1}{\Lambda_m-i\tau}k^2g_k^0\Bigr|
\le C k^2\,\frac{|g_k^0|}{\sqrt{m^4+\tau^2}}.
\end{equation}

Squaring, summing over $l$, and using Plancherel in $y$ we obtain
\begin{align*}
\|\widehat{h}(\tau)\|_{L^2_y}^2
&\le C\Bigl(
 \frac{|\widehat{F_1^0}(\tau)|^2}{m^4+\tau^2}
 + (k^4|g_k^0|^2)\frac{1}{m^4+\tau^2}
 + \sum_{l\neq0}\frac{|\widehat{F_1^l}(\tau)|^2}{|l|^{2s}\,m^{2-2s}}
 + \sum_{l\neq0}\frac{|g_k^l|^2}{m^2+\tau^2}
 \Bigr).
\end{align*}
Now integrate over $\tau\in\mathbb R$ and use the Plancherel theorem for the time Fourier transform.
The crucial point is that we replace factors like $1/(m^4+\tau^2)$ by the cruder bound $m^{-4}$,
and $1/(m^2+\tau^2)$ by $m^{-2}$, before applying Plancherel.  Hence
\begin{align*}
\int_{\mathbb R}\|\widehat{h}(\tau)\|_{L^2_y}^2\,d\tau
&\le C\Bigl(
 \frac{1}{m^4}\int_{\mathbb R}|\widehat{F_1^0}(\tau)|^2\,d\tau
 + \frac{k^4}{m^4}\|g_k^0\|^2
 + \frac{1}{m^{2-2s}}\int_{\mathbb R}\sum_{l\neq0}\frac{|\widehat{F_1^l}(\tau)|^2}{|l|^{2s}}\,d\tau \\
&\qquad\qquad + \frac{1}{m^2}\sum_{l\neq0}\|g_k^l\|^2
 \Bigr).
\end{align*}
By Plancherel,
$\int_{\mathbb R}|\widehat{F_1^0}(\tau)|^2\,d\tau = 2\pi\int_{\mathbb R}|F_1^0(t)|^2\,dt$,
and
$\int_{\mathbb R}\sum_{l\neq0}\frac{|\widehat{F_1^l}(\tau)|^2}{|l|^{2s}}\,d\tau
 = 2\pi\int_{\mathbb R}\|F_1(t,\cdot)\|_{H^{-s}_y}^2\,dt$.
Therefore, for $t\ge0$,
\begin{equation}\label{int_h_est0}
\int_{0}^{\infty}\|h(t)\|_{L^2_y}^2\,dt
\le C\Bigl(
 \frac{1}{m^4}\int_{0}^{\infty}|F_1^0(t)|^2\,dt
 + \frac{1}{m^{2-2s}}\int_{0}^{\infty}\|F_1(t)\|_{H^{-s}_y}^2\,dt
 + \frac{k^4}{m^4}\|g_k^0\|^2
 + \frac{1}{m^2}\sum_{l\neq0}\|g_k^l\|^2
 \Bigr).
\end{equation}

It remains to estimate $F_1$ in terms of $h$ and $U$.
Recall $F_1(t,y) = -ik\,U(t,y)\,h(t,y)$ for $t>0$.
For the $H^{-s}$ norm we use the standard definition
$$
\|F_1(t)\|_{H^{-s}} = \sup_{\|\varphi\|_{H^{s}}=1} |\langle F_1,\varphi\rangle|.
$$
With the Sobolev embedding $H^{s}\subset L^{\infty}$ ($s>\frac12$), we obtain
\begin{align*}
\|F_1(t)\|_{H^{-s}}
 &\le \sup_{\|\varphi\|_{H^{s}}=1} \int_{\mathbb T} k|U(t,y)h(t,y)\varphi(y)|\,dy \\
 &\le k\,\|U(t)\|_{L^2_y}\,\|h(t)\|_{L^2_y}
   \sup_{\|\varphi\|_{H^{s}}=1}\|\varphi\|_{L^\infty}
 \le C k\,\|U(t)\|_{L^2_y}\,\|h(t)\|_{L^2_y}.
\end{align*}
Similarly,
$$
|F_1^0(t)| = \Bigl|\frac{1}{2\pi}\int_{\mathbb T} F_1(t,y)\,dy\Bigr|
\le \frac{k}{2\pi}\|U(t)\|_{L^2_y}\|h(t)\|_{L^2_y}.
$$
Insert these bounds into \eqref{int_h_est0} and use that
$\|U(t)\|_{L^2_y}\le \|U\|_{L^\infty_t L^2_y}$:
\begin{align*}
\int_{0}^{\infty}\|h\|_{L^2_y}^2\,dt
&\le C k^2\|U\|_{L^\infty_t L^2_y}^2
   \Bigl(\frac{1}{m^4}+\frac{1}{m^{2-2s}}\Bigr)
   \int_{0}^{\infty}\|h\|_{L^2_y}^2\,dt \\
&\quad + C\Bigl(\frac{k^4}{m^4}+\frac{1}{m^2}\Bigr)\|g_k\|_{L^2_y}^2 .
\end{align*}
Choose $m$ so large that
$$
C k^2\|U\|_{L^\infty_t L^2_y}^2\Bigl(\frac{1}{m^4}+\frac{1}{m^{2-2s}}\Bigr) \le \frac12 .
$$
Then the first integral can be absorbed into the left‑hand side, giving
$$
\int_{0}^{\infty}\|h(t)\|_{L^2_y}^2\,dt
\le 2C\Bigl(\frac{k^4}{m^4}+\frac{1}{m^2}\Bigr)\|g_k\|_{L^2_y}^2 .
$$
Letting $m\to\infty$ forces
$\int_{0}^{\infty}\|h(t)\|_{L^2_y}^2\,dt = 0$, hence $h\equiv0$ almost everywhere.
Since $h(t)=e^{\Lambda_m t}\rho_k(t)$ for $t\ge0$, we obtain $\rho_k\equiv0$,
contradicting the assumption $\rho_k\not\equiv0$.

Thus no non‑zero mode can decay faster than any exponential.
Because $\|\rho(t)\|_{L^2}$ is non‑increasing (energy estimate), the elementary Lemma~\ref{smalllemma}
immediately implies that there exists $c_2>0$ and $C>0$ such that
$\|\rho(t)\|_{L^2}\ge C e^{-c_2 t}$ for all $t\ge0$.
This completes the proof of the lower bound.
\end{proof}


\begin{problem}
Although the proof above is nonconstructive, based on the idea of this proof, find an explicit upper bound of $c_2$, in terms of $U(t,y)$ and $\rho(0,x,y)$. 
\end{problem}
\begin{problem}
Without above proof, prove Theorem \ref{main} with an explicit estimate of upper bound of $c_2$ in terms of $U(t,y)$ and $\rho(0,x,y)$.
\end{problem}

## Proof

We use the Fourier normalization implicit in the displayed Plancherel identities in the problem: the functions
\(e^{ikx}e^{ily}\) form an orthonormal Fourier basis. Thus
\[
\|v\|_{L^2(\mathbb T)}^2=\sum_{l\in\mathbb Z}|v^l|^2,
\qquad
\|w\|_{L^2(\mathbb T^2)}^2=\sum_{k,l\in\mathbb Z}|w_k^l|^2.
\]
If a different Haar-measure normalization is chosen, only the universal numerical constants below change.

We assume first that \(N:=\|\rho_0\|_{L^2_{x,y}}>0\). If \(N=0\), then \(\rho\equiv0\), and the theorem is immediate with, for example, \(c_1=1\) and \(c_2=2\).

Set
\[
M_0:=\|U\|_{L^\infty_tL^2_y},\qquad
M_1:=\|\partial_yU\|_{L^\infty_tL^\infty_y},
\]
and
\[
C_{\rm emb}:=\left(\sum_{l\in\mathbb Z}(1+l^2)^{-3/4}\right)^{1/2}.
\]
For definiteness, take the universal constants
\[
C_{\rm res}=10^4,\qquad C_{\rm end}=10^4.
\]
They are deliberately larger than the constants produced by the estimates below.

### STEP1: Fourier Mode Reduction

**Claim:** Let
\[
\rho_0(x,y)=\sum_{k,l\in\mathbb Z}g_k^l e^{ikx}e^{ily},\qquad
\rho_{0,k}(y)=\sum_{l\in\mathbb Z}g_k^l e^{ily}.
\]
If there exists \(k\ne0\) with
\[
a_k:=\|\rho_{0,k}\|_{L_y^2}>0,
\]
fix one such \(k=k_*\) and write \(a=a_{k_*}\), \(g=\rho_{0,k_*}\), \(f(t)=\rho_{k_*}(t)\). Then
\[
\partial_t f+(k_*^2-\partial_{yy})f=-ik_*U(t,y)f,\qquad f(0)=g,
\]
and
\[
\frac{d}{dt}\|f(t)\|_{L_y^2}^2
=
-2k_*^2\|f(t)\|_{L_y^2}^2-2\|\partial_y f(t)\|_{L_y^2}^2\le0.
\]
If no such \(k\ne0\) exists, then \(\rho_0=\rho_{0,0}(y)\) and, since \(\rho_0\) is mean-zero, there is \(l_0\ne0\) with \(g_0^{l_0}\ne0\) and
\[
\|\rho(t)\|_{L^2_{x,y}}\ge |g_0^{l_0}|e^{-l_0^2t}\qquad(t\ge0).
\]

**Proof:**
Expand
\[
\rho(t,x,y)=\sum_{k\in\mathbb Z}\rho_k(t,y)e^{ikx}.
\]
Since \(U(t,y)\) is independent of \(x\), the \(x\)-Fourier modes do not couple. The coefficient of \(e^{ikx}\) in
\[
\partial_t\rho+U(t,y)\partial_x\rho=\partial_{xx}\rho+\partial_{yy}\rho
\]
is
\[
\partial_t\rho_k+ikU(t,y)\rho_k=-k^2\rho_k+\partial_{yy}\rho_k,
\]
which is the asserted equation.

For the selected nonzero mode \(f=\rho_{k_*}\), multiply the mode equation by \(\overline f\), integrate in \(y\), and take real parts. The term
\[
\operatorname{Re}\int_{\mathbb T}(-ik_*U)|f|^2\,dy
\]
vanishes because \(U\) is real-valued. Integration by parts gives
\[
\frac12\frac{d}{dt}\|f(t)\|_2^2
+k_*^2\|f(t)\|_2^2+\|\partial_y f(t)\|_2^2=0,
\]
which is the claimed identity.

If all nonzero \(x\)-modes of \(\rho_0\) vanish, then the solution remains independent of \(x\) and solves
\[
\partial_t\rho=\partial_{yy}\rho.
\]
The mean-zero condition gives \(g_0^0=0\). Since \(N>0\), at least one \(g_0^{l_0}\ne0\) with \(l_0\ne0\). The heat solution is
\[
\rho(t,y)=\sum_{l\ne0}g_0^l e^{-l^2t}e^{ily},
\]
so Plancherel yields
\[
\|\rho(t)\|_{L^2_{x,y}}^2=\sum_{l\ne0}|g_0^l|^2e^{-2l^2t}
\ge |g_0^{l_0}|^2e^{-2l_0^2t}.
\]
Taking square roots proves the last estimate.

**Dependencies:** Direct Fourier calculation.

---

### STEP2: Short-Time Lower Bound for the Selected Mode

**Claim:** Assume \(k_*\ne0\). Define
\[
M_1:=\|\partial_yU\|_{L^\infty_tL^\infty_y},\qquad
R_*:=\frac{\|\partial_y g\|_{L_y^2}}{\|g\|_{L_y^2}},
\]
\[
B_*:=8\left(1+k_*^2+R_*^2+|k_*|M_1(1+R_*)\right),
\qquad
\delta_*:=\min\{1,B_*^{-1}\}.
\]
Then for every \(0\le t\le\delta_*\),
\[
\|f(t)\|_{L_y^2}\ge a\,e^{-B_*t}.
\]
In particular,
\[
\int_0^{\min\{T,\delta_*\}} e^{2\Lambda t}\|f(t)\|_{L_y^2}^2\,dt
\ge
\frac{a^2}{4}\min\{T,\delta_*\}
\]
for every \(T>0\) and every \(\Lambda\ge0\).

**Proof:**
Let
\[
E(t):=\|f(t)\|_2^2,\qquad Y(t):=\|\partial_y f(t)\|_2^2,
\qquad K:=|k_*|M_1.
\]
By STEP1, \(E(t)\le E(0)=a^2\). Differentiating the mode equation in \(y\) gives
\[
\partial_t(\partial_y f)+(k_*^2-\partial_{yy})(\partial_y f)
=-ik_*U\,\partial_y f-ik_*(\partial_yU)f.
\]
Taking the \(L^2_y\) inner product with \(\partial_y f\), taking real parts, and discarding the nonpositive diffusion and \(k_*^2\) terms gives
\[
\frac12Y'(t)
\le |k_*|M_1\|f(t)\|_2\|\partial_yf(t)\|_2
\le Ka\,Y(t)^{1/2}.
\]
Equivalently, after the usual harmless regularization of \(Y^{1/2}\) at zeros,
\[
\frac{d}{dt}Y(t)^{1/2}\le Ka.
\]
Hence, for \(t\ge0\),
\[
Y(t)^{1/2}\le Y(0)^{1/2}+Kat=a(R_*+Kt).
\]

Now \(B_*\ge8\), so \(\delta_*=B_*^{-1}\). For \(0\le t\le\delta_*\), STEP1 and the last estimate imply
\[
\begin{aligned}
E(t)
&=a^2-2\int_0^t\bigl(k_*^2E(s)+Y(s)\bigr)\,ds  \\
&\ge a^2\left[
1-2\left(k_*^2t+R_*^2t+R_*Kt^2+\frac{K^2t^3}{3}\right)
\right].
\end{aligned}
\]
Put
\[
A:=1+k_*^2+R_*^2+K(1+R_*),\qquad B_*=8A,\qquad x:=B_*t\in[0,1].
\]
Since \(k_*^2+R_*^2\le A\), \(R_*K\le A\), and \(K\le A\), we have
\[
k_*^2t+R_*^2t+R_*Kt^2+\frac{K^2t^3}{3}
\le
\frac{x}{8}+\frac{x^2}{64}+\frac{x^3}{1536}.
\]
Therefore
\[
2\left(k_*^2t+R_*^2t+R_*Kt^2+\frac{K^2t^3}{3}\right)
\le
\left(\frac14+\frac1{32}+\frac1{768}\right)x.
\]
The numerical coefficient on the right is less than \(1-e^{-2}\). Since the function
\(x\mapsto 1-e^{-2x}\) is concave on \([0,1]\), it lies above its chord, so
\[
1-e^{-2x}\ge (1-e^{-2})x
\quad(0\le x\le1).
\]
Consequently,
\[
E(t)\ge a^2e^{-2x}=a^2e^{-2B_*t},
\]
which gives \(\|f(t)\|_2\ge ae^{-B_*t}\).

The same estimate also gives the cruder bound
\[
E(t)\ge
a^2\left[
1-\left(\frac14+\frac1{32}+\frac1{768}\right)
\right]
\ge \frac{a^2}{4}
\qquad(0\le t\le\delta_*).
\]
Since \(e^{2\Lambda t}\ge1\), integration over
\([0,\min\{T,\delta_*\}]\) proves
\[
\int_0^{\min\{T,\delta_*\}}e^{2\Lambda t}\|f(t)\|_2^2\,dt
\ge\frac{a^2}{4}\min\{T,\delta_*\}.
\]

**Dependencies:** STEP1.

---

### STEP3: Finite-Window Lifted Resolvent Inequality ⭐ KEY STEP

**Claim:** Assume \(k_*\ne0\), fix \(s=3/4\), and let
\[
C_{\rm emb}:=\left(\sum_{l\in\mathbb Z}(1+l^2)^{-3/4}\right)^{1/2}.
\]
With \(C_{\rm res}=10^4\) and \(C_{\rm end}=10^4\), define, for \(m\ge1\),
\[
\Lambda_m:=k_*^2+\frac{m^2+(m+1)^2}{2},
\]
\[
A_m:=C_{\rm res}C_{\rm emb}^2 k_*^2\|U\|_{L^\infty_tL^2_y}^2
\left(m^{-4}+m^{-1/2}\right),
\]
\[
B_m:=C_{\rm res}m^{-1},
\qquad
D_m:=C_{\rm end}(1+k_*^2+m^2)^2.
\]
For every \(T>0\), with
\[
I_m(T):=\int_0^T e^{2\Lambda_mt}\|f(t)\|_{L_y^2}^2\,dt,
\]
one has
\[
I_m(T)
\le
A_m I_m(T)+B_m a^2
+D_m e^{2\Lambda_mT}\|f(T)\|_{L_y^2}^2.
\]

**Proof:**
<key-original-step>
Write
\[
q_m:=\frac{m^2+(m+1)^2}{2}=m^2+m+\frac12,
\qquad
\alpha_l:=k_*^2+l^2-\Lambda_m=l^2-q_m.
\]
The point of choosing \(q_m\) halfway between \(m^2\) and \((m+1)^2\) is that it is uniformly separated from every square. Indeed, for every \(l\in\mathbb Z\),
\[
|\alpha_l|=|l^2-q_m|\ge m+\frac12\ge m.
\]
Also, for \(l\ne0\),
\[
|\alpha_l|\ge \frac12\,m^{1/4}|l|^{3/4}.
\]
To verify the last estimate, put \(r=|l|\). If \(1\le r\le m\), then
\[
|\alpha_l|=q_m-r^2\ge q_m-m^2=m+\frac12\ge m\ge m^{1/4}r^{3/4}.
\]
If \(r\ge m+1\), the function
\[
r\mapsto \frac{r^2-q_m}{r^{3/4}}
=r^{5/4}-q_mr^{-3/4}
\]
has positive derivative on \([m+1,\infty)\). Hence its minimum on integers \(r\ge m+1\) is at \(r=m+1\), where
\[
\frac{(m+1)^2-q_m}{(m+1)^{3/4}}
=\frac{m+1/2}{(m+1)^{3/4}}
\ge \frac12m^{1/4}.
\]
Thus, with
\[
R_l(\tau):=(i\tau+\alpha_l)^{-1},
\]
we have
\[
|R_l(\tau)|\le\frac1{\sqrt{\tau^2+m^2}},
\]
\[
|R_0(\tau)|\le\frac1{\sqrt{\tau^2+m^4}},
\]
and, for \(l\ne0\),
\[
|R_l(\tau)|\le\frac{2}{m^{1/4}|l|^{3/4}}.
\]

Fix \(T>0\), and define the lifted finite-window function
\[
h(t,y):=
\begin{cases}
e^{\Lambda_mt}g(y),& t<0,\\
e^{\Lambda_mt}f(t,y),&0\le t\le T,\\
0,&t>T.
\end{cases}
\]
There is no jump at \(t=0\), while there is a terminal jump from
\(e^{\Lambda_mT}f(T)\) to \(0\) at \(t=T\). In distributions on
\(\mathbb R_t\times\mathbb T_y\),
\[
\partial_t h+(k_*^2-\partial_{yy}-\Lambda_m)h
=F_1+F_2-H\delta_T,
\]
where
\[
F_1(t,y):=-ik_*U(t,y)h(t,y){\bf 1}_{(0,T)}(t),
\]
\[
F_2(t,y):=e^{\Lambda_mt}(k_*^2-\partial_{yy})g(y){\bf 1}_{(-\infty,0)}(t),
\]
and
\[
H(y):=e^{\Lambda_mT}f(T,y).
\]

Take the unitary Fourier transform in \(t\), and expand in the \(y\)-Fourier basis. The transform of
\(e^{\Lambda_mt}{\bf 1}_{(-\infty,0)}(t)\) is
\((2\pi)^{-1/2}(\Lambda_m-i\tau)^{-1}\), and the transform of \(\delta_T\) is
\((2\pi)^{-1/2}e^{-iT\tau}\). Since \((2\pi)^{-1/2}<1\), each \(l\)-mode obeys the pointwise bound
\[
|\widehat h^l(\tau)|
\le |R_l(\tau)|\,|\widehat{F_1^l}(\tau)|
+|R_l(\tau)|\frac{(k_*^2+l^2)|g^l|}{|\Lambda_m-i\tau|}
+|R_l(\tau)|\,|H^l|.
\]
Using \(|u+v+w|^2\le3(|u|^2+|v|^2+|w|^2)\) and Plancherel,
\[
I_m(T)\le \|h\|_{L^2(\mathbb R_tL^2_y)}^2
\le 3(\mathcal F+\mathcal G+\mathcal H),
\]
where
\[
\mathcal F:=\int_{\mathbb R}\sum_l|R_l(\tau)|^2|\widehat{F_1^l}(\tau)|^2\,d\tau,
\]
\[
\mathcal G:=\int_{\mathbb R}\sum_l
|R_l(\tau)|^2\frac{(k_*^2+l^2)^2}{\Lambda_m^2+\tau^2}|g^l|^2\,d\tau,
\]
and
\[
\mathcal H:=\int_{\mathbb R}\sum_l|R_l(\tau)|^2|H^l|^2\,d\tau.
\]

We estimate these three terms separately.

First, the forcing term \(F_1\). The resolvent bounds give
\[
\sum_l|R_l|^2|\widehat{F_1^l}|^2
\le
\frac{|\widehat{F_1^0}|^2}{m^4+\tau^2}
+4m^{-1/2}\sum_{l\ne0}|l|^{-3/2}|\widehat{F_1^l}|^2.
\]
Since \(|l|^{-3/2}\le 2(1+l^2)^{-3/4}\) for \(l\ne0\), Plancherel in \(t\) gives
\[
\mathcal F
\le
m^{-4}\int_0^T |F_1^0(t)|^2\,dt
+8m^{-1/2}\int_0^T\|F_1(t)\|_{H^{-3/4}_y}^2\,dt.
\]
For the zero mode,
\[
|F_1^0(t)|\le |k_*|\|U(t)\|_2\|h(t)\|_2.
\]
For the \(H^{-3/4}\) norm, if \(\|\varphi\|_{H^{3/4}}=1\), then the Fourier series estimate
\[
\|\varphi\|_{L^\infty}
\le
\left(\sum_l(1+l^2)^{-3/4}\right)^{1/2}\|\varphi\|_{H^{3/4}}
=C_{\rm emb}
\]
gives
\[
|\langle F_1(t),\varphi\rangle|
\le |k_*|\|U(t)\|_2\|h(t)\|_2\|\varphi\|_\infty
\le |k_*|C_{\rm emb}M_0\|h(t)\|_2.
\]
Thus
\[
\mathcal F
\le
10C_{\rm emb}^2k_*^2M_0^2(m^{-4}+m^{-1/2})I_m(T).
\]

Second, the initial extension term. Let
\[
b:=\Lambda_m=k_*^2+q_m>0,\qquad a_l:=|\alpha_l|\ge m.
\]
Using
\[
\int_{\mathbb R}\frac{d\tau}{(\tau^2+a_l^2)(\tau^2+b^2)}
=\frac{\pi}{a_lb(a_l+b)}
\]
and
\[
k_*^2+l^2=b+\alpha_l,
\qquad
(k_*^2+l^2)^2\le(a_l+b)^2,
\]
we obtain
\[
\begin{aligned}
\int_{\mathbb R}
|R_l(\tau)|^2\frac{(k_*^2+l^2)^2}{\Lambda_m^2+\tau^2}\,d\tau
&=
\pi\frac{(k_*^2+l^2)^2}{a_lb(a_l+b)}\\
&\le \pi\left(\frac1{a_l}+\frac1b\right)
\le \frac{2\pi}{m}.
\end{aligned}
\]
Therefore
\[
\mathcal G\le 2\pi m^{-1}\sum_l|g^l|^2=2\pi m^{-1}a^2.
\]

Third, the terminal jump. Since \(a_l\ge m\),
\[
\mathcal H
=\sum_l|H^l|^2\int_{\mathbb R}\frac{d\tau}{\tau^2+a_l^2}
\le \frac{\pi}{m}\|H\|_2^2
\le \pi e^{2\Lambda_mT}\|f(T)\|_2^2.
\]

Combining the bounds for \(\mathcal F,\mathcal G,\mathcal H\), and using
\(C_{\rm res}=C_{\rm end}=10^4\), gives
\[
I_m(T)
\le
A_mI_m(T)+B_ma^2+D_me^{2\Lambda_mT}\|f(T)\|_2^2,
\]
with \(A_m,B_m,D_m\) as stated.
</key-original-step><heuristics>The lifted function turns the parabolic evolution on \([0,T]\) into a resolvent equation on the whole time line. The midpoint choice of \(\Lambda_m\) places the spectral parameter between two consecutive \(y\)-Laplacian eigenvalues, so every \(y\)-mode has a resolvent denominator at least of size \(m\). The initial data is handled by the exponentially decaying extension for \(t<0\); the only finite-window price is the terminal jump at \(T\), and that jump is exactly the endpoint term. If the endpoint were too small, the resolvent inequality would force the weighted mass \(I_m(T)\) to be small, contradicting the short-time mass from STEP2.</heuristics>

**Dependencies:** STEP1; direct proofs of the high-frequency resolvent and \(H^{3/4}\hookrightarrow L^\infty\) estimates.

---

### STEP4: Endpoint Lower Bound from the Finite-Window Estimate

**Claim:** Assume \(k_*\ne0\). Let \(m_*\) be the least positive integer satisfying
\[
A_{m_*}\le\frac14,
\qquad
B_{m_*}\le\frac{\delta_*}{16}.
\]
Such an \(m_*\) exists because \(A_m\to0\) and \(B_m\to0\). Define
\[
\Lambda_*:=\Lambda_{m_*},\qquad
\theta_*:=\left(\frac{\delta_*}{32D_{m_*}}\right)^{1/2}.
\]
Then for every \(T\ge\delta_*\),
\[
\|f(T)\|_{L_y^2}\ge \theta_*\,a\,e^{-\Lambda_*T}.
\]

**Proof:**
Since \(A_m\to0\) and \(B_m=C_{\rm res}m^{-1}\to0\), such an \(m_*\) exists. For \(T\ge\delta_*\), STEP2 gives
\[
I_{m_*}(T)
\ge
\int_0^{\delta_*}e^{2\Lambda_*t}\|f(t)\|_2^2\,dt
\ge \frac{a^2\delta_*}{4}.
\]
STEP3 gives
\[
(1-A_{m_*})I_{m_*}(T)
\le B_{m_*}a^2+D_{m_*}e^{2\Lambda_*T}\|f(T)\|_2^2.
\]
Using \(A_{m_*}\le1/4\) and \(B_{m_*}\le\delta_*/16\),
\[
\begin{aligned}
D_{m_*}e^{2\Lambda_*T}\|f(T)\|_2^2
&\ge
\frac34\cdot\frac{a^2\delta_*}{4}
-\frac{a^2\delta_*}{16}  \\
&=
\frac{a^2\delta_*}{8}
\ge \frac{a^2\delta_*}{32}.
\end{aligned}
\]
Thus
\[
\|f(T)\|_2
\ge
\left(\frac{\delta_*}{32D_{m_*}}\right)^{1/2}a e^{-\Lambda_*T}
=\theta_*a e^{-\Lambda_*T}.
\]

**Dependencies:** STEP2, STEP3.

---

### STEP5: Global Lower Bound for the Selected Mode

**Claim:** Assume \(k_*\ne0\). With \(B_*,\delta_*,\Lambda_*,\theta_*\) from STEP2 and STEP4, set
\[
\gamma_*:=
\max\left\{
  B_*,
  \Lambda_*+\delta_*^{-1}\log(\theta_*^{-1})
\right\}.
\]
Then for every \(t\ge0\),
\[
\|\rho_{k_*}(t,\cdot)\|_{L_y^2}
=
\|f(t)\|_{L_y^2}
\ge
a e^{-\gamma_*t}.
\]

**Proof:**
For \(0\le t\le\delta_*\), STEP2 gives
\[
\|f(t)\|_2\ge ae^{-B_*t}\ge ae^{-\gamma_*t}.
\]
For \(t\ge\delta_*\), STEP4 gives
\[
\|f(t)\|_2\ge\theta_*ae^{-\Lambda_*t}.
\]
Since \(0<\theta_*\le1\) and \(t/\delta_*\ge1\),
\[
\theta_*
=e^{-\log(\theta_*^{-1})}
\ge e^{-(t/\delta_*)\log(\theta_*^{-1})}.
\]
Therefore
\[
\theta_*ae^{-\Lambda_*t}
\ge
a\exp\left[-\left(\Lambda_*+\delta_*^{-1}\log(\theta_*^{-1})\right)t\right]
\ge ae^{-\gamma_*t}.
\]

**Dependencies:** STEP2, STEP4.

---

### STEP6: Normalized Short-Time Lower Bound for the Full Solution

**Claim:** Let
\[
N:=\|\rho_0\|_{L^2_{x,y}},\qquad
Q:=\frac{\|\nabla\rho_0\|_{L^2_{x,y}}}{\|\rho_0\|_{L^2_{x,y}}},
\qquad
C_{\rm short}:=Q^2e^{M_1}.
\]
Then
\[
\|\rho(t)\|_{L^2_{x,y}}\ge N e^{-C_{\rm short}t}
\qquad\text{for all }0\le t\le1.
\]

**Proof:**
Set
\[
E(t):=\|\rho(t)\|_2^2,\qquad F(t):=\|\nabla\rho(t)\|_2^2.
\]
The full energy identity is
\[
\frac12E'(t)=-F(t).
\]
We next estimate the ratio \(F/E\). Differentiating \(F\) and integrating by parts,
\[
\frac12F'(t)
=-\|D^2\rho(t)\|_2^2
-\operatorname{Re}\int_{\mathbb T^2}(\partial_yU)(t,y)\,\rho_y\,\overline{\rho_x}\,dxdy.
\]
The terms containing \(U\rho_{xx}\) and \(U\rho_{xy}\) vanish after integration by parts in \(x\), because \(U\) is independent of \(x\). Hence
\[
F'(t)
\le -2\|D^2\rho(t)\|_2^2+M_1F(t).
\]
By Cauchy's inequality in Fourier variables,
\[
F(t)^2
\le E(t)\|D^2\rho(t)\|_2^2.
\]
Indeed, if \(\rho=\sum_{n\in\mathbb Z^2}\rho_n e^{in\cdot z}\), then
\[
F=\sum_n |n|^2|\rho_n|^2,\qquad
\|D^2\rho\|_2^2=\sum_n |n|^4|\rho_n|^2,
\]
and the displayed inequality is Cauchy-Schwarz.

Let \(R(t):=F(t)/E(t)\). Since \(E'(t)=-2F(t)\),
\[
R'(t)
=\frac{F'(t)}{E(t)}-\frac{F(t)E'(t)}{E(t)^2}
\le
\frac{-2\|D^2\rho(t)\|_2^2+M_1F(t)}{E(t)}
+2R(t)^2
\le M_1R(t).
\]
Thus
\[
R(t)\le R(0)e^{M_1t}=Q^2e^{M_1t}.
\]
Since
\[
\frac{d}{dt}\log\|\rho(t)\|_2=-R(t),
\]
for \(0\le t\le1\) we have
\[
\log\frac{\|\rho(t)\|_2}{N}
\ge
-Q^2\int_0^t e^{M_1s}\,ds
\ge
-Q^2e^{M_1}t.
\]
This is exactly the stated lower bound.

**Dependencies:** Energy estimates for the full equation.

---

### STEP7: Explicit Lower-Decay Exponent

**Claim:** Define an explicit lower-decay exponent \(c_2\) as follows.

If some \(k\ne0\) has \(a_k>0\), choose \(k_*\ne0\) as in STEP1 and set
\[
c_2:=
\max\left\{
  2,\,
  C_{\rm short},\,
  \gamma_*+\log\left(\frac{N}{a}\right)
\right\}.
\]
Then
\[
\|\rho(t)\|_{L^2_{x,y}}\ge N e^{-c_2t}
\qquad(t\ge0).
\]

If \(a_k=0\) for every \(k\ne0\), choose any \(l_0\ne0\) with \(g_0^{l_0}\ne0\), set \(b:=|g_0^{l_0}|\), and define
\[
c_2:=
\max\left\{
  2,\,
  C_{\rm short},\,
  l_0^2+\log\left(\frac{N}{b}\right)
\right\}.
\]
Then again
\[
\|\rho(t)\|_{L^2_{x,y}}\ge N e^{-c_2t}
\qquad(t\ge0).
\]
In both cases \(c_2\) is an explicit finite expression in the Fourier coefficients of \(\rho_0\), \(\|\rho_0\|_{H^1}\), \(M_0=\|U\|_{L^\infty_tL^2_y}\), and \(M_1=\|\partial_yU\|_{L^\infty_tL^\infty_y}\), plus the displayed universal constants.

**Proof:**
For \(0\le t\le1\), STEP6 gives
\[
\|\rho(t)\|_2\ge Ne^{-C_{\rm short}t}\ge Ne^{-c_2t}.
\]

Assume first that some nonzero \(x\)-mode is present. For \(t\ge1\), Plancherel and STEP5 give
\[
\|\rho(t)\|_2\ge\|\rho_{k_*}(t)\|_{L^2_y}
\ge ae^{-\gamma_*t}.
\]
Since \(t\ge1\),
\[
ae^{-\gamma_*t}
=
N\exp\left[-\gamma_*t-\log\left(\frac Na\right)\right]
\ge
N\exp\left[-\left(\gamma_*+\log\left(\frac Na\right)\right)t\right]
\ge Ne^{-c_2t}.
\]

If no nonzero \(x\)-mode is present, STEP1 gives, for \(t\ge1\),
\[
\|\rho(t)\|_2\ge be^{-l_0^2t}.
\]
The same calculation gives
\[
be^{-l_0^2t}
=
N\exp\left[-l_0^2t-\log\left(\frac Nb\right)\right]
\ge
N\exp\left[-\left(l_0^2+\log\left(\frac Nb\right)\right)t\right]
\ge Ne^{-c_2t}.
\]
Together with the short-time estimate, this proves the claim.

**Dependencies:** STEP1, STEP5, STEP6.

---

### STEP8: Two-Sided Exponential Bound

**Claim:** Taking
\[
c_1:=1,\qquad c_2\text{ as in STEP7},
\]
one has, for every \(t\ge0\),
\[
\|\rho(0,\cdot)\|_{L^2_{x,y}}e^{-c_2t}
\le
\|\rho(t,\cdot)\|_{L^2_{x,y}}
\le
\|\rho(0,\cdot)\|_{L^2_{x,y}}e^{-c_1t}.
\]

**Proof:**
The lower bound is exactly STEP7. It remains only to prove the upper bound. Since the drift field \((U(t,y),0)\) is divergence-free,
\[
\frac12\frac{d}{dt}\|\rho(t)\|_2^2=-\|\nabla\rho(t)\|_2^2.
\]
The spatial mean is conserved and is zero. By Fourier series on \(\mathbb T^2\), every nonzero spatial mode has \(|(k,l)|^2\ge1\), so
\[
\|\rho(t)\|_2^2\le\|\nabla\rho(t)\|_2^2.
\]
Therefore
\[
\frac{d}{dt}\|\rho(t)\|_2^2\le-2\|\rho(t)\|_2^2.
\]
Gronwall's inequality gives
\[
\|\rho(t)\|_2^2\le e^{-2t}\|\rho_0\|_2^2,
\]
hence
\[
\|\rho(t)\|_2\le e^{-t}\|\rho_0\|_2.
\]
Because STEP7 defines \(c_2\ge2\), we have \(0<c_1=1<c_2\).

**Dependencies:** STEP7 and the Fourier-series Poincare inequality proved above.

---

### GOAL: Main Result

**Claim:**
\begin{problem}
Although the proof above is nonconstructive, based on the idea of this proof, find an explicit upper bound of $c_2$, in terms of $U(t,y)$ and $\rho(0,x,y)$. 
\end{problem}
\begin{problem}
Without above proof, prove Theorem \ref{main} with an explicit estimate of upper bound of $c_2$ in terms of $U(t,y)$ and $\rho(0,x,y)$.
\end{problem}

**Proof:**
The preceding steps give a complete proof of Theorem \(\ref{main}\) with the explicit choice
\[
c_1=1
\]
and \(c_2\) defined in STEP7. In the case where a nonzero \(x\)-mode is present, this explicit exponent is
\[
c_2=
\max\left\{
2,\,
Q^2e^{M_1},\,
\gamma_*+\log\left(\frac{N}{a}\right)
\right\},
\]
where
\[
\gamma_*=
\max\left\{
B_*,
\Lambda_*+\delta_*^{-1}\log(\theta_*^{-1})
\right\},
\]
\[
B_*=
8\left(1+k_*^2+
\frac{\|\partial_yg\|_2^2}{\|g\|_2^2}
+|k_*|M_1\left(1+\frac{\|\partial_yg\|_2}{\|g\|_2}\right)
\right),
\qquad
\delta_*=B_*^{-1},
\]
\[
\Lambda_*=k_*^2+\frac{m_*^2+(m_*+1)^2}{2},
\qquad
\theta_*=\left(\frac{\delta_*}{32D_{m_*}}\right)^{1/2},
\]
\[
D_{m_*}=10^4(1+k_*^2+m_*^2)^2,
\]
and \(m_*\) is the least integer \(m\ge1\) satisfying
\[
10^4C_{\rm emb}^2k_*^2M_0^2(m^{-4}+m^{-1/2})\le\frac14,
\qquad
10^4m^{-1}\le\frac{\delta_*}{16}.
\]
All quantities are determined explicitly by \(U\) and \(\rho_0\).

If the data are independent of \(x\), choose \(l_0\ne0\) with \(g_0^{l_0}\ne0\), put \(b=|g_0^{l_0}|\), and use
\[
c_2=
\max\left\{
2,\,
Q^2e^{M_1},\,
l_0^2+\log\left(\frac{N}{b}\right)
\right\}.
\]
STEP8 proves the desired two-sided estimate for all \(t\ge0\).

**Dependencies:** STEP8.

## Key Ideas

The proof selects one nonzero Fourier mode in \(x\), lifts it by \(e^{\Lambda_mt}\), and applies a time-Fourier resolvent estimate on a finite window \([0,T]\). The midpoint choice of \(\Lambda_m\) creates a uniform gap from all \(y\)-frequencies. A short-time lower mass estimate and the finite-window endpoint term then force an explicit lower bound for the selected mode at time \(T\). A separate full-solution short-time estimate removes the prefactor loss from selecting only one Fourier mode.

## Deviations from Decomposition Plan

The proof follows the decomposition structure, with two quantitative corrections and one usage note.

First, in STEP3 the initial-extension contribution is bounded by \(B_m=C_{\rm res}m^{-1}\), not by \(C_{\rm res}(k_*^4m^{-4}+m^{-2})\). This is the value obtained by carrying out the \(\tau\)-integral
\[
\int_{\mathbb R}
\frac{(k_*^2+l^2)^2}{(\tau^2+\alpha_l^2)(\tau^2+\Lambda_m^2)}\,d\tau.
\]
The weaker \(m^{-1}\) bound still tends to zero and is sufficient for STEP4.

Second, STEP6 is proved directly from the shear \(H^1/L^2\) ratio estimate, giving
\[
C_{\rm short}=Q^2e^{M_1}
\]
instead of the Appendix-A-style bounded-drift constant stated in the decomposition. This is more direct under the theorem's assumption
\(\|U\|_{L^\infty_tC^\infty_y}<\infty\).

Finally, the monotone-function lemma appearing in the copied problem text is not used. The proof obtains a uniform exponential lower bound from the finite-window endpoint estimate instead.