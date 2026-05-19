# Proof

## Problem Statement

Let $P_t^x$ denote the law at time $t$ of the discrete-time switch-walk-switch walk on $\mathbb Z_2\wr\mathbb Z$, where each departure/arrival
lamp is resampled independently from $\mathrm{Bernoulli}(1/2)$ and the base move is simple symmetric on $\mathbb Z$. For $x=(\mathbf 0,0)$ and
$y=(\mathbf 0,2)$, determine the asymptotic behavior of $$\|P_t^x-P_t^y\|_{\mathrm{TV}}\sim t^{-1/2},$$
up to constants.

## Proof

Write \(S=(S_j)_{j\ge0}\) for the nearest-neighbor simple symmetric random walk on \(\mathbb Z\), and write \(\mathbb P_u\) for its law when \(S_0=u\). Put
\[
m_t=\min_{0\le j\le t}S_j,\qquad M_t=\max_{0\le j\le t}S_j,
\]
and
\[
p_t^u(a,b,z)=\mathbb P_u(m_t=a,M_t=b,S_t=z).
\]
Total variation is normalized as \(\|\alpha-\beta\|_{\mathrm{TV}}=\frac12\sum |\alpha-\beta|\). All random-walk estimates used below are proved in the text, so no external theorem is used as a black box.

### STEP1: Mixture Over The Base Range

**Claim:** For \(u\in\{0,2\}\), let \(\mu_t^u=P_t^{(\mathbf 0,u)}\). Let \(S\) be the simple symmetric random walk on \(\mathbb Z\) started at \(u\), and put
\[
m_t=\min_{0\le s\le t}S_s,\qquad M_t=\max_{0\le s\le t}S_s.
\]
For integers \(a\le z\le b\), let \(\Lambda_{a,b,z}\) be the probability measure on \(\mathbb Z_2\wr\mathbb Z\) which has base coordinate \(z\), independent \(\mathrm{Bernoulli}(1/2)\) lamps on every site of \([a,b]\cap\mathbb Z\), and lamp value \(0\) on every site outside \([a,b]\). Then, for every \(t\ge1\) and \(u\in\{0,2\}\),
\[
\mu_t^u=\sum_{\substack{a\le u\le b\\a\le z\le b}}
\mathbb P_u(m_t=a,M_t=b,S_t=z)\,\Lambda_{a,b,z}.
\]
Consequently, if \(G_t^u=\mathcal L_u(m_t,M_t,S_t)\), then for every \(t\ge1\),
\[
\|\mu_t^0-\mu_t^2\|_{\mathrm{TV}}\le \|G_t^0-G_t^2\|_{\mathrm{TV}}.
\]

**Proof:**
Fix \(t\ge1\), and condition on a base trajectory \((S_0,\ldots,S_t)\). A site \(v\) is resampled precisely at those steps for which \(v\) is a departure or arrival site. If \(v\notin R_t:=\{S_0,\ldots,S_t\}\), no resampling at \(v\) occurs and the final lamp remains the initial value \(0\). If \(v\in R_t\), then \(v\) is resampled at least once: if \(v=S_0\), it is resampled on departure at the first step; if \(v=S_j\) for some \(j\ge1\), it is resampled on arrival at time \(j\). Let \(\ell(v)\) be the last resampling time of \(v\). The final lamp at \(v\) is the Bernoulli variable sampled at time \(\ell(v)\). These last resampling variables are independent for distinct \(v\), because every departure and arrival resampling variable in the switch-walk-switch chain is independent. Thus, conditional on the base trajectory, the final lamps are independent fair bits on \(R_t\), and are zero outside \(R_t\).

A nearest-neighbor path on \(\mathbb Z\) visits every integer between its minimum and maximum, so
\[
R_t=[m_t,M_t]\cap\mathbb Z.
\]
Conditional on \((m_t,M_t,S_t)=(a,b,z)\), the lamplighter state has law \(\Lambda_{a,b,z}\). Summing over triples gives the displayed mixture identity.

Define the Markov kernel \(K\) from triples to lamplighter states by \(K((a,b,z),\cdot)=\Lambda_{a,b,z}\). The mixture identity says \(\mu_t^u=G_t^uK\). For probability measures \(\alpha,\beta\) on the triple space,
\[
\|\alpha K-\beta K\|_{\mathrm{TV}}
=\frac12\sum_x\left|\sum_w(\alpha(w)-\beta(w))K(w,x)\right|
\le \frac12\sum_w|\alpha(w)-\beta(w)|\sum_xK(w,x)
=\|\alpha-\beta\|_{\mathrm{TV}}.
\]
Taking \(\alpha=G_t^0\) and \(\beta=G_t^2\) proves the contraction bound.

**Dependencies:** Direct proof of the facts corresponding to S1, S2, and S4.

---

### STEP2: Base Projection Lower Bound

**Claim:** There exist constants \(c_{\mathrm{base}}>0\), \(C_{\mathrm{base}}<\infty\), and \(t_0\ge1\) such that for all \(t\ge t_0\),
\[
c_{\mathrm{base}}t^{-1/2}
\le
\|\mathcal L_0(S_t)-\mathcal L_2(S_t)\|_{\mathrm{TV}}
\le
C_{\mathrm{base}}t^{-1/2}.
\]
In particular, for all \(t\ge t_0\),
\[
\|\mu_t^0-\mu_t^2\|_{\mathrm{TV}}\ge c_{\mathrm{base}}t^{-1/2}.
\]

