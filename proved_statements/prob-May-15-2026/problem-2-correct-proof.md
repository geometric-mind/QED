# Proof

## Problem Statement

Let $d\ge3$ be a fixed integer, and let $G=\mathbb Z_2\wr T_d$ be the lamplighter group on the $d$-regular tree $T_d$. Let $\mu$ be the switch-walk-switch measure on $G$. Determine the exact asymptotic of $\mu^{(2n)}(e)$ as $n\to\infty$ in the following sense: prove that there exists $C>0$ and function $\varepsilon(n)=o(1)$, we have
\[
p_{2n}(e,e)=\rho^{2n}_d\exp(-(C+\varepsilon(n))\frac{n}{\log^2n}).
\]
You may use the fact that the spectrum radius of the random walk on the lamplighter group is $$
\rho_d:=\frac{2\sqrt{d-1}}{d},
$$
without proving. In your proof, do not cite the paper ``The Anderson model on the Bethe lattice: Lifshitz Tails'' or any other unpublished work.

## Proof

Throughout the proof put
\[
b=d-1,\qquad \rho_d=\frac{2\sqrt b}{d}.
\]
We write $o$ for a fixed root of $T_d$ and write $p_n(e,e)=\mu^{(n)}(e)$.

### STEP1: Percolation Spectral Representation

**Claim:** Put \(b=d-1\). Let \(P_\omega\) be the equivariant killed transition operator on \(\ell^2(T_d)\),
\[
P_\omega(x,y)=\frac1d{\bf 1}_{\{x\sim y,\ x,y\text{ are open}\}},
\]
with closed vertices carrying the zero row and column. Define the trace
\[
\tau(F)=\mathbb E_{1/2}\langle \delta_o,F_\omega\delta_o\rangle
\]
for equivariant bounded random operators \(F_\omega\). Then there is a probability measure \(\nu_d\) supported in \([-\rho_d,\rho_d]\) such that, for every \(n\ge0\),
\[
p_{2n}(e,e)=\tau(P_\omega^{2n})
=\int_{[-\rho_d,\rho_d]}\lambda^{2n}\,d\nu_d(\lambda).
\]
Moreover, for every equivariant random subset \(W_\omega\subseteq T_d\), if \(Q_\omega\) denotes multiplication by \({\bf 1}_{W_\omega}\), then
\[
\tau(Q)=\mathbb P(o\in W_\omega).
\]

**Proof:**
Let
\[
x_0=o,x_1,\ldots,x_m=o,\qquad x_{i+1}\sim x_i,
\]
be a base simple-random-walk path on \(T_d\), and let
\[
R_m=\{x_0,x_1,\ldots,x_m\}
\]
be its range. For the switch-walk-switch walk with lamp group \(\mathbb Z_2\), conditional on this base path and on the event that the base walk returns to \(o\), the final lamp at each vertex in \(R_m\) is a sum in \(\mathbb Z_2\) of at least one independent uniform switch. These sums use disjoint families of switches for different vertices. Hence the final lamps on the vertices of \(R_m\) are independent uniform \(\mathbb Z_2\)-variables, and the probability that all of them are off is \(2^{-|R_m|}\). Therefore
\[
p_m(e,e)=
\sum_{\substack{x_0=o,\ x_m=o\\ x_{i+1}\sim x_i}}
d^{-m}\,2^{-|\{x_0,\ldots,x_m\}|}.
\tag{1.1}
\]

For Bernoulli site percolation with parameter \(1/2\),
\[
\langle\delta_o,P_\omega^m\delta_o\rangle
=
\sum_{\substack{x_0=o,\ x_m=o\\ x_{i+1}\sim x_i}}
d^{-m}
\prod_{v\in\{x_0,\ldots,x_m\}}{\bf 1}_{\{v\text{ open}\}}.
\]
Taking expectation over \(\omega\), the product has mean \(2^{-|R_m|}\), so the last display has expectation equal to (1.1). Thus
\[
p_m(e,e)=\tau(P_\omega^m)\qquad(m\ge0).
\tag{1.2}
\]
This direct computation is the special case needed here of the usual lamplighter/percolation identity. <cite>type=theorem; label=S1; title=On the spectrum of lamplighter groups and percolation clusters; authors=Franz Lehner, Markus Neuhauser, Wolfgang Woess; source_url=https://arxiv.org/abs/0712.3135; verifier_locator=Abstract; statement_match=exact; statement=We show that the spectral measure (Plancherel measure) of any symmetric "switch--walk--switch" random walk on $H \wr G$ coincides with the expected spectral measure (integrated density of states) of the random walk with absorbing boundary on the cluster of the group identity for Bernoulli site percolation on $X$ with parameter $p = 1/|H|$.; usage=used only as literature support for the path-sum identity proved explicitly in STEP1 in the special case \(H=\mathbb Z_2\) and \(X=T_d\).</cite>

It remains to justify the support. The operator \(P_\omega\) is self-adjoint. We prove \(\|P_\omega\|\le\rho_d\). Choose an end of \(T_d\) and let \(h:T_d\to\mathbb Z\) be the corresponding Busemann height, normalized so that every vertex has one neighbor of height \(h(x)-1\) and \(b\) neighbors of height \(h(x)+1\). Put
\[
\psi(x)=b^{-h(x)/2}>0.
\]
Then
\[
\sum_{y\sim x}\frac{\psi(y)}{\psi(x)}
=\sqrt b+b\cdot b^{-1/2}=2\sqrt b.
\tag{1.3}
\]
For a finitely supported \(f\),
\[
\begin{aligned}
|\langle Af,f\rangle|
&\le \sum_{x\sim y}|f(x)|\,|f(y)|\\
&\le \frac12\sum_{x\sim y}
\left(\frac{\psi(y)}{\psi(x)}|f(x)|^2
+\frac{\psi(x)}{\psi(y)}|f(y)|^2\right)\\
&= \sum_x |f(x)|^2\sum_{y\sim x}\frac{\psi(y)}{\psi(x)}
=2\sqrt b\,\|f\|_2^2,
\end{aligned}
\]
where \(A\) is the adjacency operator of \(T_d\). Thus \(\|A\|\le2\sqrt b\). Since \(P_\omega\) is the compression of \(A/d\) to the open vertices, extended by zero on closed vertices, \(\|P_\omega\|\le2\sqrt b/d=\rho_d\).