**Proof:**
Let \(q_t(k)=\mathbb P_0(S_t=k)\). On the parity class \(k\equiv t\pmod 2\), write \(k=2j-t\). Then
\[
q_t(2j-t)=2^{-t}\binom tj,\qquad 0\le j\le t.
\]
Let \(r_j=2^{-t}\binom tj\), and set \(r_{-1}=r_{t+1}=0\). The sequence \(r_0,\ldots,r_t\) is unimodal. Since \(\mathcal L_2(S_t)\) is the translate of \(\mathcal L_0(S_t)\) by \(2\),
\[
\|\mathcal L_0(S_t)-\mathcal L_2(S_t)\|_{\mathrm{TV}}
=\frac12\sum_{j=0}^{t+1}|r_j-r_{j-1}|.
\]
For a nonnegative unimodal sequence with zero endpoints, the sum of its positive increments is the maximum value, and the sum of the absolute values of its negative increments is also the maximum value. Hence
\[
\frac12\sum_{j=0}^{t+1}|r_j-r_{j-1}|=\max_{0\le j\le t}r_j.
\tag{2.1}
\]

It remains to bound the largest binomial mass. For \(t=2n\),
\[
\max_j r_j=2^{-2n}\binom{2n}{n}
=\prod_{k=1}^n\frac{2k-1}{2k}.
\]
For \(0<u\le1/2\), there is an absolute \(C_0\) such that
\[
-u-C_0u^2\le \log(1-u)\le -u.
\]
Applying this with \(u=1/(2k)\) gives
\[
\log\prod_{k=1}^n\frac{2k-1}{2k}
=-\frac12\sum_{k=1}^n\frac1k+O(1)
=-\frac12\log n+O(1).
\]
Thus \(2^{-2n}\binom{2n}{n}=\Theta(n^{-1/2})\). For \(t=2n+1\), the two central masses equal
\[
2^{-(2n+1)}\binom{2n+1}{n}
=\frac{2n+1}{2n+2}\,2^{-2n}\binom{2n}{n},
\]
so the same order holds. Combining this with (2.1) proves the two-sided endpoint estimate.

Finally, the base-coordinate projection \(\pi(f,z)=z\) sends \(\mu_t^0\) and \(\mu_t^2\) to \(\mathcal L_0(S_t)\) and \(\mathcal L_2(S_t)\), respectively. For any projection \(\pi\),
\[
\|\pi_\ast\alpha-\pi_\ast\beta\|_{\mathrm{TV}}
=\frac12\sum_y\left|\sum_{x:\pi(x)=y}(\alpha(x)-\beta(x))\right|
\le \|\alpha-\beta\|_{\mathrm{TV}}.
\]
This gives the lamplighter lower bound.

**Dependencies:** Direct proof of the facts corresponding to S2 and S3.

---

### STEP3: Non-Common Range Support

**Claim:** Let
\[
\mathcal C=\{(a,b,z)\in\mathbb Z^3:\ a\le0,\ b\ge2,\ a\le z\le b\}.
\]
There is a constant \(C_{\partial}<\infty\) such that for every \(t\ge1\),
\[
G_t^0(\mathcal C^c)+G_t^2(\mathcal C^c)
=
\mathbb P_0(M_t<2)+\mathbb P_2(m_t>0)
=
\mathbb P_0(\tau_2>t)+\mathbb P_0(\tau_{-2}>t)
\le C_{\partial}t^{-1/2}.
\]

**Proof:**
For a walk started at \(0\), \(m_t\le0\), so \((m_t,M_t,S_t)\notin\mathcal C\) exactly when \(M_t<2\). Since the walk is nearest-neighbor, \(M_t<2\) is the same event as \(\tau_2>t\). For a walk started at \(2\), \(M_t\ge2\), so \((m_t,M_t,S_t)\notin\mathcal C\) exactly when \(m_t>0\). Translating by \(-2\) gives
\[
\mathbb P_2(m_t>0)=\mathbb P_0(\tau_{-2}>t).
\]

We bound \(\mathbb P_0(\tau_2>t)\). Reflect every path from \(0\) to \(y<2\) that hits \(2\) at the first hitting time of \(2\). Reflection in the line \(2\) maps its endpoint \(y\) to \(4-y\), and this map is a bijection. Hence
\[
\mathbb P_0(M_t<2)
=\sum_{\substack{y<2\\y\equiv t\!\!\pmod2}}\bigl(q_t(y)-q_t(4-y)\bigr).
\]
If \(t\) is even, this telescopes, using symmetry \(q_t(-r)=q_t(r)\), to \(q_t(0)+q_t(2)\). If \(t\) is odd, it telescopes to \(q_t(-1)+q_t(1)=2q_t(1)\). STEP2 gives \(\sup_r q_t(r)\le Ct^{-1/2}\), and therefore
\[
\mathbb P_0(\tau_2>t)\le 2Ct^{-1/2}.
\]
The estimate for \(\mathbb P_0(\tau_{-2}>t)\) is the same by symmetry.

**Dependencies:** STEP2 and direct proof of the facts corresponding to S4.

---

### STEP4: Inclusion-Exclusion For Exact Range

**Claim:** For integers \(r\le s\), define the killed transition kernel
\[
K_t^{[r,s]}(u,z)=
\mathbb P_u\big(S_t=z,\ r\le S_j\le s\ \text{for every }0\le j\le t\big),
\]
with the convention \(K_t^{[r,s]}(u,z)=0\) if \(u\notin[r,s]\), \(z\notin[r,s]\), or \(r>s\). For
\[
p_t^u(a,b,z)=\mathbb P_u(m_t=a,M_t=b,S_t=z),
\]
one has, for every \(t\ge0\), every \(u\in\mathbb Z\), and every \(a\le z\le b\),
\[
p_t^u(a,b,z)
=
K_t^{[a,b]}(u,z)
-K_t^{[a+1,b]}(u,z)
-K_t^{[a,b-1]}(u,z)
+K_t^{[a+1,b-1]}(u,z).
\]

**Proof:**
Let
\[
E_{r,s}(z)=\{S_t=z,\ r\le S_j\le s\text{ for every }0\le j\le t\}.
\]
The event \(\{m_t=a,M_t=b,S_t=z\}\) is \(E_{a,b}(z)\) together with the requirement that the path visits both endpoints \(a\) and \(b\). Inside \(E_{a,b}(z)\), missing \(a\) is exactly \(E_{a+1,b}(z)\), missing \(b\) is exactly \(E_{a,b-1}(z)\), and missing both endpoints is exactly \(E_{a+1,b-1}(z)\). Inclusion-exclusion gives the formula. The zero convention covers boundary cases where a smaller interval no longer contains \(u\) or \(z\).

**Dependencies:** Direct proof of the range-as-interval fact corresponding to S4.

---

### STEP5: Translation To A Finite-Difference Problem

**Claim:** For \(L\ge2\), \(0\le i\le L\), and \(0\le x\le L\), define
\[
h_{t,L}(i,x)=
\mathbb P_i\!\left(\min_{0\le s\le t}S_s=0,\ \max_{0\le s\le t}S_s=L,\ S_t=x\right),
\]
and set \(h_{t,L}(i,x)=0\) if \(i\notin[0,L]\) or \(x\notin[0,L]\). For \(A<B\), set
\[
\mathcal K_t^{A,B}(u,x)=\mathbb P_u(S_t=x,\ A<S_j<B\ \text{for all }0\le j\le t),
\]
again with value \(0\) if \(u\) or \(x\) is not strictly between \(A\) and \(B\). With \(A=-1\), \(B=L+1\), and
\[
\Delta_A F(A,B)=F(A,B)-F(A+1,B),\quad
\Delta_B F(A,B)=F(A,B)-F(A,B-1),\quad
\Delta_i F(i)=F(i)-F(i+2),
\]
one has, for every \(t\ge0\), \(L\ge2\), \(0\le i\le L-2\), and \(0\le x\le L\),
\[
h_{t,L}(i,x)=\Delta_A\Delta_B\mathcal K_t^{A,B}(i,x),
\]
and
\[
h_{t,L}(i,x)-h_{t,L}(i+2,x)
=
\Delta_A\Delta_B\Delta_i\mathcal K_t^{A,B}(i,x).
\]
Moreover,
\[
\sum_{\substack{a\le0,\ b\ge2\\a\le z\le b}}
|p_t^0(a,b,z)-p_t^2(a,b,z)|
=
\sum_{L=2}^{\infty}\sum_{i=0}^{L-2}\sum_{x=0}^{L}
|h_{t,L}(i,x)-h_{t,L}(i+2,x)|.
\]

**Proof:**
For \(A=-1\) and \(B=L+1\), the event in \(\mathcal K_t^{A,B}\) is the event that the path stays in \([0,L]\). The term with \(A\) replaced by \(A+1=0\) is the event that the path stays in \([1,L]\), and the term with \(B\) replaced by \(B-1=L\) is the event that the path stays in \([0,L-1]\). Thus
\[
\Delta_A\Delta_B\mathcal K_t^{A,B}(i,x)
\]
is the probability that the path stays in \([0,L]\), ends at \(x\), and misses neither \(0\) nor \(L\). This is exactly \(h_{t,L}(i,x)\). Applying \(\Delta_i\) subtracts the same expression with starting point \(i+2\), giving the second displayed identity.

For the sum identity, use the bijection
\[
L=b-a,\qquad i=-a,\qquad x=z-a.
\]
The constraints \(a\le0\), \(b\ge2\), \(a\le z\le b\) become \(L\ge2\), \(0\le i\le L-2\), and \(0\le x\le L\). Translation invariance gives
\[
p_t^0(a,b,z)=h_{t,L}(i,x),\qquad
p_t^2(a,b,z)=h_{t,L}(i+2,x).
\]
Substituting these identities proves the claimed equality of sums.

**Dependencies:** STEP4.

---

### STEP6: Free Heat-Kernel Finite Differences

**Claim:** Let \(q_t(r)=\mathbb P_0(S_t=r)\), with \(q_t(r)=0\) on the wrong parity class. There exist constants \(C_m,c_m,J_m<\infty\), for \(m=0,1,2,3\), such that for all \(t\ge1\), all \(r\in\mathbb Z\), and all even integers \(\eta_1,\ldots,\eta_m\),
\[
\left|\nabla_{\eta_1}\cdots\nabla_{\eta_m}q_t(r)\right|
\le
C_m t^{-(m+1)/2}
\prod_{\ell=1}^{m}(1+|\eta_\ell|)
\left(1+\frac{|r|+\sum_{\ell=1}^{m}|\eta_\ell|}{\sqrt t}\right)^{J_m}
\exp\!\left[-c_m\frac{(|r|-\sum_{\ell=1}^{m}|\eta_\ell|)_+^2}{t}\right],
\]
where \(\nabla_{\eta}f(r)=f(r+\eta)-f(r)\), and the empty product for \(m=0\) equals \(1\).