Define
\[
\nu_d(B)=\tau({\bf 1}_B(P_\omega)),\qquad B\subset\mathbb R\ \text{Borel}.
\]
The spectral theorem and the preceding norm bound give a probability measure supported on \([-\rho_d,\rho_d]\), and (1.2) gives
\[
p_{2n}(e,e)=\tau(P_\omega^{2n})
=\int_{[-\rho_d,\rho_d]}\lambda^{2n}\,d\nu_d(\lambda).
\]
Finally, for \(Q_\omega\) multiplication by \({\bf 1}_{W_\omega}\),
\[
\tau(Q)=\mathbb E\langle\delta_o,Q_\omega\delta_o\rangle
=\mathbb E\,{\bf 1}_{\{o\in W_\omega\}}
=\mathbb P(o\in W_\omega).
\]
This proves STEP1.

**Dependencies:** S1 for literature context; direct switch-walk-switch path computation; elementary weighted Schur bound.

---

### STEP2: Finite Bethe-Tree Trap Lower Bound

**Claim:** There exist constants \(c_d>0\) and \(K_d<\infty\) such that for every integer \(r\ge1\) and every \(n\ge1\),
\[
p_{2n}(e,e)\ge c_d(r+2)^{-3}\,2^{-K_d b^{r+1}}
\left(\rho_d\cos\frac{\pi}{r+2}\right)^{2n}.
\]
One may take \(K_d=3+1/(d-2)\).

**Proof:**
Fix one neighbor \(o^-\) of \(o\). Let \(A_r\) be the forward rooted \(b\)-ary tree of depth \(r\): it consists of \(o\) and all vertices reachable from \(o\) by a path of length at most \(r\) whose first step is not \(o^-\). Then
\[
|A_r|=\frac{b^{r+1}-1}{b-1},\qquad
|\partial A_r|=1+b^{r+1},
\tag{2.1}
\]
where \(\partial A_r\) is the external vertex boundary in \(T_d\).

Let \(E_r\) be the event that every vertex of \(A_r\) is open and every vertex of \(\partial A_r\) is closed. On \(E_r\), the open cluster of \(o\) is exactly \(A_r\). Since \(b-1=d-2\ge1\),
\[
\begin{aligned}
|A_r|+|\partial A_r|
&=\frac{b^{r+1}-1}{b-1}+1+b^{r+1}\\
&\le \left(3+\frac1{d-2}\right)b^{r+1}.
\end{aligned}
\]
Thus, with \(K_d=3+1/(d-2)\),
\[
\mathbb P(E_r)=2^{-|A_r|-|\partial A_r|}
\ge 2^{-K_d b^{r+1}}.
\tag{2.2}
\]

Put
\[
\theta=\frac{\pi}{r+2}.
\]
Define a radial vector \(u\) on \(A_r\) by assigning to each level-\(j\) vertex the value
\[
u_j=b^{-j/2}\sin((j+1)\theta),\qquad 0\le j\le r.
\]
Let \(A_{A_r}\) be the adjacency matrix of \(A_r\). We verify that \(u\) is an eigenvector. At the root,
\[
b u_1=\sqrt b\,\sin(2\theta)=2\sqrt b\cos\theta\,\sin\theta
=2\sqrt b\cos\theta\,u_0.
\]
For \(1\le j\le r-1\),
\[
\begin{aligned}
u_{j-1}+b u_{j+1}
&=b^{-(j-1)/2}\sin(j\theta)
+b\,b^{-(j+1)/2}\sin((j+2)\theta)\\
&=b^{-(j-1)/2}\bigl[\sin(j\theta)+\sin((j+2)\theta)\bigr]\\
&=2\sqrt b\cos\theta\,b^{-j/2}\sin((j+1)\theta)
=2\sqrt b\cos\theta\,u_j.
\end{aligned}
\]
At level \(r\), the only neighbor inside \(A_r\) is the parent. Since \((r+2)\theta=\pi\),
\[
u_{r-1}=b^{-(r-1)/2}\sin(r\theta)
=2\sqrt b\cos\theta\,b^{-r/2}\sin((r+1)\theta)
=2\sqrt b\cos\theta\,u_r.
\]
Therefore \(A_{A_r}u=2\sqrt b\cos\theta\,u\). The killed transition operator inherited from \(T_d\) is \(A_{A_r}/d\), so its principal eigenvalue is at least
\[
\lambda_r=\frac{2\sqrt b}{d}\cos\theta
=\rho_d\cos\frac{\pi}{r+2}.
\tag{2.3}
\]
It is the principal eigenvalue because \(u\) is positive on \(A_r\).

Let \(\phi_r\) be the normalized positive eigenfunction. Since level \(j\) has \(b^j\) vertices,
\[
\phi_r(o)^2
=
\frac{\sin^2\theta}
{\sum_{j=0}^r b^j b^{-j}\sin^2((j+1)\theta)}
=
\frac{\sin^2\theta}
{\sum_{k=1}^{r+1}\sin^2(k\theta)}.
\]
Using
\[
\sum_{k=1}^{r+1}\sin^2(k\theta)=\frac{r+2}{2}
\]
for \(\theta=\pi/(r+2)\), and using \(\sin\theta\ge 2\theta/\pi=2/(r+2)\) for \(r\ge1\), we obtain
\[
\phi_r(o)^2
=\frac{2\sin^2\theta}{r+2}
\ge\frac{8}{(r+2)^3}.
\tag{2.4}
\]

On \(E_r\), spectral expansion of the killed walk on the finite cluster \(A_r\) gives
\[
\langle\delta_o,P_\omega^{2n}\delta_o\rangle
\ge \phi_r(o)^2\lambda_r^{2n}.
\]
Taking expectation, and applying STEP1, (2.2), (2.3), and (2.4), gives the claim with \(c_d=8\). This proves STEP2.

**Dependencies:** STEP1; direct finite-tree eigenvector computation; Bernoulli site-percolation independence.

---

### STEP3: Lower Asymptotic Bound

**Claim:** With \(b=d-1\),
\[
p_{2n}(e,e)\ge
\rho_d^{2n}\exp\left[-\left(\pi^2(\log b)^2+o(1)\right)\frac{n}{\log^2 n}\right]
\qquad(n\to\infty).
\]

**Proof:**
For all sufficiently large \(n\), set
\[
r_n=\left\lfloor\log_b n-3\log_b\log n\right\rfloor.
\]
Then \(r_n\to\infty\), and
\[
b^{r_n+1}
\le b\,b^{\log_b n-3\log_b\log n}
=O\left(\frac{n}{(\log n)^3}\right)
=o\left(\frac{n}{\log^2 n}\right).
\tag{3.1}
\]
Also
\[
r_n+2=\frac{\log n}{\log b}\,(1+o(1)),
\qquad
\frac1{(r_n+2)^2}
=\frac{(\log b)^2}{\log^2 n}(1+o(1)).
\tag{3.2}
\]
As \(x\downarrow0\),
\[
\log\cos x=-\frac{x^2}{2}+O(x^4).
\]
Therefore
\[
\begin{aligned}
2n\log\cos\frac{\pi}{r_n+2}
&=-\frac{\pi^2 n}{(r_n+2)^2}
+O\left(\frac{n}{(r_n+2)^4}\right)\\
&=-\left(\pi^2(\log b)^2+o(1)\right)
\frac{n}{\log^2 n}.
\end{aligned}
\tag{3.3}
\]
The non-eigenvalue part of the lower bound in STEP2 contributes to the logarithm only
\[
O(b^{r_n+1})+O(\log r_n)
=o\left(\frac{n}{\log^2 n}\right)
\tag{3.4}
\]
by (3.1). Substituting \(r=r_n\) in STEP2 and using (3.3)--(3.4) proves STEP3.

**Dependencies:** STEP2.

---

### STEP4: Dense-Ball Faber-Krahn Stability ⭐ KEY STEP

**Claim:** For every \(\eta>0\) there exist constants
\[
a_\eta\in(0,1),\qquad c_\eta>0,\qquad \delta_0=\delta_0(d,\eta)>0
\]
such that the following deterministic statement holds. For \(0<\delta<\delta_0\), set
\[
r_\delta=\left\lfloor\frac{\pi/\sqrt2-\eta}{\sqrt\delta}\right\rfloor .
\]
If \(T\) is any connected subtree of \(T_d\), finite or infinite, and
\[
\sup_{v\in T}|T\cap B_{T_d}(v,r_\delta)|<a_\eta b^{r_\delta},
\]
then the killed transition operator \(P_T=A_T/d\) satisfies
\[
\sup\sigma(P_T)\le \rho_d(1-(1+c_\eta)\delta).
\]
Equivalently, if \(\sup\sigma(P_T)\ge \rho_d(1-\delta)\), then there exists \(v\in T\) with
\[
|T\cap B_{T_d}(v,r_\delta)|\ge a_\eta b^{r_\delta}.
\]

**Proof:**
<key-original-step>
We prove the contrapositive through a deterministic operator estimate.
For the harmless edge case in which the displayed integer \(r_\delta\le0\), we interpret \(B(v,r_\delta)\) as \(B(v,0)=\{v\}\). Then, since \(a_\eta<1\) and \(b^{r_\delta}\le1\), the sparse hypothesis is false for every nonempty connected subtree, while the dense alternative is automatic. Thus the only substantive case is \(r_\delta\ge1\).

First we need a one-dimensional moment inequality. Suppose \(\nu\) is a probability measure on \(\mathbb R\) with characteristic function
\[
\widehat\nu(t)=\int_{\mathbb R}e^{itx}\,d\nu(x)
\]
and suppose \(\widehat\nu(t)=0\) for \(|t|\ge1\). Then
\[
\int_{\mathbb R}x^2\,d\nu(x)\ge \pi^2,
\tag{4.1}
\]
with the convention that the inequality is automatic when the second moment is infinite. Indeed, the Boas--Kac--Krein convolution-root theorem gives a function \(h\in L^2(\mathbb R)\), supported in an interval of length \(1\), such that
\[
\widehat\nu(t)=\int_{\mathbb R}h(s+t)\overline{h(s)}\,ds.
\]
<cite>type=theorem; label=BKK; title=Convolution roots of radial positive definite functions with compact support; authors=Werner Ehm, Tilmann Gneiting, Donald Richards; source_url=https://pure.psu.edu/en/publications/convolution-roots-of-radial-positive-definite-functions-with-comp; verifier_locator=Abstract, lines 30-31; statement_match=exact; statement=A classical theorem of Boas, Kac, and Krein states that a characteristic function ψ with ψ(x) = 0 for |x| ≥ τ admits a representation of the form ψ (x) = ∫ u(y)u(y + x) dy, x ∈ ℝ, where the convolution root u ∈ L^{2} (ℝ) is complex-valued with u(x) = 0 for |x| ≥ τ/2.; usage=used with \(\tau=1\) to factor the compactly supported characteristic function in STEP4 and derive the sharp second-moment lower bound \(\int x^2\,d\nu(x)\ge\pi^2\) by the Dirichlet Poincare inequality.</cite>
With the Fourier transform convention
\[
\widehat h(x)=\int_{\mathbb R}e^{-itx}h(t)\,dt,
\]
Fourier inversion gives that \(\nu\) has density \((2\pi)^{-1}|\widehat h(x)|^2\). Hence, if \(h\in H^1\),
\[
\int x^2\,d\nu(x)
=\frac1{2\pi}\int x^2|\widehat h(x)|^2\,dx
=\int |h'(t)|^2\,dt.
\]
If \(h\notin H^1\), the second moment is infinite. Since \(h\) is supported in an interval of length \(1\), the Dirichlet Poincare inequality gives
\[
\int |h'|^2\ge \pi^2\int |h|^2.
\]
For completeness, after translating the interval to \([0,1]\), the sine expansion
\(h(t)=\sum_{k\ge1}a_k\sin(k\pi t)\) gives
\[
\int_0^1|h'|^2=\frac{\pi^2}{2}\sum_{k\ge1}k^2|a_k|^2
\ge \frac{\pi^2}{2}\sum_{k\ge1}|a_k|^2
=\pi^2\int_0^1|h|^2,
\]
and the general \(H^1_0\) case follows by approximation.
Finally, \(\int |h|^2=\widehat\nu(0)=1\). This proves (4.1).

Next we prove the sharp contraction estimate needed for the tree. Let \(0<\gamma<\pi^2/2\). We claim that there are \(\varepsilon=\varepsilon(\gamma)>0\) and \(m_0=m_0(\gamma)\) such that for every contraction \(S\) on a Hilbert space and every \(m\ge m_0\),
\[
\|S^m\|\le\varepsilon
\quad\Longrightarrow\quad
w(S)\le1-\frac{\gamma}{m^2},
\tag{4.2}
\]
where
\[
w(S)=\sup_{\|u\|=1}|\langle Su,u\rangle|
\]
is the numerical radius.

Assume (4.2) is false. Then there are contractions \(S_j\), integers \(m_j\to\infty\), and \(\varepsilon_j\downarrow0\) such that
\[
\|S_j^{m_j}\|\le\varepsilon_j,
\qquad
w(S_j)>1-\frac{\gamma}{m_j^2}.
\tag{4.3}
\]
Multiplying \(S_j\) by a complex scalar of modulus \(1\), which does not change \(\|S_j^{m_j}\|\), we may choose unit vectors \(\xi_j\) satisfying
\[
\operatorname{Re}\langle S_j\xi_j,\xi_j\rangle
\ge 1-\frac{\gamma+o(1)}{m_j^2}.
\tag{4.4}
\]