**Proof:**
First prove the Gaussian bound
\[
q_t(r)\le C t^{-1/2}\exp(-cr^2/t).
\tag{6.1}
\]
If \(r\not\equiv t\pmod2\) or \(|r|>t\), this is immediate. Otherwise \(q_t(r)=2^{-t}\binom tn\), where \(n=(t+r)/2\). Let \(n_0\) be a mode of the binomial sequence, so \(n_0\in\{\lfloor t/2\rfloor,\lceil t/2\rceil\}\), and put \(d=|n-n_0|\). The central binomial estimate from STEP2 gives \(2^{-t}\binom t{n_0}\le Ct^{-1/2}\). If \(n\ge n_0\), then
\[
\frac{2^{-t}\binom tn}{2^{-t}\binom t{n_0}}
=\prod_{\ell=1}^{d}\frac{t-n_0-\ell+1}{n_0+\ell}
\le \prod_{\ell=1}^{d}\left(1-\frac{c\ell}{t}\right)
\le \exp\left[-\frac{c}{t}\sum_{\ell=1}^{d}\ell\right]
\le e^{-cd^2/t}
\]
as long as \(d\le t/4\); the case \(n\le n_0\) is identical by symmetry. If \(d>t/4\), applying the previous product estimate only for the first \(\lfloor t/4\rfloor\) factors gives \(e^{-ct}\), which is at most \(e^{-c'd^2/t}\) because \(d\le t\). Since \(d\asymp |r|\), (6.1) follows.

Let \(\delta f(r)=f(r+2)-f(r)\). For \(j=1,2,3\), direct binomial-ratio computations give, on the correct parity class and with \(q_t(r)=2^{-t}\binom t{(t+r)/2}\),
\[
\delta q_t(r)
=q_t(r)\frac{-2(r+1)}{t+r+2},
\tag{6.2}
\]
\[
\delta^2 q_t(r)
=q_t(r)\frac{4(r^2+4r-t+2)}{(t+r+2)(t+r+4)},
\tag{6.3}
\]
and
\[
\delta^3 q_t(r)
=q_t(r)\frac{-8(r+3)(r^2+6r-3t+2)}
{(t+r+2)(t+r+4)(t+r+6)}.
\tag{6.4}
\]
These formulas are obtained by writing \(q_t(r+2\ell)=q_t(r)R_\ell\), where
\[
R_\ell=\prod_{s=0}^{\ell-1}\frac{t-(t+r)/2-s}{(t+r)/2+s+1},
\]
and expanding \(\sum_{\ell=0}^j(-1)^{j-\ell}\binom j\ell R_\ell\).

If \(|r|\le t/2\), then the denominators in (6.2)-(6.4) are bounded below by constant multiples of \(t\). Combining those formulas with (6.1) gives, for \(j=0,1,2,3\),
\[
|\delta^j q_t(r)|
\le C_j t^{-(j+1)/2}
\left(1+\frac{|r|}{\sqrt t}\right)^{2j+2}
\exp(-c_jr^2/t).
\tag{6.5}
\]
If \(|r|>t/2\), then \(\delta^j q_t(r)\) is a signed sum of at most \(2^j\) terms \(q_t(r+2\ell)\), \(0\le\ell\le j\). For all \(t\) larger than a constant depending only on \(j\), these terms have \(|r+2\ell|\ge |r|/2\), and (6.1) gives an \(\exp(-c|r|^2/t)\) factor. Enlarging the polynomial exponent and the constant covers the remaining finite set of small \(t\). Thus (6.5) holds for all \(r\).

Now let \(\eta=2d\). If \(d>0\),
\[
\nabla_{\eta}f(r)=\sum_{s=0}^{d-1}\delta f(r+2s),
\]
and if \(d<0\), the analogous sum has \(|d|\) translated terms with the opposite sign. Iterating this identity for \(\eta_1,\ldots,\eta_m\), the expression \(\nabla_{\eta_1}\cdots\nabla_{\eta_m}q_t(r)\) is a sum of at most \(C_m\prod_{\ell=1}^m(1+|\eta_\ell|)\) terms of the form \(\delta^m q_t(r+\theta)\), with \(|\theta|\le\sum_\ell|\eta_\ell|\). Applying (6.5), using
\[
|r+\theta|\le |r|+\sum_\ell|\eta_\ell|,
\qquad
|r+\theta|\ge (|r|-\sum_\ell|\eta_\ell|)_+,
\]
and adjusting constants gives the claimed estimate.

**Dependencies:** STEP2 and direct proof of the facts corresponding to S3.

---

### STEP7: Long-Interval Reflection Estimate

**Claim:** There exist constants \(C_{\mathrm{long}},c_{\mathrm{long}},J_{\mathrm{long}}<\infty\) such that for every \(t\ge1\), every \(L\ge2\), every \(N=L+2\) satisfying \(N\ge\sqrt t\), every \(0\le i\le L-2\), and every \(0\le x\le L\),
\[
|h_{t,L}(i,x)-h_{t,L}(i+2,x)|
\le
C_{\mathrm{long}}t^{-2}
\left(1+\frac{N}{\sqrt t}\right)^{J_{\mathrm{long}}}
\exp\!\left[-c_{\mathrm{long}}\frac{N^2}{t}\right].
\]

**Proof:**
Let \(A=-1\), \(B=L+1\), and \(N=B-A=L+2\). The reflection image formula for the walk killed at \(A\) and \(B\) is
\[
\mathcal K_t^{A,B}(u,x)
=\sum_{k\in\mathbb Z}\left\{
q_t(x-u+2kN)-q_t(x+u-2A+2kN)
\right\}.
\tag{7.1}
\]
One way to verify (7.1) is to check that the right side has initial value \(\mathbf 1_{\{u=x\}}\) on \(A<x<B\), vanishes at \(x=A,B\), and satisfies the same discrete heat equation in the interior as the killed kernel; uniqueness follows by induction on \(t\). For fixed \(t\), only finitely many image terms are nonzero, since \(q_t(r)=0\) when \(|r|>t\), so the finite differences below may be applied term by term.

By STEP5,
\[
h_{t,L}(i,x)-h_{t,L}(i+2,x)=\Delta_A\Delta_B\Delta_i\mathcal K_t^{A,B}(i,x).
\]
Apply the three finite differences term by term in (7.1). For the first image family
\[
F_k=q_t(x-u+2kN),
\]
the start difference has mesh \(-2\), and each boundary difference changes \(N\) to \(N-1\), hence changes the argument by \(-2k\). Therefore \(\Delta_A\Delta_B\Delta_iF_k\) is, up to sign, a third finite difference of \(q_t\) with meshes \(-2,-2k,-2k\). For \(k=0\), both boundary meshes are zero, so this term is annihilated. For \(k\ne0\),
\[
|x-u+2kN|\ge (2|k|-1)N.
\tag{7.2}
\]

For the second image family
\[
H_k=q_t(x+u-2A+2kN),
\]
the start difference has mesh \(2\), the \(A\)-difference has mesh \(-2(k+1)\), and the \(B\)-difference has mesh \(-2k\). The \(k=0\) term is killed by the \(B\)-difference, and the \(k=-1\) term is killed by the \(A\)-difference. For \(k\notin\{0,-1\}\), writing \(y=x-A\) and \(v=u-A\), with \(1\le y,v\le N-1\), gives
\[
|y+v+2kN|\ge c_0(|k|+1)N
\tag{7.3}
\]
for an absolute \(c_0>0\), after reducing \(c_0\) to cover all \(k\notin\{0,-1\}\).

There are only finitely many cases with \(N<N_0\), and then \(t\le N^2<N_0^2\); enlarging the final constant covers them. Assume \(N\ge N_0\), with \(N_0\) large enough that the mesh sums in STEP6 are at most half the lower bounds in (7.2) and (7.3). STEP6 with \(m=3\) gives, for the surviving first-family terms,
\[
|\Delta_A\Delta_B\Delta_iF_k|
\le
C t^{-2}(1+|k|)^J
\left(1+\frac{|k|N}{\sqrt t}\right)^J
\exp\!\left[-c\frac{k^2N^2}{t}\right],
\]
and the same bound, with \(|k|+1\) in place of \(|k|\), for the surviving second-family terms. Since \(N/\sqrt t\ge1\),
\[
\sum_{k\in\mathbb Z}(1+|k|)^J
\left(1+\frac{(|k|+1)N}{\sqrt t}\right)^J
\exp\!\left[-c\frac{(|k|+1)^2N^2}{t}\right]
\le
C\left(1+\frac N{\sqrt t}\right)^{J'}
\exp\!\left[-c'\frac{N^2}{t}\right].
\]
Summing the image bounds proves the claimed estimate.

**Dependencies:** STEP5 and STEP6.

---

### STEP8: Spectral Representation For The Killed Kernel

**Claim:** For \(A<B\), \(N=B-A\ge2\), and \(A<u,x<B\), the killed kernel has the exact signed spectral representation
\[
\mathcal K_t^{A,B}(u,x)=
\frac{2}{N}\sum_{n=1}^{N-1}
\left(\cos\frac{\pi n}{N}\right)^t
\sin\frac{\pi n(u-A)}{N}\,
\sin\frac{\pi n(x-A)}{N}.
\]
If \(m(n,N)=\min\{n,N-n\}\), then for some absolute \(c>0\),
\[
\left|\cos\frac{\pi n}{N}\right|^t
\le \exp\!\left[-c\,t\,m(n,N)^2/N^2\right].
\]
Furthermore, for \(1\le m<N/2\),
\[
\left(\cos\frac{\pi(N-m)}{N}\right)^t=(-1)^t\left(\cos\frac{\pi m}{N}\right)^t
\]
and, for every integer \(r\),
\[
\sin\frac{\pi(N-m)r}{N}=(-1)^{r+1}\sin\frac{\pi mr}{N}.
\]

**Proof:**
Translate so that \(A=0\). On the state space \(\{1,\ldots,N-1\}\), the killed transition matrix is
\[
Pf(j)=\frac12f(j-1)+\frac12f(j+1),
\]
with boundary values \(f(0)=f(N)=0\). For \(1\le n\le N-1\), the vector
\[
\varphi_n(j)=\sin(\pi n j/N)
\]
satisfies
\[
P\varphi_n(j)=\cos(\pi n/N)\varphi_n(j).
\]
The sine orthogonality relation
\[
\sum_{j=1}^{N-1}\sin(\pi n j/N)\sin(\pi m j/N)=\frac N2\,\mathbf 1_{\{m=n\}}
\]
gives the displayed spectral expansion of \(P^t\).

For \(0\le\theta\le\pi\), \(|\cos\theta|\le \exp[-c\,\operatorname{dist}(\theta,\pi\mathbb Z)^2]\) for a universal \(c>0\); this follows by compactness after checking the quadratic behavior at \(0\) and \(\pi\). Taking \(\theta=\pi n/N\) gives the exponential bound. The two sign identities follow from
\[
\cos(\pi-\theta)=-\cos\theta
\]
and
\[
\sin(\pi r-\theta r)=(-1)^{r+1}\sin(\theta r)
\]
for integer \(r\).

**Dependencies:** Direct proof of the facts corresponding to S3 and S4.

---

### STEP9: Paired-Mode Mixed Finite Difference ⭐ KEY STEP

**Claim:** For \(A<B\), \(N=B-A\ge4\), \(0\le \alpha,\beta\le1\) with \(\alpha+\beta\le2\), and \(1\le m\le\lfloor N/2\rfloor\), write \(N_{\alpha,\beta}=N-\alpha-\beta\). Define \(\Theta_{m,t}^{A+\alpha,B-\beta}(u,x)\) to be the sum of the two spectral terms of \(\mathcal K_t^{A+\alpha,B-\beta}(u,x)\) whose frequencies are \(m\) and \(N_{\alpha,\beta}-m\) when \(2m<N_{\alpha,\beta}\), and define \(\Theta_{m,t}^{A+\alpha,B-\beta}(u,x)=0\) when \(2m\ge N_{\alpha,\beta}\). Then there exist constants \(C_{\mathrm{mode}},c_{\mathrm{mode}}<\infty\) such that for every \(t\ge1\), every \(N\le\sqrt t\), every \(A+1\le u\le B-3\), and every \(A+1\le x\le B-1\),
\[
\left|
\Delta_A\Delta_B\Delta_u\Theta_{m,t}^{A,B}(u,x)
\right|
\le
C_{\mathrm{mode}}N^{-4}
\left(1+\frac{t m^2}{N^2}\right)^3
\exp\!\left[-c_{\mathrm{mode}}\frac{t m^2}{N^2}\right],
\]
where \(\Delta_A,\Delta_B\) are the boundary differences from STEP5 and \(\Delta_uF(u)=F(u)-F(u+2)\), applied to the zero-extended paired-mode quantities with denominators \(N\), \(N-1\), and \(N-2\).

**Proof:**
<key-original-step>
Set \(r=u-A\) and \(y=x-A\). Thus \(1\le r\le N-3\) and \(1\le y\le N-1\). For boundary shifts \(\alpha,\beta\in\{0,1\}\), put
\[
s=N-\alpha-\beta,\qquad r_\alpha=r-\alpha,\qquad y_\alpha=y-\alpha.
\]
Assume first that \(2m<N-2\). Then \(2m<s\) for every denominator \(s\in\{N,N-1,N-2\}\) that appears in the mixed boundary difference. By STEP8, the paired mode at denominator \(s\) equals
\[
\Theta_{m,t}^{A+\alpha,B-\beta}(u,x)
=\frac{2}{s}\left(\cos\frac{\pi m}{s}\right)^t
\sin\frac{\pi m r_\alpha}{s}\sin\frac{\pi m y_\alpha}{s}
\;+\;
\frac{2}{s}\left(\cos\frac{\pi(s-m)}{s}\right)^t
\sin\frac{\pi(s-m)r_\alpha}{s}\sin\frac{\pi(s-m)y_\alpha}{s}.
\]
Using the sign identities from STEP8, the second term is
\[
\frac{2}{s}(-1)^t\left(\cos\frac{\pi m}{s}\right)^t
(-1)^{r_\alpha+1}(-1)^{y_\alpha+1}
\sin\frac{\pi m r_\alpha}{s}\sin\frac{\pi m y_\alpha}{s}.
\]
Since \(r_\alpha+y_\alpha=r+y-2\alpha\), the parity factor is independent of \(\alpha\), and it is also unchanged when \(u\) is replaced by \(u+2\). Therefore
\[
\Theta_{m,t}^{A+\alpha,B-\beta}(u,x)
=\chi\,
\phi(s,r_\alpha,y_\alpha),
\tag{9.1}
\]
where \(\chi=1+(-1)^{t+r+y}\), so \(|\chi|\le2\), and
\[
\phi(s,p,q)=\frac{2}{s}\left(\cos\frac{\pi m}{s}\right)^t
\sin\frac{\pi m p}{s}\sin\frac{\pi m q}{s}.
\tag{9.2}
\]
This is the point at which the signed high-frequency term is used: before taking absolute values, the high-frequency mode has been combined with the low-frequency mode into the single parity factor \(\chi\).

The boundary and start differences in (9.1) are finite differences of \(\phi\) in the three variables \((s,p,q)\). The \(A\)-difference changes \((s,p,q)\) by
\[
v_A=(-1,-1,-1),
\]
the \(B\)-difference changes it by
\[
v_B=(-1,0,0),
\]
and the \(u\)-difference changes it by
\[
v_u=(0,2,0).
\]
For a \(C^3\) function, the iterated finite difference along fixed vectors is an integral of the corresponding third directional derivative over the unit cube. Hence
\[
\left|\Delta_A\Delta_B\Delta_u\Theta_{m,t}^{A,B}(u,x)\right|
\le
C\sup |D_{v_A}D_{v_B}D_{v_u}\phi(s,p,q)|,
\tag{9.3}
\]
where the supremum is over \(s\in[N-2,N]\), \(p\in[r-1,r+2]\), and \(q\in[y-1,y]\). These \(p,q\) are bounded in absolute value by \(N+2\).

We now bound the derivatives of \(\phi\). Put
\[
\tau_s=\frac{tm^2}{s^2}.
\]
Because \(N\le\sqrt t\) and \(s\in[N-2,N]\), after changing constants \(\tau_s\) is comparable to \(tm^2/N^2\), and \(s\) is comparable to \(N\).

First,
\[
a(s)=\frac2s\left(\cos\frac{\pi m}{s}\right)^t
\]
satisfies, for \(0\le j\le3\),
\[
|a^{(j)}(s)|
\le
C_j s^{-1-j}(1+\tau_s)^j e^{-c\tau_s}.
\tag{9.4}
\]
Indeed, if \(m/s\le1/3\), then \(\tan(\pi m/s)\le C m/s\), and differentiating
\[
t\log\cos(\pi m/s)
\]
shows that its \(j\)-th \(s\)-derivative is bounded by \(C_j\tau_s/s^j\) for \(1\le j\le3\). Applying the product and chain rules to \(s^{-1}\exp(t\log\cos(\pi m/s))\) gives (9.4). If \(m/s>1/3\), then \(|\cos(\pi m/s)|\le\rho<1\). Every \(j\)-th derivative, \(j\le3\), of \((\cos(\pi m/s))^t\) is a sum of at most \(C_j\) terms bounded by
\[
C_j s^{-j}t^j\rho^{\,t-j}.
\]
Since \(m/s>1/3\), \(\tau_s\asymp t\), so this is bounded by the right side of (9.4) after decreasing \(c\).

Second, for \(b(s,p)=\sin(\pi m p/s)\), every mixed derivative of total order \(d\le3\) satisfies
\[
|\partial_s^\ell\partial_p^{d-\ell} b(s,p)|
\le C_d\left(\frac{1+\tau_s}{s}\right)^d,
\qquad 0\le \ell\le d.
\tag{9.5}
\]
For \(p\le N+2\) and \(s\asymp N\), each derivative of the argument \(\pi mp/s\) of positive order is bounded by \(C m/s\) times the appropriate power of \(s^{-1}\); since \(t\ge N^2\), we have \(\tau_s\ge c m^2\), and therefore \(m/s\le C(1+\tau_s)/s\). The chain rule gives (9.5).

Combining (9.4) and (9.5) with the product rule for \(\phi=a(s)b(s,p)b(s,q)\), every third partial derivative of \(\phi\) is bounded by
\[
C N^{-1}\left(\frac{1+tm^2/N^2}{N}\right)^3
\exp\!\left[-c\frac{tm^2}{N^2}\right].
\tag{9.6}
\]
Directional derivatives along \(v_A,v_B,v_u\) are linear combinations of third partial derivatives with bounded coefficients. Equations (9.3) and (9.6) prove the desired estimate in the case \(2m<N-2\).

It remains to handle the threshold case \(2m\ge N-2\). Then \(m\ge (N-2)/2\). For each denominator \(s\in\{N,N-1,N-2\}\), either the paired mode is zero by definition, or \(m/s\ge1/4\). In the nonzero case, \(|\cos(\pi m/s)|\le\rho<1\), and therefore a single paired-mode value is bounded by \(C N^{-1}e^{-ct}\). The mixed difference contains only finitely many such values, so its absolute value is at most \(C N^{-1}e^{-ct}\). Since \(t\ge N^2\) and \(m^2/N^2\ge c_0>0\), choosing \(c_{\mathrm{mode}}\) small enough gives
\[
C N^{-1}e^{-ct}
\le
C' N^{-4}\left(1+\frac{tm^2}{N^2}\right)^3
\exp\!\left[-c_{\mathrm{mode}}\frac{tm^2}{N^2}\right].
\]
This proves the estimate in all cases.
</key-original-step><heuristics>The key point is that the dangerous signed high-frequency eigenvalue is not estimated separately. It is paired with the corresponding low-frequency eigenvalue first, and the pair collapses to a fixed parity factor times one smooth low-frequency expression. Boundary changes only alter the denominator and the two sine coordinates by one, while the start shift alters one sine coordinate by two. Thus the mixed difference is a third directional finite difference of a smooth function. Each derivative costs one factor \(N^{-1}(1+tm^2/N^2)\), and the eigenvalue contributes the damping \(\exp[-c tm^2/N^2]\). Modes near the middle of the spectrum are already exponentially small because \(N\le\sqrt t\).</heuristics>

**Dependencies:** STEP5 and STEP8.

---

### STEP10: Short-Interval Pointwise Bound

**Claim:** There exist constants \(C_{\mathrm{short}},c_{\mathrm{short}}<\infty\) such that for every \(t\ge1\), every \(L\ge2\), every \(N=L+2\) satisfying \(N\le\sqrt t\), every \(0\le i\le L-2\), and every \(0\le x\le L\),
\[
|h_{t,L}(i,x)-h_{t,L}(i+2,x)|
\le
C_{\mathrm{short}}N^{-4}\exp\!\left[-c_{\mathrm{short}}\frac{t}{N^2}\right].
\]

**Proof:**
Let \(A=-1\), \(B=L+1\), so \(N=B-A=L+2\). By STEP5,
\[
h_{t,L}(i,x)-h_{t,L}(i+2,x)=\Delta_A\Delta_B\Delta_i\mathcal K_t^{A,B}(i,x).
\]
Use the spectral expansion from STEP8 for each of the denominators \(N,N-1,N-2\) appearing in \(\Delta_A\Delta_B\). Pair the frequency \(m\) with \(N'-m\) for each denominator \(N'\), and use the zero extension from STEP9 when a pair is absent. The central frequency \(m=N'/2\), if it exists, has eigenvalue \(0\) for \(t\ge1\), so it contributes nothing. Therefore the mixed difference is the sum over \(1\le m\le\lfloor N/2\rfloor\) of the mixed differences of paired modes.

STEP9 gives
\[
|h_{t,L}(i,x)-h_{t,L}(i+2,x)|
\le
C N^{-4}
\sum_{m=1}^{\lfloor N/2\rfloor}
\left(1+\frac{tm^2}{N^2}\right)^3
\exp\!\left[-c\frac{tm^2}{N^2}\right].
\]
Since \(N\le\sqrt t\), \(a=t/N^2\ge1\). For \(m\ge1\),
\[
(1+am^2)^3e^{-cam^2}\le C e^{-c'a}e^{-c''a(m^2-1)}(1+m)^6,
\]
and the last factor is summable uniformly in \(a\ge1\). Hence
\[
\sum_{m=1}^{\infty}(1+am^2)^3e^{-cam^2}\le C e^{-c'a}.
\]
This proves the claimed short-interval estimate.

**Dependencies:** STEP5, STEP8, and STEP9.

---

### STEP11: Common-Support Summation

**Claim:** There is a constant \(C_{\mathrm{int}}<\infty\) such that for every \(t\ge1\),
\[
\frac12
\sum_{\substack{a\le0,\ b\ge2\\ a\le z\le b}}
\left|
p_t^0(a,b,z)-p_t^2(a,b,z)
\right|
\le C_{\mathrm{int}}t^{-1/2}.
\]

**Proof:**
By STEP5, the sum is
\[
\frac12\sum_{L=2}^\infty\sum_{i=0}^{L-2}\sum_{x=0}^L
|h_{t,L}(i,x)-h_{t,L}(i+2,x)|.
\]
Put \(N=L+2\). For fixed \(N\), the number of pairs \((i,x)\) is at most \(N^2\).

For \(N\le\sqrt t\), STEP10 gives a contribution bounded by
\[
C\sum_{2\le N\le\sqrt t}N^2\cdot N^{-4}e^{-ct/N^2}
=C\sum_{2\le N\le\sqrt t}N^{-2}e^{-ct/N^2}.
\]
With \(r=N/\sqrt t\), this Riemann sum is bounded by
\[
C t^{-1/2}\int_0^1 r^{-2}e^{-c/r^2}\,dr
\le C't^{-1/2}.
\tag{11.1}
\]

For \(N\ge\sqrt t\), STEP7 gives a contribution bounded by
\[
C\sum_{N\ge\sqrt t}
N^2 t^{-2}
\left(1+\frac N{\sqrt t}\right)^J
e^{-cN^2/t}.
\]
Again setting \(r=N/\sqrt t\), the sum is bounded by
\[
C t^{-1/2}\int_1^\infty r^2(1+r)^J e^{-cr^2}\,dr
\le C't^{-1/2}.
\tag{11.2}
\]
Combining (11.1) and (11.2) proves the claim.

**Dependencies:** STEP5, STEP7, and STEP10.

---

### STEP12: Range-Endpoint Total Variation Bound

**Claim:** There is a constant \(C_{\mathrm{range}}<\infty\) such that for every \(t\ge1\),
\[
\|G_t^0-G_t^2\|_{\mathrm{TV}}\le C_{\mathrm{range}}t^{-1/2}.
\]
More explicitly, one may take \(C_{\mathrm{range}}=C_{\mathrm{int}}+C_{\partial}\).

**Proof:**
Let
\[
\mathcal C=\{(a,b,z):a\le0,\ b\ge2,\ a\le z\le b\}.
\]
Then
\[
\|G_t^0-G_t^2\|_{\mathrm{TV}}
\le
\frac12\sum_{(a,b,z)\in\mathcal C}|p_t^0(a,b,z)-p_t^2(a,b,z)|
+\frac12\bigl(G_t^0(\mathcal C^c)+G_t^2(\mathcal C^c)\bigr).
\]
STEP11 bounds the first term by \(C_{\mathrm{int}}t^{-1/2}\), and STEP3 bounds the second term by \((C_{\partial}/2)t^{-1/2}\). Enlarging constants gives the stated bound; in particular \(C_{\mathrm{range}}=C_{\mathrm{int}}+C_{\partial}\) is valid.

**Dependencies:** STEP3 and STEP11.

---

### STEP13: Lamplighter Upper Bound

**Claim:** There is a constant \(C_{\mathrm{up}}<\infty\) such that for every \(t\ge1\),
\[
\|P_t^{(\mathbf 0,0)}-P_t^{(\mathbf 0,2)}\|_{\mathrm{TV}}
=
\|\mu_t^0-\mu_t^2\|_{\mathrm{TV}}
\le C_{\mathrm{up}}t^{-1/2}.
\]

**Proof:**
By STEP1,
\[
\|\mu_t^0-\mu_t^2\|_{\mathrm{TV}}
\le \|G_t^0-G_t^2\|_{\mathrm{TV}}.
\]
STEP12 bounds the right side by \(C_{\mathrm{range}}t^{-1/2}\). Take \(C_{\mathrm{up}}=C_{\mathrm{range}}\).

**Dependencies:** STEP1 and STEP12.

---

### GOAL: Main Result

**Claim:** Let $P_t^x$ denote the law at time $t$ of the discrete-time switch-walk-switch walk on $\mathbb Z_2\wr\mathbb Z$, where each departure/arrival
lamp is resampled independently from $\mathrm{Bernoulli}(1/2)$ and the base move is simple symmetric on $\mathbb Z$. For $x=(\mathbf 0,0)$ and
$y=(\mathbf 0,2)$, determine the asymptotic behavior of $$\|P_t^x-P_t^y\|_{\mathrm{TV}}\sim t^{-1/2},$$
up to constants.

**Proof:**
Let \(x=(\mathbf0,0)\) and \(y=(\mathbf0,2)\). STEP2 gives constants \(c>0\) and \(t_0\) such that
\[
\|P_t^x-P_t^y\|_{\mathrm{TV}}\ge c t^{-1/2}\qquad(t\ge t_0).
\]
STEP13 gives a constant \(C<\infty\) such that
\[
\|P_t^x-P_t^y\|_{\mathrm{TV}}\le C t^{-1/2}\qquad(t\ge1).
\]
Therefore
\[
\|P_t^x-P_t^y\|_{\mathrm{TV}}=\Theta(t^{-1/2})
\]
as \(t\to\infty\), which is the requested asymptotic behavior up to constants.

**Dependencies:** STEP2 and STEP13.

## Key Ideas

The switch-walk-switch resampling makes the lamp configuration, conditional on the base path, equal to independent fair bits on the base range and zeros outside. In one dimension the range is an interval, so the lamplighter comparison reduces to comparing the law of \((m_t,M_t,S_t)\) for base walks started at \(0\) and \(2\). The lower bound is already visible from the base endpoint. The upper bound is obtained by proving that the range-endpoint law changes by only \(O(t^{-1/2})\) under the fixed shift: long intervals are controlled by reflection images and finite differences of the free heat kernel, while short intervals are controlled by the signed spectral expansion of the killed walk, with low and high modes paired before taking absolute values.

## Deviations from Decomposition Plan

None in substance -- followed the revised decomposition plan. The planned literature inputs S1-S4 were proved directly in the relevant steps rather than cited as external black boxes.