For each \(j\), construct an isometric dilation as follows. Let
\[
D_j=(I-S_j^*S_j)^{1/2}
\]
and define \(V_j\) on the Hilbert direct sum
\[
\mathcal H_j^+=\mathcal H_j\oplus\mathcal H_j\oplus\mathcal H_j\oplus\cdots
\]
by
\[
V_j(x_0,x_1,x_2,\ldots)
=(S_jx_0,D_jx_0,x_1,x_2,\ldots).
\]
Then
\[
\|S_jx_0\|^2+\|D_jx_0\|^2=\|x_0\|^2,
\]
so \(V_j\) is an isometry. Embed \(\xi_j\) as \((\xi_j,0,0,\ldots)\). The first coordinate of \(V_j^k\xi_j\) is \(S_j^k\xi_j\), so
\[
\langle V_j^k\xi_j,\xi_j\rangle=\langle S_j^k\xi_j,\xi_j\rangle
\qquad(k\ge0).
\tag{4.5}
\]
Extend \(V_j\) explicitly to a unitary. On
\[
\mathcal K_j=\mathcal H_j^+\oplus\mathcal H_j^+
\]
define
\[
W_j(x,y)=\bigl(V_jx+(I-V_jV_j^*)y,\,-V_j^*y\bigr).
\]
The range projection of \(V_j\) is \(V_jV_j^*\). Thus \(V_jx\) is orthogonal to \((I-V_jV_j^*)y\), and
\[
\|W_j(x,y)\|^2
=\|x\|^2+\|(I-V_jV_j^*)y\|^2+\|V_j^*y\|^2
=\|x\|^2+\|y\|^2.
\]
The inverse is
\[
W_j^{-1}(u,v)=\bigl(V_j^*u,\,(I-V_jV_j^*)u-V_jv\bigr),
\]
so \(W_j\) is unitary. Embed \(\xi_j\) in \(\mathcal K_j\) as \((\xi_j,0)\). Since
\[
W_j(x,0)=(V_jx,0),
\]
we have \(W_j^k(\xi_j,0)=(V_j^k\xi_j,0)\) for \(k\ge0\). Hence, by (4.5),
\[
\langle W_j^k(\xi_j,0),(\xi_j,0)\rangle
=\langle S_j^k\xi_j,\xi_j\rangle
\qquad(k\ge0).
\tag{4.6}
\]
By the spectral theorem for the unitary \(W_j\), there is a probability measure \(\mu_j\) on the unit circle whose Fourier coefficients satisfy
\[
\widehat\mu_j(k)=\langle S_j^k\xi_j,\xi_j\rangle\qquad(k\ge0).
\]
Writing the circle as \(\theta\in[-\pi,\pi)\), push \(\mu_j\) forward under \(t=m_j\theta\); call the resulting probability measure on \([-\pi m_j,\pi m_j)\) by \(\nu_j\).

From (4.4),
\[
\int(1-\cos\theta)\,d\mu_j(\theta)
=1-\operatorname{Re}\widehat\mu_j(1)
\le\frac{\gamma+o(1)}{m_j^2}.
\tag{4.7}
\]
Since \(1-\cos\theta\ge 2\theta^2/\pi^2\) on \([-\pi,\pi]\), (4.7) gives a uniform second-moment bound for \(\nu_j\):
\[
\int t^2\,d\nu_j(t)
=m_j^2\int\theta^2\,d\mu_j(\theta)
\le \frac{\pi^2}{2}(\gamma+o(1)).
\tag{4.8}
\]
The bound (4.8) implies tightness by Markov's inequality. After passing to a subsequence, \(\nu_j\) converges weakly to a probability measure \(\nu\).

Fix \(s\ge1\) and put \(k_j=\lfloor s m_j\rfloor\). For all large \(j\), \(k_j\ge m_j\), so by (4.3),
\[
\left|\int e^{i(k_j/m_j)t}\,d\nu_j(t)\right|
=|\widehat\mu_j(k_j)|
=|\langle S_j^{k_j}\xi_j,\xi_j\rangle|
\le\|S_j^{k_j}\|
\le\|S_j^{m_j}\|
\le\varepsilon_j\to0.
\]
Because \(k_j/m_j\to s\) and the first moments of \(\nu_j\) are uniformly bounded by (4.8), weak convergence implies
\[
\widehat\nu(s)=0\qquad(s\ge1).
\]
Indeed, if \(\alpha_j=k_j/m_j\), then
\[
\left|\int(e^{i\alpha_j t}-e^{ist})\,d\nu_j(t)\right|
\le |\alpha_j-s|\sup_j\int |t|\,d\nu_j(t)\to0,
\]
and \(\int e^{ist}\,d\nu_j(t)\to\int e^{ist}\,d\nu(t)\) by weak convergence.
By conjugation, \(\widehat\nu(s)=0\) also for \(s\le-1\). Hence (4.1) gives
\[
\int t^2\,d\nu(t)\ge\pi^2.
\]
On the other hand, (4.7) says
\[
\int m_j^2(1-\cos(t/m_j))\,d\nu_j(t)
\le\gamma+o(1).
\]
For each fixed \(R\), choose a continuous cutoff \(\chi_R\) with \(0\le\chi_R\le1\), \(\chi_R=1\) on \([-R,R]\), and support in \([-R-1,R+1]\). The functions \(\chi_R(t)m_j^2(1-\cos(t/m_j))\) converge uniformly to \(\chi_R(t)t^2/2\), so weak convergence and nonnegativity give
\[
\frac12\int_{|t|\le R}t^2\,d\nu(t)
\le \frac12\int \chi_R(t)t^2\,d\nu(t)
\le \gamma.
\]
Letting \(R\to\infty\) gives \(\int t^2\,d\nu(t)\le2\gamma<\pi^2\), contradicting the preceding lower bound. This proves the contraction estimate (4.2).

Now let \(T\) be a connected subtree of \(T_d\), not equal to all of \(T_d\). Choose a boundary edge \(o^-o\) with \(o\in T\) and \(o^-\notin T\), and root \(T\) at \(o\), oriented away from \(o^-\). Every vertex then has at most \(b\) children. Let \(|x|\) be rooted distance from \(o\), set
\[
m(x)=b^{-|x|},
\]
and define \(U:\ell^2(T)\to\ell^2(T,m)\) by
\[
(Uf)(x)=b^{|x|/2}f(x).
\]
Define the backward shift \(S\) on \(\ell^2(T,m)\) by
\[
(Sg)(x)=
\begin{cases}
g(\bar x),&x\ne o,\\
0,&x=o,
\end{cases}
\]
where \(\bar x\) is the parent of \(x\). If \(c(y)\le b\) is the number of children of \(y\), then
\[
\|Sg\|_{\ell^2(m)}^2
=\sum_{x\ne o}b^{-|x|}|g(\bar x)|^2
=\sum_y\frac{c(y)}{b}b^{-|y|}|g(y)|^2
\le\|g\|_{\ell^2(m)}^2,
\]
so \(S\) is a contraction.

A direct computation gives
\[
UA_TU^{-1}=\sqrt b\,(S+S^*).
\tag{4.9}
\]
Indeed, for \(x\ne o\),
\[
(UA_TU^{-1}g)(x)
=\sqrt b\,g(\bar x)+\frac1{\sqrt b}\sum_{y:\bar y=x}g(y),
\]
and the root formula is the same without the parent term, while
\[
(S^*g)(x)=\frac1b\sum_{y:\bar y=x}g(y).
\]
For \(k\ge1\), let \(D_k(x)\) be the number of descendants of \(x\) at rooted distance exactly \(k\). Since \(S^kg\) copies \(g(x)\) to the descendants of \(x\) at distance \(k\),
\[
\|S^kg\|^2
=\sum_x b^{-|x|}|g(x)|^2\frac{D_k(x)}{b^k},
\]
and hence
\[
\|S^k\|^2=\sup_{x\in T}\frac{D_k(x)}{b^k}.
\tag{4.10}
\]
Finally, if \(G_\theta g(x)=e^{i\theta |x|}g(x)\), then \(G_\theta\) is unitary and
\[
G_\theta S G_\theta^{-1}=e^{i\theta}S.
\]
Since
\[
2w(S)=\sup_{\theta\in\mathbb R}
\|e^{i\theta}S+e^{-i\theta}S^*\|,
\]
the gauge equivalence implies
\[
\|S+S^*\|=2w(S).
\tag{4.11}
\]

We now choose constants. If \(\eta\ge\pi/\sqrt2\), take \(a_\eta=1/2\), \(c_\eta=1\), and \(\delta_0=1\). Then \(r_\delta\le0\) for every \(0<\delta<\delta_0\), so the assertion follows from the convention in the preceding paragraph. Hence assume \(0<\eta<\pi/\sqrt2\). Put
\[
A_\eta=\frac{\pi}{\sqrt2}-\eta.
\]
Choose \(\gamma\) with
\[
A_\eta^2<\gamma<\frac{\pi^2}{2}.
\]
Let \(\varepsilon=\varepsilon(\gamma)\) and \(m_0=m_0(\gamma)\) be supplied by (4.2), and set
\[
a_\eta=\min\{\varepsilon^2,1/2\}.
\]
Choose \(\delta_0>0\) so small that
\[
r_\delta=\left\lfloor\frac{A_\eta}{\sqrt\delta}\right\rfloor\ge m_0
\qquad(0<\delta<\delta_0).
\]

Assume
\[
\sup_{v\in T}|T\cap B(v,r_\delta)|<a_\eta b^{r_\delta}.
\tag{4.12}
\]
Because \(a_\eta\le1/2\), the full tree \(T_d\) cannot satisfy (4.12) for \(r_\delta\ge1\), so the preceding rooted representation applies. Descendant spheres are contained in ordinary balls, so (4.10) and (4.12) give
\[
\|S^{r_\delta}\|^2
=\sup_x\frac{D_{r_\delta}(x)}{b^{r_\delta}}
\le \sup_x\frac{|T\cap B(x,r_\delta)|}{b^{r_\delta}}
<a_\eta\le\varepsilon^2.
\]
Thus \(\|S^{r_\delta}\|\le\varepsilon\). By (4.2),
\[
w(S)\le1-\frac{\gamma}{r_\delta^2}.
\]
Since \(r_\delta\le A_\eta/\sqrt\delta\),
\[
\frac{\gamma}{r_\delta^2}\ge \frac{\gamma}{A_\eta^2}\delta.
\]
Define
\[
c_\eta=\frac{\gamma}{A_\eta^2}-1>0.
\]
Then
\[
w(S)\le1-(1+c_\eta)\delta.
\tag{4.13}
\]
Using (4.9), (4.11), and (4.13),
\[
\sup\sigma(A_T)\le\|A_T\|
=\sqrt b\,\|S+S^*\|
=2\sqrt b\,w(S)
\le2\sqrt b(1-(1+c_\eta)\delta).
\]
After division by \(d\),
\[
\sup\sigma(P_T)\le \rho_d(1-(1+c_\eta)\delta).
\]
This proves the sparse-ball implication. The dense-ball alternative is exactly its contrapositive.
</key-original-step><heuristics>The estimate works because a tree whose radius-\(r\) balls contain only \(a b^r\) vertices has a rooted backward shift \(S\) with \(\|S^r\|\le\sqrt a\). A contraction can have numerical radius within \(\gamma/r^2\) of \(1\) only if its \(r\)-th power remains bounded away from zero; the sharp obstruction is the one-dimensional Dirichlet eigenvalue \(\pi^2\), which becomes \(\pi^2/2\) after passing from \(1-\cos\theta\) to \(\theta^2/2\). Thus near-edge spectrum forces almost full \(b\)-ary growth for order \(\delta^{-1/2}\) generations, and this is exactly the dense local ball witness.</heuristics>

This proves STEP4.

**Dependencies:** Boas--Kac--Krein theorem citation BKK; elementary dilation of a contraction to an isometry; rooted-shift representation. This step intentionally replaces the decomposition plan's S3/S4 comparison route; see "Deviations from Decomposition Plan."

---

### STEP5: Dense Percolation Balls Are Rare

**Claim:** For every \(a\in(0,1)\) and every \(\zeta>0\) there exist constants \(r_0=r_0(d,a,\zeta)\) and \(c=c(d,a,\zeta)>0\) such that, for Bernoulli site percolation on \(T_d\) with parameter \(1/2\),
\[
\mathbb P\left(|C_\omega(o)\cap B_{T_d}(o,r)|\ge a b^r\right)
\le \exp\left[-c\,b^r r^{-2}\right]
\le \exp\left[-\exp((\log b-\zeta)r)\right]
\]
for every \(r\ge r_0\), where \(C_\omega(o)\) is the open cluster of \(o\), interpreted as empty when \(o\) is closed.

**Proof:**
Let \(Z_j\) be the number of vertices in \(C_\omega(o)\) at distance \(j\) from \(o\). If \(o\) is closed, all \(Z_j=0\). Conditional on the open vertices in generation \(j-1\), every possible forward child in generation \(j\) is independently open with probability \(1/2\), and each vertex in generation \(j-1\) has at most \(b\) forward children.

Choose an integer \(L=L(a,d)\) such that for all large \(r\),
\[
|B(o,r-L)|\le \frac a4 b^r.
\tag{5.1}
\]
This is possible because \(|B(o,R)|\le C_d b^R\). Put
\[
\alpha=\frac{a(b-1)}{4b}.
\tag{5.2}
\]
Suppose \(\sum_{j=0}^r Z_j\ge a b^r\). If for every \(j\in\{r-L+1,\ldots,r\}\) we had \(Z_j<\alpha b^j\), then by (5.1) and (5.2),
\[
\sum_{j=0}^r Z_j
\le |B(o,r-L)|+\alpha\sum_{j=r-L+1}^r b^j
\le \frac a4 b^r+\frac{a(b-1)}{4b}\cdot\frac{b^{r+1}}{b-1}
=\frac a2 b^r,
\]
contradicting \(\sum_{j=0}^r Z_j\ge a b^r\). Therefore
\[
\left\{\sum_{j=0}^r Z_j\ge a b^r\right\}
\subseteq
\bigcup_{j=r-L+1}^r\{Z_j\ge\alpha b^j\}.
\tag{5.3}
\]

We now prove that for each fixed \(\alpha>0\) there are \(c_\alpha>0\) and \(j_0\) such that
\[
\mathbb P(Z_j\ge\alpha b^j)\le e^{-c_\alpha b^j}
\qquad(j\ge j_0).
\tag{5.4}
\]
Let
\[
D=\frac d b=1+\frac1b<2.
\]
The number of vertices in the sphere of radius \(j\) is at most \(D b^j\). Choose a finite chain
\[
\alpha=\alpha_0<\alpha_1<\cdots<\alpha_m<D
\]
such that
\[
\frac{\alpha_i}{\alpha_{i+1}}>\frac12\quad(0\le i<m),
\qquad
\alpha_m>\frac D2.
\tag{5.5}
\]
Such a chain exists because \(\alpha<D\) and \(D<2\).

We shall use the following elementary binomial estimate. If \(X\sim\operatorname{Bin}(N,1/2)\) and \(q>1/2\), choose \(t>0\). Then
\[
\mathbb P(X\ge qN)
\le e^{-tqN}\mathbb E e^{tX}
=\left(e^{-tq}\frac{1+e^t}{2}\right)^N.
\]
For \(t>0\) small enough after \(q>1/2\) is fixed, the factor in parentheses is strictly less than \(1\); hence \(\mathbb P(X\ge qN)\le e^{-I(q)N}\) for some \(I(q)>0\).

Fix \(i<m\). On the event
\[
Z_j\ge\alpha_i b^j,\qquad Z_{j-1}<\alpha_{i+1}b^{j-1},
\]
at least \(\alpha_i b^j\) open forward children must appear among fewer than \(\alpha_{i+1}b^j\) possible child sites. If the number \(N\) of possible child sites is below \(\alpha_i b^j\), this event is impossible; otherwise \(N\ge\alpha_i b^j\), and the required success fraction is at least \(\alpha_i/\alpha_{i+1}>1/2\). Thus the preceding binomial estimate gives a constant \(\gamma_i>0\) such that
\[
\mathbb P\bigl(Z_j\ge\alpha_i b^j,\ Z_{j-1}<\alpha_{i+1}b^{j-1}\bigr)
\le e^{-\gamma_i b^j}.
\tag{5.6}
\]
Consequently,
\[
\mathbb P(Z_j\ge\alpha_i b^j)
\le
\mathbb P(Z_{j-1}\ge\alpha_{i+1}b^{j-1})
+e^{-\gamma_i b^j}.
\tag{5.7}
\]
Iterating (5.7) for \(i=0,\ldots,m-1\), it remains to bound
\[
\mathbb P(Z_{j-m}\ge\alpha_m b^{j-m}).
\]
Since \(Z_{j-m}\) is bounded above by the number of open vertices in the sphere of radius \(j-m\), and that sphere has at most \(D b^{j-m}\) vertices, the threshold fraction is at least \(\alpha_m/D>1/2\) whenever the event is possible. The same binomial estimate gives
\[
\mathbb P(Z_{j-m}\ge\alpha_m b^{j-m})
\le e^{-\gamma_m b^{j-m}}
\le e^{-\gamma_m b^{-m} b^j}.
\tag{5.8}
\]
Combining (5.7) and (5.8), and decreasing the constant to absorb the fixed number \(m\) of terms, proves (5.4).

By (5.3) and (5.4),
\[
\mathbb P\left(|C_\omega(o)\cap B(o,r)|\ge a b^r\right)
\le L e^{-c_\alpha b^{r-L+1}}
\le e^{-c_1 b^r}
\tag{5.9}
\]
for all sufficiently large \(r\). Weakening the constant gives
\[
e^{-c_1 b^r}\le e^{-c b^r r^{-2}}.
\]
Finally, because
\[
\log(c b^r r^{-2})=\log c+r\log b-2\log r
\ge(\log b-\zeta)r
\]
for all sufficiently large \(r\), we have
\[
c b^r r^{-2}\ge \exp((\log b-\zeta)r).
\]
This proves both displayed inequalities and hence STEP5.

**Dependencies:** Bernoulli independence on \(T_d\); elementary binomial exponential bounds proved in the step.

---

### STEP6: Spectral Mass Is Bounded by Witness Density ⭐ KEY STEP

**Claim:** Let \(P_\omega\) be a bounded self-adjoint equivariant random operator on \(\ell^2(T_d)\), let \(W_\omega\) be an equivariant random subset, and let \(Q_\omega\) be multiplication by \({\bf 1}_{W_\omega}\). Suppose that for deterministic numbers \(E_0<E\),
\[
\sup\sigma\big((1-Q_\omega)P_\omega(1-Q_\omega)\big)\le E_0
\qquad\text{almost surely.}
\]
Then
\[
\tau\left({\bf 1}_{[E,\infty)}(P_\omega)\right)\le \tau(Q_\omega)
=\mathbb P(o\in W_\omega).
\]
If the same hypothesis holds with \(P_\omega\) replaced by \(-P_\omega\), then
\[
\tau\left({\bf 1}_{(-\infty,-E]\cup[E,\infty)}(P_\omega)\right)
\le 2\,\mathbb P(o\in W_\omega).
\]

**Proof:**
<key-original-step>
Let
\[
\Pi_\omega={\bf 1}_{[E,\infty)}(P_\omega).
\]
Take \(f\in\operatorname{Ran}\Pi_\omega\) with \(Q_\omega f=0\). Then \(f=(1-Q_\omega)f\). By the spectral theorem applied to the restriction of \(P_\omega\) to \(\operatorname{Ran}\Pi_\omega\),
\[
\langle P_\omega f,f\rangle\ge E\|f\|^2.
\tag{6.1}
\]
On the other hand, since \(f=(1-Q_\omega)f\),
\[
\langle P_\omega f,f\rangle
=
\langle(1-Q_\omega)P_\omega(1-Q_\omega)f,f\rangle
\le E_0\|f\|^2.
\tag{6.2}
\]
Because \(E_0<E\), (6.1)--(6.2) force \(f=0\). Hence \(Q_\omega\Pi_\omega\) is injective on \(\operatorname{Ran}\Pi_\omega\).

Set
\[
T_\omega=Q_\omega\Pi_\omega.
\]
In the finite von Neumann algebra of equivariant random operators with trace \(\tau\), the support projection of \(T_\omega^*T_\omega\) is \(\Pi_\omega\), because \(T_\omega\) has no kernel on \(\operatorname{Ran}\Pi_\omega\). The support projection of \(T_\omega T_\omega^*\) is dominated by \(Q_\omega\), because \(\operatorname{Ran}T_\omega\subseteq\operatorname{Ran}Q_\omega\). Let
\[
T_\omega=V_\omega|T_\omega|
\]
be the polar decomposition. Then
\[
V_\omega^*V_\omega=s(T_\omega^*T_\omega)=\Pi_\omega,
\qquad
V_\omega V_\omega^*=s(T_\omega T_\omega^*)\le Q_\omega,
\]
where \(s(\cdot)\) denotes the support projection. Since \(\tau\) is tracial on equivariant random operators,
\[
\tau(\Pi_\omega)
=\tau(V_\omega^*V_\omega)
=\tau(V_\omega V_\omega^*)
\le\tau(Q_\omega).
\]
Thus
\[
\tau({\bf 1}_{[E,\infty)}(P_\omega))\le\tau(Q_\omega).
\]
STEP1 gives \(\tau(Q_\omega)=\mathbb P(o\in W_\omega)\).

If the same hypothesis holds with \(P_\omega\) replaced by \(-P_\omega\), the identical argument gives
\[
\tau({\bf 1}_{[E,\infty)}(-P_\omega))\le\tau(Q_\omega),
\]
that is,
\[
\tau({\bf 1}_{(-\infty,-E]}(P_\omega))\le\tau(Q_\omega).
\]
Adding this to the positive-edge estimate yields
\[
\tau\left({\bf 1}_{(-\infty,-E]\cup[E,\infty)}(P_\omega)\right)
\le2\tau(Q_\omega)=2\mathbb P(o\in W_\omega).
\]
</key-original-step><heuristics>The high-energy subspace cannot contain a nonzero vector supported entirely outside the witness set, because outside the witnesses the compressed operator has spectral top below \(E\). Therefore the map \(f\mapsto Qf\) embeds the high-energy subspace into \(\ell^2(W)\). In a finite trace setting, an equivariant injection cannot increase von Neumann dimension, so the trace per root of the high-energy spectral projection is bounded by the root density of \(W\).</heuristics>

This proves STEP6.

**Dependencies:** STEP1; spectral theorem; polar decomposition and traciality in the equivariant random-operator von Neumann algebra.

---

### STEP7: Double-Exponential Spectral Edge Tail

**Claim:** Let \(\nu_d\) be the spectral measure from STEP1 and put
\[
\kappa_d=\frac{\pi}{\sqrt2}\log b.
\]
For every \(\eta>0\) there exist \(c=c(d,\eta)>0\) and \(\delta_0=\delta_0(d,\eta)>0\) such that, for all \(0<\delta<\delta_0\),
\[
\nu_d\big(\{\lambda:\ |\lambda|\ge \rho_d(1-\delta)\}\big)
\le
\exp\left[-c\exp\left(\frac{\kappa_d-\eta}{\sqrt\delta}\right)\right].
\]

**Proof:**
It is enough to prove the assertion for \(0<\eta<\kappa_d/2\), since larger \(\eta\) only weaken the bound.

Apply STEP4 with
\[
\eta_4=\frac{\eta}{4\log b}.
\]
Let \(a=a_{\eta_4}\) and \(c_4=c_{\eta_4}\). For sufficiently small \(\delta\), set
\[
r_\delta=
\left\lfloor
\frac{\pi/\sqrt2-\eta_4}{\sqrt\delta}
\right\rfloor.
\]
Define the equivariant witness set
\[
W_\delta(\omega)=
\left\{v:\ |C_\omega(v)\cap B(v,r_\delta)|\ge a b^{r_\delta}\right\},
\]
and let \(Q_\delta\) be multiplication by \({\bf 1}_{W_\delta}\).

After deleting \(W_\delta\), every remaining open component \(T\) satisfies
\[
\sup_{v\in T}|T\cap B(v,r_\delta)|<a b^{r_\delta}.
\]
Indeed, if \(v\) remains, then \(v\notin W_\delta\), and the component of \(v\) after deletion is a subset of the original open cluster \(C_\omega(v)\). STEP4 therefore gives
\[
\sup\sigma((1-Q_\delta)P_\omega(1-Q_\delta))
\le \rho_d(1-(1+c_4)\delta)
<\rho_d(1-\delta).
\tag{7.1}
\]
Every open subgraph of \(T_d\) is bipartite. On each connected component, multiplication by \(+1\) on one bipartition class and by \(-1\) on the other conjugates the adjacency operator to its negative. Hence the same bound (7.1) holds for \(-P_\omega\).

Applying STEP6 with \(E=\rho_d(1-\delta)\) gives
\[
\nu_d\{\lambda:\ |\lambda|\ge \rho_d(1-\delta)\}
\le 2\mathbb P(o\in W_\delta).
\tag{7.2}
\]
By STEP5,
\[
\mathbb P(o\in W_\delta)
\le \exp[-c_1 b^{r_\delta}r_\delta^{-2}]
\tag{7.3}
\]
for all sufficiently small \(\delta\).

Since
\[
r_\delta=
\left(\frac{\pi}{\sqrt2}-\eta_4+o(1)\right)\delta^{-1/2},
\]
we have
\[
\log(b^{r_\delta}r_\delta^{-2})
=r_\delta\log b-2\log r_\delta
\ge \frac{\kappa_d-\eta}{\sqrt\delta}
\tag{7.4}
\]
for all sufficiently small \(\delta\). Combining (7.2)--(7.4), and reducing the exponent constant to absorb the factor \(2\), proves STEP7.

**Dependencies:** STEP1, STEP4, STEP5, STEP6.

---

### STEP8: Upper Asymptotic Bound

**Claim:** With \(b=d-1\),
\[
p_{2n}(e,e)\le
\rho_d^{2n}\exp\left[-\left(\pi^2(\log b)^2-o(1)\right)\frac{n}{\log^2 n}\right]
\qquad(n\to\infty).
\]

**Proof:**
Recall
\[
\kappa_d=\frac{\pi}{\sqrt2}\log b.
\]
Fix \(0<\eta<\kappa_d/4\), and set
\[
\delta_n=\left(\frac{\kappa_d-2\eta}{\log n}\right)^2.
\]
By STEP1,
\[
p_{2n}(e,e)=\int |\lambda|^{2n}\,d\nu_d(\lambda).
\]
Split the integral into
\[
I_1=\int_{\{|\lambda|\le\rho_d(1-\delta_n)\}}|\lambda|^{2n}\,d\nu_d(\lambda),
\qquad
I_2=\int_{\{|\lambda|>\rho_d(1-\delta_n)\}}|\lambda|^{2n}\,d\nu_d(\lambda).
\]
For the first part,
\[
I_1\le \rho_d^{2n}(1-\delta_n)^{2n}
\le \rho_d^{2n}\exp(-2n\delta_n)
=\rho_d^{2n}
\exp\left[-2(\kappa_d-2\eta)^2\frac{n}{\log^2 n}\right].
\tag{8.1}
\]
For the second part, STEP7 gives
\[
I_2\le
\rho_d^{2n}
\exp\left[
-c\exp\left(\frac{\kappa_d-\eta}{\sqrt{\delta_n}}\right)
\right].
\]
Since
\[
\sqrt{\delta_n}=\frac{\kappa_d-2\eta}{\log n},
\]
this becomes
\[
I_2\le
\rho_d^{2n}
\exp\left[
-c n^{(\kappa_d-\eta)/(\kappa_d-2\eta)}
\right].
\tag{8.2}
\]
The exponent
\[
\frac{\kappa_d-\eta}{\kappa_d-2\eta}>1,
\]
so (8.2) is smaller than
\[
\rho_d^{2n}\exp\left[-M\frac{n}{\log^2 n}\right]
\]
for every fixed \(M>0\), once \(n\) is large enough. Combining this with (8.1),
\[
p_{2n}(e,e)
\le
\rho_d^{2n}
\exp\left[
-\left(2(\kappa_d-2\eta)^2-o(1)\right)\frac{n}{\log^2 n}
\right].
\]
Since \(\eta>0\) is arbitrary and
\[
2\kappa_d^2
=2\left(\frac{\pi}{\sqrt2}\log b\right)^2
=\pi^2(\log b)^2,
\]
we obtain the claimed upper bound. This proves STEP8.

**Dependencies:** STEP1, STEP7.

---

### STEP9: Squeezing the Constant

**Claim:** Let
\[
C_d=\pi^2(\log(d-1))^2
\]
and define
\[
\varepsilon(n)=
-\frac{\log\left(p_{2n}(e,e)/\rho_d^{2n}\right)}{n/\log^2 n}-C_d.
\]
Then \(\varepsilon(n)\to0\) and
\[
p_{2n}(e,e)=\rho_d^{2n}
\exp\left[-(C_d+\varepsilon(n))\frac{n}{\log^2 n}\right].
\]

**Proof:**
STEP3 gives
\[
\limsup_{n\to\infty}
\frac{-\log(p_{2n}(e,e)/\rho_d^{2n})}{n/\log^2 n}
\le
\pi^2(\log b)^2.
\tag{9.1}
\]
STEP8 gives
\[
\liminf_{n\to\infty}
\frac{-\log(p_{2n}(e,e)/\rho_d^{2n})}{n/\log^2 n}
\ge
\pi^2(\log b)^2.
\tag{9.2}
\]
Together (9.1)--(9.2) imply
\[
\frac{-\log(p_{2n}(e,e)/\rho_d^{2n})}{n/\log^2 n}
\to
\pi^2(\log b)^2.
\]
Since \(b=d-1\), this limit is \(C_d\). The displayed definition of \(\varepsilon(n)\) therefore satisfies \(\varepsilon(n)\to0\), and rearranging the definition gives
\[
p_{2n}(e,e)=\rho_d^{2n}
\exp\left[-(C_d+\varepsilon(n))\frac{n}{\log^2 n}\right].
\]
This proves STEP9.

**Dependencies:** STEP3, STEP8.

---

### GOAL: Main Result

**Claim:** Let $d\ge3$ be a fixed integer, and let $G=\mathbb Z_2\wr T_d$ be the lamplighter group on the $d$-regular tree $T_d$. Let $\mu$ be the switch-walk-switch measure on $G$. Determine the exact asymptotic of $\mu^{(2n)}(e)$ as $n\to\infty$ in the following sense: prove that there exists $C>0$ and function $\varepsilon(n)=o(1)$, we have
\[
p_{2n}(e,e)=\rho^{2n}_d\exp(-(C+\varepsilon(n))\frac{n}{\log^2n}).
\]
You may use the fact that the spectrum radius of the random walk on the lamplighter group is $$
\rho_d:=\frac{2\sqrt{d-1}}{d},
$$
without proving. In your proof, do not cite the paper ``The Anderson model on the Bethe lattice: Lifshitz Tails'' or any other unpublished work.

**Proof:**
STEP9 proves the required formula with the explicit constant
\[
C=C_d=\pi^2(\log(d-1))^2.
\]
Since \(d\ge3\), \(d-1>1\), so \(C>0\). The proof uses no unpublished work as a black box and does not cite the prohibited work. This proves the original problem.

**Dependencies:** STEP9.

## Key Ideas

The lower bound comes from forcing an open forward \(b\)-ary trap of depth \(r\). Its cost is \(\exp[-O(b^r)]\), while its top killed-walk eigenvalue is \(\rho_d\cos(\pi/(r+2))\). Choosing \(r\sim\log_b n\) gives the lower correction constant \(\pi^2(\log b)^2\).

The upper bound is spectral. STEP4 proves that any cluster with spectrum within \(\rho_d\delta\) of the edge must contain a dense ball of radius about \((\pi/\sqrt2)\delta^{-1/2}\). STEP5 shows such dense balls are double-exponentially rare in that radius. STEP6 converts this rarity into a spectral-tail bound by comparing von Neumann dimension with witness density. Finally STEP8 converts the double-exponential edge tail into the matching moment upper bound.

## Deviations from Decomposition Plan

STEP4 follows a different deterministic proof than the suggested Perron-vector localization and S3/S4 finite-tree comparison. Instead, it uses a rooted-shift representation of subtrees and a sharp contraction numerical-radius estimate derived from the Boas--Kac--Krein moment inequality. This was chosen because it proves exactly the dense-ball witness statement with the required \(\pi/\sqrt2\) threshold and handles finite and infinite connected subtrees uniformly.

No other substantive deviations. No computational checks were needed; all estimates are symbolic.
