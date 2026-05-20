# Proof

## Problem Statement

Consider the advection diffusion equation in $\mathbb{T}^2$:
\begin{equation}\label{nonshear}
    \partial_t \rho + u(At,x,y)\cdot\nabla \rho = \Delta \rho,\quad \rho(0,x,y)=\rho_0(x,y).
\end{equation}
Assume that $0\neq \rho(0,\cdot)=\rho_0(x,y) \in L^2_{x,y}$ is mean-zero, $A>0$ and that 
\[
\|u(t,x,y)\|_{L^{\infty}_t W^{1,\infty}_{x,y}} < \infty.
\]
Moreover, we have $\nabla\cdot u=0$. Then we have the unique weak solution $\rho$. Let us assume in addition, $u(t,x,y)$ is periodic in $t$, with period $L$, or $u(t,x,y)=u(t+L,x,y)$.
\begin{problem}
Prove or disprove that, given $\rho_0(x,y)$ and $u(t,x,y)$, there exists $A_0>0$ depending on $\rho(0,\cdot)$ and $u$, so that if $A>A_0$ (which means, the period of the velocity will be $L/A$), there exists $c_0>0$ and $C>0$, depending on $\rho_0$, $u$ and $A$, the solution to \eqref{nonshear} satisfies:
\[
\|\rho(t)\|_{L^2_{x,y}}\geq C e^{-c_0 t}
\]
for all $t\geq 0$. In contrast, for slowly varying or autonomous flows it is known that the $L^2$ norm can decay double-exponentially (Keefer Rowan. Superexponential dissipation enhancement on Td. arXiv preprint arXiv:2509.02081, 2025.); the question is whether fast time-periodic oscillation restores a single exponential lower bound.
\end{problem}

## Proof

We prove the assertion. All Hilbert spaces are complexified; the real-valued conclusion follows by applying the same estimate to the complexification of the real solution. Pairings with adjoint observables use the bilinear pairing
\[
\langle f,g\rangle=\int_{\mathbb T^2} f(x)g(x)\,dx,
\]
while $\|\cdot\|_2$ denotes the usual Hilbert $L^2$ norm.

### STEP1: Basic evolution, energy, periodicity, non-extinction, and duality

**Claim:** Fix $A>0$, set $T_A=L/A$, and write
\[
b_A(t,x)=u(At,x),\qquad H=L^2_0(\mathbb T^2).
\]
Let $U_A(t,s):H\to H$ be the weak solution operator for
\[
\partial_t\rho=\Delta\rho-b_A(t,\cdot)\cdot\nabla\rho .
\]
Then for every $0\leq s\leq t$ and every $f\in H$,
\[
\int_{\mathbb T^2}U_A(t,s)f\,dxdy=0,
\]
\[
\frac12\frac{d}{dt}\|U_A(t,s)f\|_2^2+\|\nabla U_A(t,s)f\|_2^2=0
\]
in the distributional sense on $(s,\infty)$, and hence
\[
\|U_A(t,s)f\|_2\leq \|f\|_2 .
\]
Moreover
\[
U_A(t+T_A,s+T_A)=U_A(t,s),
\]
and if $0\ne f\in H$, then
\[
\|U_A(t,s)f\|_2>0\qquad\text{for every }t\ge s.
\]
Finally, if $\psi$ satisfies the backward adjoint equation
\[
-\partial_t\psi=\Delta\psi+b_A(t,\cdot)\cdot\nabla\psi
\]
on $[s,t]$, then
\[
\langle U_A(r,s)f,\psi(r)\rangle_{L^2(\mathbb T^2)}
=
\langle f,\psi(s)\rangle_{L^2(\mathbb T^2)}
\]
for every $r\in[s,t]$.

**Proof:**
For smooth data, integrating the equation over $\mathbb T^2$ gives
\[
\frac{d}{dt}\int_{\mathbb T^2}\rho(t,x)\,dx
=\int_{\mathbb T^2}\Delta\rho\,dx-\int_{\mathbb T^2}b_A\cdot\nabla\rho\,dx.
\]
The first integral is zero by periodicity. The second is zero because
\[
\int_{\mathbb T^2}b_A\cdot\nabla\rho\,dx
=\int_{\mathbb T^2}\nabla\cdot(b_A\rho)\,dx-\int_{\mathbb T^2}(\nabla\cdot b_A)\rho\,dx=0.
\]
Hence the mean is preserved.

Multiplying the equation by $\rho$ and integrating yields
\[
\frac12\frac{d}{dt}\|\rho(t)\|_2^2
=\int_{\mathbb T^2}\rho\Delta\rho\,dx-\int_{\mathbb T^2}\rho\,b_A\cdot\nabla\rho\,dx.
\]
The diffusion term is $-\|\nabla\rho(t)\|_2^2$. The transport term vanishes since
\[
\int_{\mathbb T^2}\rho\,b_A\cdot\nabla\rho\,dx
=\frac12\int_{\mathbb T^2}b_A\cdot\nabla(\rho^2)\,dx
=\frac12\int_{\mathbb T^2}\nabla\cdot(b_A\rho^2)\,dx
-\frac12\int_{\mathbb T^2}(\nabla\cdot b_A)\rho^2\,dx=0.
\]
Thus
\[
\frac12\frac{d}{dt}\|\rho(t)\|_2^2+\|\nabla\rho(t)\|_2^2=0.
\]
This is the usual incompressible advection-diffusion energy law:
<cite>type=identity; label=Seis-energy-balance; title=Bounds on the Rate of Enhanced Dissipation; authors=Christian Seis; source_url=https://doi.org/10.1007/s00220-022-04588-3; verifier_locator=p. 2072, equation (2); statement_match=exact; statement=It is a well-known fact that the advection field has no impact on the \(L^2\) energy balance law, $$\begin{aligned} \frac{1}{2} \frac{\textrm{d}}{\textrm{d}t}\Vert \theta ^{\kappa }\Vert ^2_{L^2} + \kappa \Vert \nabla \theta ^{\kappa }\Vert _{L^2}^2 = 0. \end{aligned}$$; usage=Used as a reference for the energy identity; the identity is also derived directly above for the present divergence-free equation with \(\kappa=1\).</cite>
For weak $L^2$ data, approximate the datum by smooth mean-zero data, use the uniform bounds in
\[
L^\infty_{\rm loc}([s,\infty);L^2)\cap L^2_{\rm loc}([s,\infty);H^1),
\]
pass to a weak limit in the equation, and pass to the integrated energy identity by lower semicontinuity and the usual equality recovery obtained from testing the weak equation by time mollifications of the solution. The contraction estimate follows by integrating the identity from $s$ to $t$.

The time-periodicity follows from
\[
b_A(t+T_A,\cdot)=u(At+L,\cdot)=u(At,\cdot)=b_A(t,\cdot).
\]
The shifted solution $r\mapsto U_A(r+T_A,s+T_A)f$ and the unshifted solution $r\mapsto U_A(r,s)f$ solve the same Cauchy problem; uniqueness gives
\[
U_A(t+T_A,s+T_A)=U_A(t,s).
\]

Suppose $U_A(t_1,s)f=0$ for some $t_1>s$. Forward uniqueness gives $U_A(t,s)f=0$ for all $t\ge t_1$. Choose $\varepsilon\in(0,t_1-s)$ and choose any interior time $t_2>t_1$. Parabolic smoothing gives boundedness of the solution and of its spatial gradient on compact subcylinders of $\mathbb T^2\times(s+\varepsilon,\infty)$. Since the solution vanishes on an open neighborhood of every point $(x,t_2)$, it vanishes to infinite order there. Poon's unique-continuation theorem applies locally:
<cite>type=theorem; label=Poon-unique-continuation; title=Unique continuation for parabolic equations; authors=Chi-Cheung Poon; source_url=https://www.osti.gov/biblio/441145; verifier_locator=OSTI bibliographic record, description field for Theorem 1.1; statement_match=exact; statement=Suppose that both u and {triangledown}u are uniformly bounded. If u vanishes of infinite order in space-time at any point in R{sup n} X (0,{infinity}), then u is identically zero.; usage=Applied locally after positive-time smoothing to rule out extinction of a nonzero positive-time advection-diffusion solution.</cite>
Thus the solution is identically zero on $\mathbb T^2\times(s+\varepsilon,\infty)$. Letting $\varepsilon\downarrow0$ and using strong $L^2$ continuity at $s$ gives $f=0$, a contradiction. Therefore nonzero data cannot have zero $L^2$ norm at a later time.

For smooth $\rho$ and $\psi$ satisfying the forward equation and the displayed backward adjoint equation,
\[
\frac{d}{dr}\langle \rho(r),\psi(r)\rangle
=\langle \Delta\rho-b_A\cdot\nabla\rho,\psi\rangle
+\langle \rho,-\Delta\psi-b_A\cdot\nabla\psi\rangle.
\]
The Laplacian terms cancel by integration by parts, and the transport terms equal
\[
-\int_{\mathbb T^2}b_A\cdot\nabla(\rho\psi)\,dx=0.
\]
The pairing is constant. The weak identity follows by the same approximation argument used above.

**Dependencies:** S1, S2.

---

### STEP2: Autonomous adjoint finite root chain detecting the datum ⭐ KEY STEP

**Claim:** Define the time-averaged divergence-free drift
\[
\bar u(x)=\frac1L\int_0^L u(s,x)\,ds
\]
and the autonomous averaged operators on $H=L^2_0(\mathbb T^2)$
\[
B=\Delta-\bar u\cdot\nabla,\qquad B^*=\Delta+\bar u\cdot\nabla .
\]
For the prescribed datum $0\ne\rho_0\in H$, there exist an integer $d\ge1$, mean-zero functions
\[
\Phi_0=(\phi_1,\dots,\phi_d)\in (H^2(\mathbb T^2)\cap H)^d,
\]
and a matrix $G_0\in\mathbb C^{d\times d}$ such that
\[
B^*\Phi_0=\Phi_0G_0
\]
columnwise and
\[
q_0:=
\left(\langle\rho_0,\phi_1\rangle,\dots,
\langle\rho_0,\phi_d\rangle\right)\in\mathbb C^d
\]
satisfies
\[
\|q_0\|_{\mathbb C^d}>0.
\]
In addition,
\[
K_0:=\left(\sum_{j=1}^d\|\phi_j\|_2^2\right)^{1/2}<\infty,
\qquad
g_0:=\|G_0\|_{\mathbb C^d\to\mathbb C^d}<\infty .
\]

**Proof:**
<key-original-step>
We first prove completeness of the generalized root spaces of $B^*$ in $H$.

Choose $\lambda>0$. For smooth mean-zero $f$,
\[
\operatorname{Re}\langle(\lambda-B^*)f,f\rangle_{\rm Herm}
=\lambda\|f\|_2^2+\|\nabla f\|_2^2,
\]
because $\bar u$ is divergence-free and $\bar u\cdot\nabla$ is skew-symmetric in the Hermitian $L^2$ pairing. The coercive form gives the invertibility of
\[
\lambda-B^*:H^2(\mathbb T^2)\cap H\to H
\]
for $\lambda$ large enough, and elliptic regularity gives the displayed domain.

Let
\[
R=(\lambda-B^*)^{-1},\qquad R_0=(\lambda-\Delta)^{-1}
\]
on $H$. The heat resolvent $R_0$ is compact, self-adjoint, injective, and of finite order; in the Fourier basis its eigenvalues are $(\lambda+\mu_k)^{-1}$, where $\mu_k$ are the positive eigenvalues of $-\Delta$ on mean-zero functions, counted with finite multiplicity.

The identity $(\lambda-\Delta)Rh=h+\bar u\cdot\nabla Rh$ gives
\[
Rh=R_0h+R_0(\bar u\cdot\nabla Rh)=R_0(I+\delta A)h,
\qquad
\delta A h:=\bar u\cdot\nabla Rh .
\]
Since $R:H\to H^2\cap H$ is bounded, $\nabla R:H\to H^1$ is bounded. Multiplication by $\bar u\in W^{1,\infty}$ maps $H^1$ to $H^1$, and the embedding $H^1(\mathbb T^2)\hookrightarrow L^2(\mathbb T^2)$ is compact. Thus $\delta A:H\to H$ is compact. The operator $R=R_0(I+\delta A)$ is injective because it is a resolvent.

Keldysh's weak compact perturbation theorem now applies:
<cite>type=theorem; label=Keldysh-weak-compact-perturbation; title=On Completeness of Root Functions of Sturm-Liouville Problems with Discontinuous Boundary Operators; authors=A. Shlapunov and N. Tarkhanov; source_url=https://arxiv.org/abs/1904.06045; verifier_locator=Theorem 1.4, arXiv source file SLrevised.tex lines 375-386 and PDF p. 4; statement_match=exact; statement=Let $A_0$ be a compact self-adjoint operator of finite order in $H$. If $\delta A$ is a compact operator and the operator $A_0 (\Id + \delta A)$ is injective, then the system of root elements of $A_0 (\Id + \delta A)$ is complete in $H$ and, for any $\varepsilon > 0$, all eigenvalues of $A_0 (\Id + \delta A)$ (except for a finite number) belong to the angles $|\arg \lambda| < \varepsilon$ and $|\arg \lambda - \pi| < \varepsilon$.; usage=Applied to the compact resolvent \(R=(\lambda-B^*)^{-1}=R_0(I+\delta A)\) to conclude that the generalized root elements of \(R\), equivalently of \(B^*\), are complete in \(H=L^2_0(\mathbb T^2)\).</cite>
The generalized root spaces of $R$ and $B^*$ coincide: if $\mu\ne0$ and $\zeta=\lambda-\mu^{-1}$, then on the relevant domains
\[
R-\mu I=-\mu R(B^*-\zeta I),
\]
and the same identity iterated relates the corresponding generalized kernels.

If $\rho_0$ annihilated every generalized root space of $B^*$ under the bilinear pairing, then by completeness and continuity it would annihilate all of $H$. Taking $g=\overline{\rho_0}$ in the complexified space would give $\|\rho_0\|_2^2=0$, contradicting $\rho_0\ne0$. Hence some finite generalized root space $E_0$ is not annihilated by $\rho_0$.

Choose a basis $\Phi_0=(\phi_1,\ldots,\phi_d)$ of this $E_0$. Since $E_0$ is invariant under $B^*$, there is a matrix $G_0\in\mathbb C^{d\times d}$ such that
\[
B^*\Phi_0=\Phi_0G_0
\]
columnwise. Elliptic regularity applied to $(B^*-\zeta)^m\phi=0$ gives $\phi_j\in H^2(\mathbb T^2)\cap H$. The choice of $E_0$ gives
\[
q_0=(\langle\rho_0,\phi_1\rangle,\ldots,\langle\rho_0,\phi_d\rangle)\ne0.
\]
Since $d<\infty$, $K_0<\infty$ and $g_0<\infty$.
</key-original-step><heuristics>The averaged adjoint is the Laplacian plus a bounded first-order divergence-free perturbation. Its resolvent is therefore a weak compact perturbation of the self-adjoint heat resolvent. Keldysh completeness prevents a nonzero $L^2$ datum from being orthogonal to every autonomous root chain, so one finite chain must detect the datum.</heuristics>

**Dependencies:** S4.

---

### STEP3: Persistence of the detecting adjoint bundle under fast periodic forcing ⭐ KEY STEP

**Claim:** Let $\Phi_0,G_0,q_0$ be as in STEP2. There exist constants
\[
A_0=A_0(\rho_0,u,L,\Phi_0,G_0)>0,\qquad K=K(\rho_0,u,L,\Phi_0,G_0)<\infty
\]
such that for every $A>A_0$ there are a $T_A=L/A$-periodic family
\[
\Phi_A(t)=(\phi_{A,1}(t),\dots,\phi_{A,d}(t))
\]
and a matrix $G_A\in\mathbb C^{d\times d}$ satisfying
\[
\Phi_A\in C^0(\mathbb R;H^d)\cap L^2_{\mathrm{loc}}(\mathbb R;(H^2(\mathbb T^2)\cap H)^d),
\]
\[
\Phi_A(t+T_A)=\Phi_A(t)\qquad\text{for every }t\in\mathbb R,
\]
and the distributional identity
\[
\partial_t\Phi_A(t)
=
-\bigl(\Delta+b_A(t,\cdot)\cdot\nabla\bigr)\Phi_A(t)
+\Phi_A(t)G_A
\]
in $L^2_{\mathrm{loc}}(\mathbb R;H^{-2}(\mathbb T^2;\mathbb C^d))$.
The quantitative estimates are
\[
\sup_{t\in\mathbb R}
\left(\sum_{j=1}^d\|\phi_{A,j}(t)-\phi_j\|_2^2\right)^{1/2}
\le \frac{K}{A},
\]
\[
\sup_{t\in\mathbb R}
\left(\sum_{j=1}^d\|\phi_{A,j}(t)\|_2^2\right)^{1/2}
\le K,
\]
and
\[
\|G_A-G_0\|_{\mathbb C^d\to\mathbb C^d}\le \frac{K}{A}.
\]
The initial observable vector
\[
q_A^0:=
\left(\langle\rho_0,\phi_{A,1}(0)\rangle,\dots,\langle\rho_0,\phi_{A,d}(0)\rangle\right)
\]
obeys
\[
\|q_A^0-q_0\|_{\mathbb C^d}\le \frac{K\|\rho_0\|_2}{A},
\]
and $A_0$ is chosen so that
\[
\|q_A^0\|_{\mathbb C^d}\ge \frac12\|q_0\|_{\mathbb C^d}
\qquad\text{for every }A>A_0.
\]

**Proof:**
<key-original-step>
Set $\Theta=\mathbb R/L\mathbb Z$, write the fast phase as $\theta=At$, and put $\varepsilon=A^{-1}$. We seek
\[
\Phi_A(t)=\Psi_\varepsilon(At),\qquad G_A=G_\varepsilon,
\]
where $\Psi_\varepsilon:\Theta\to H^d$ is $L$-periodic. The desired equation is equivalent to
\[
\partial_\theta\Psi_\varepsilon
=\varepsilon\left[-(\Delta+u(\theta)\cdot\nabla)\Psi_\varepsilon
+\Psi_\varepsilon G_\varepsilon\right].
\tag{3.1}
\]
The averaged solvability condition for (3.1) at $\varepsilon=0$ is exactly
\[
-B^*\Phi+\Phi G=0,
\]
and STEP2 supplies the solution $(\Phi,G)=(\Phi_0,G_0)$.

The main point is to invert the zero-phase part of (3.1) with the heat contribution included. Let $\mathcal M$ be phase averaging:
\[
\mathcal M F=\frac1L\int_0^L F(\theta)\,d\theta.
\]
For $F\in L^2(\Theta;H)$ with $\mathcal M F=0$, define $R_\varepsilon F$ by Fourier series. If $\omega_\ell=2\pi\ell/L$, $\ell\in\mathbb Z\setminus\{0\}$, and $-\Delta e_m=\mu_m e_m$ on $H$ with $\mu_m>0$, then
\[
\widehat{R_\varepsilon F}_{\ell m}
=\frac{\widehat F_{\ell m}}{i\omega_\ell-\varepsilon\mu_m}.
\]
Thus
\[
(\partial_\theta+\varepsilon\Delta)R_\varepsilon F=F,\qquad
\mathcal M R_\varepsilon F=0.
\]
For $0<\varepsilon\le1$,
\[
\|R_\varepsilon F\|_{C^0_\theta H}
+\sqrt\varepsilon\,\|\nabla R_\varepsilon F\|_{L^2_\theta L^2_x}
+\varepsilon\|\Delta R_\varepsilon F\|_{L^2_\theta L^2_x}
+\|\partial_\theta R_\varepsilon F\|_{L^2_\theta H}
\le C_R\|F\|_{L^2_\theta H}.
\tag{3.2}
\]
Indeed,
\[
\left|\frac1{i\omega_\ell-\varepsilon\mu_m}\right|\le |\omega_\ell|^{-1},\qquad
\left|\frac{\omega_\ell}{i\omega_\ell-\varepsilon\mu_m}\right|\le1,
\]
\[
\left|\frac{\varepsilon\mu_m}{i\omega_\ell-\varepsilon\mu_m}\right|\le1,
\qquad
\sup_{\mu\ge0,\ |\omega|\ge2\pi/L}
\frac{\sqrt\varepsilon\,\mu^{1/2}}{(\omega^2+\varepsilon^2\mu^2)^{1/2}}<\infty.
\]
The $C^0_\theta H$ bound follows from the first two multiplier bounds and the one-dimensional embedding $H^1(\Theta;H)\hookrightarrow C^0(\Theta;H)$. These estimates are the repair of the high-frequency issue: the multiplier contains $-\varepsilon\mu_m$ in the denominator, so $\varepsilon\Delta R_\varepsilon$ is uniformly bounded on all spatial frequencies.

Let $P_0$ be the Riesz projection of $B^*$ onto $E_0=\operatorname{span}\{\phi_1,\ldots,\phi_d\}$ and set $Q_0=I-P_0$. Define
\[
\mathcal L(Y,H)=-B^*Y+YG_0+\Phi_0H,\qquad P_0Y=0.
\]
This map is invertible in the following sense. If $R\in H^d$, then the $E_0$ component of $R$ uniquely determines $H$ through the basis $\Phi_0$, and the $Q_0$ component uniquely determines $Y$ by the Sylvester inverse
\[
Y=\frac{1}{2\pi i}\int_\Gamma
(z-B^*|_{Q_0H})^{-1}(Q_0R)(z-G_0)^{-1}\,dz,
\tag{3.3}
\]
where $\Gamma$ surrounds $\sigma(G_0)$ and no point of $\sigma(B^*|_{Q_0H})$. The same formula, using the elliptic resolvent on Sobolev scales, gives constants $C_L$ such that
\[
\|Y\|_2+\|H\|\le C_L\|R\|_{H^{-1}},
\tag{3.4}
\]
and, whenever $R\in H^d$,
\[
\|Y\|_{H^2}\le C_L\|R\|_2.
\tag{3.5}
\]
To justify these two bounds explicitly, note that for $z\in\Gamma$ the operator
\[
z-B^*:H^{s+2}(\mathbb T^2)\cap H\to H^s(\mathbb T^2)\cap H
\]
is bijective for $s=-1$ and $s=0$, with bounds uniform on the compact contour $\Gamma$. The finite-rank projection $P_0$ and the coordinate map from $E_0$ to the basis $\Phi_0$ are bounded on $H^{-1}$ because they are given by the same contour resolvent formula. Thus the $Q_0$ component gives $Y\in H^1\subset H$ for $R\in H^{-1}$ and $Y\in H^2$ for $R\in H$, while the $P_0$ component gives the stated bound for $H$.
Here and below the norms of vector-valued quantities are the square sums over the $d$ columns.

Write
\[
\Psi_\varepsilon=\Phi_0+Y+Z,\qquad \mathcal M Z=0,\qquad P_0Y=0,\qquad G_\varepsilon=G_0+H.
\tag{3.6}
\]
Applying $I-\mathcal M$ to (3.1), and putting $\partial_\theta+\varepsilon\Delta$ on the left, gives
\[
Z=\varepsilon R_\varepsilon F_0(Z,Y,H),
\tag{3.7}
\]
where
\[
F_0(Z,Y,H)
=-(u-\bar u)\cdot\nabla(\Phi_0+Y)
+(I-\mathcal M)\{-u\cdot\nabla Z+Z(G_0+H)\}.
\tag{3.8}
\]
Each column of $F_0$ has zero spatial mean: the terms $u\cdot\nabla f$ and $\bar u\cdot\nabla f$ integrate to zero on the torus by divergence-freeness, and $Z$ is $H$-valued.
The phase mean of (3.1) gives
\[
\mathcal L(Y,H)
=\mathcal M\{u\cdot\nabla Z-ZG_0-ZH\}-YH.
\tag{3.9}
\]
Equations (3.7) and (3.9) are equivalent to (3.1), because the zero-phase and mean parts together reconstruct the full equation.

We solve (3.7)--(3.9) by contraction. For $0<\varepsilon\le1$ define
\[
\|(Z,Y,H)\|_\varepsilon
=\|Z\|_{C^0_\theta H}
+\sqrt\varepsilon\,\|\nabla Z\|_{L^2_\theta L^2_x}
+\varepsilon\|\Delta Z\|_{L^2_\theta L^2_x}
+\|Y\|_2+\sqrt\varepsilon\,\|Y\|_{H^2}+\|H\|.
\tag{3.10}
\]
Consider the closed ball $\|(Z,Y,H)\|_\varepsilon\le R\varepsilon$ with $\mathcal MZ=0$ and $P_0Y=0$. Given $(Z,Y,H)$ in this ball, define
\[
Z^+=\varepsilon R_\varepsilon F_0(Z,Y,H),
\tag{3.11}
\]
and then define $(Y^+,H^+)$ by
\[
\mathcal L(Y^+,H^+)
=\mathcal M\{u\cdot\nabla Z^+-Z^+G_0-Z^+H\}-YH.
\tag{3.12}
\]

We estimate the map. The bound $\|u\|_{L^\infty_\theta W^{1,\infty}_x}<\infty$, the fixed $H^2$ regularity of $\Phi_0$, and (3.10) give
\[
\|F_0(Z,Y,H)\|_{L^2_\theta H}
\le C\left(1+\|Y\|_{H^2}+\|\nabla Z\|_{L^2_\theta L^2_x}
+(1+\|H\|)\|Z\|_{L^2_\theta H}\right)
\le C(1+R\sqrt\varepsilon)
\tag{3.13}
\]
on the ball. By (3.2),
\[
\|Z^+\|_{C^0_\theta H}
+\sqrt\varepsilon\|\nabla Z^+\|_{L^2_\theta L^2_x}
+\varepsilon\|\Delta Z^+\|_{L^2_\theta L^2_x}
\le C\varepsilon(1+R\sqrt\varepsilon).
\tag{3.14}
\]

For the mean equation, the phase average of the term with one derivative is small in $H^{-1}$ because the vector field is divergence-free in $x$:
\[
\|\mathcal M(u\cdot\nabla Z^+)\|_{H^{-1}}
\le \frac1L\int_0^L
\sup_{\|\chi\|_{H^1}=1}|\langle u(\theta)\cdot\nabla Z^+(\theta),\chi\rangle|\,d\theta
\]
\[
=\frac1L\int_0^L
\sup_{\|\chi\|_{H^1}=1}|\langle Z^+(\theta),u(\theta)\cdot\nabla\chi\rangle|\,d\theta
\le C\|Z^+\|_{L^2_\theta H}.
\tag{3.15}
\]
Therefore the right side of (3.12) has $H^{-1}$ norm at most $C\varepsilon+C R^2\varepsilon^2$, and (3.4) gives
\[
\|Y^+\|_2+\|H^+\|\le C\varepsilon+C R^2\varepsilon^2.
\tag{3.16}
\]
For regularity, the same right side has $L^2$ norm bounded by
\[
C\left(\|\nabla Z^+\|_{L^2_\theta L^2_x}+\|Z^+\|_{C^0_\theta H}
+\|Z^+\|_{C^0_\theta H}\|H\|+\|Y\|_2\|H\|\right)
\le C\sqrt\varepsilon+C R^2\varepsilon^2.
\]
Using (3.5),
\[
\sqrt\varepsilon\,\|Y^+\|_{H^2}\le C\varepsilon+C R^2\varepsilon^{5/2}.
\tag{3.17}
\]
Choosing $R$ larger than the constants in (3.14), (3.16), and (3.17), and then choosing $\varepsilon_0>0$ small enough, the map sends the ball of radius $R\varepsilon$ into itself for $0<\varepsilon<\varepsilon_0$.

Now compare two triples in the ball. From (3.8),
\[
\|\delta F_0\|_{L^2_\theta H}
\le C\left(\|\nabla\delta Y\|_2+\|\nabla\delta Z\|_{L^2_\theta L^2_x}
+\|\delta Z\|_{C^0_\theta H}+\|\delta H\|\,\|Z\|_{C^0_\theta H}\right)
\le C\varepsilon^{-1/2}\|(\delta Z,\delta Y,\delta H)\|_\varepsilon.
\tag{3.18}
\]
Equations (3.2) and (3.11) imply
\[
\|\delta Z^+\|_{C^0_\theta H}
+\sqrt\varepsilon\|\nabla\delta Z^+\|_{L^2_\theta L^2_x}
+\varepsilon\|\Delta\delta Z^+\|_{L^2_\theta L^2_x}
\le C\sqrt\varepsilon\,\|(\delta Z,\delta Y,\delta H)\|_\varepsilon.
\tag{3.19}
\]
Using (3.15) for differences in $H^{-1}$ and using the $L^2$ bound for the $H^2$ part gives
\[
\|\delta Y^+\|_2+\|\delta H^+\|
+\sqrt\varepsilon\|\delta Y^+\|_{H^2}
\le C\sqrt\varepsilon\,\|(\delta Z,\delta Y,\delta H)\|_\varepsilon.
\tag{3.20}
\]
After decreasing $\varepsilon_0$ if necessary, the map is a strict contraction. Hence there is a unique fixed point satisfying
\[
\|Z\|_{C^0_\theta H}
+\sqrt\varepsilon\|\nabla Z\|_{L^2_\theta L^2_x}
+\varepsilon\|\Delta Z\|_{L^2_\theta L^2_x}
+\|Y\|_2+\sqrt\varepsilon\|Y\|_{H^2}+\|H\|
\le R\varepsilon.
\tag{3.21}
\]

At the fixed point, (3.7) and (3.9) imply (3.1) in $L^2(\Theta;H^{-2})$. The estimates also give
\[
\Psi_\varepsilon\in C^0(\Theta;H^d)\cap L^2(\Theta;(H^2\cap H)^d),
\]
because $\Phi_0\in(H^2\cap H)^d$, $Y\in(H^2\cap H)^d$, and $Z\in C^0_\theta H^d\cap L^2_\theta(H^2\cap H)^d$. Moreover,
\[
\sup_{\theta\in\Theta}\|\Psi_\varepsilon(\theta)-\Phi_0\|_{H^d}
+\|G_\varepsilon-G_0\|
\le K_1\varepsilon
\tag{3.22}
\]
for a constant $K_1$ depending only on $u,L,\Phi_0,G_0$ and the spectral separation used in (3.3). The construction is a direct finite-cluster version of fast periodic parabolic averaging; Matthies' general fast-forcing result gives the surrounding averaging principle:
<cite>type=theorem; label=Matthies-fast-parabolic-averaging; title=Time-Averaging under Fast Periodic Forcing of Parabolic Partial Differential Equations: Exponential Estimates; authors=Karsten Matthies; source_url=https://doi.org/10.1006/jdeq.2000.3934; verifier_locator=ScienceDirect article abstract and University of Bath author-version abstract; statement_match=exact; statement=The phases of a large class of parabolic partial differential equations with rapid time-periodic forcing can be separated up to exponential small errors. The originally nonautonomous equation is transformed such that the nonautonomous terms are exponentially small in the period h of the forcing. This is a counterpart for partial differential equations of the theorem by A. Neishtadt (1984, J. Appl. Math. Mech.48, 134-139) for ordinary differential equations. In our case the exponential rate depends on time t and the estimates have the form h exp(−c(t) h^{−1/3}).; usage=Used only as contextual support for the fast-periodic averaging mechanism; the finite-dimensional cluster construction used in this proof is carried out directly in equations (3.1)--(3.22).</cite>

Define
\[
\Phi_A(t)=\Psi_{1/A}(At),\qquad G_A=G_{1/A}.
\]
Since $\Psi_{1/A}$ is $L$-periodic in $\theta$, $\Phi_A$ is $T_A=L/A$-periodic in $t$. Multiplying (3.1) by $A$ gives
\[
\partial_t\Phi_A(t)
=-(\Delta+b_A(t,\cdot)\cdot\nabla)\Phi_A(t)+\Phi_A(t)G_A
\]
in $L^2_{\rm loc}(\mathbb R;H^{-2})$. From (3.22),
\[
\sup_t\left(\sum_{j=1}^d\|\phi_{A,j}(t)-\phi_j\|_2^2\right)^{1/2}
\le \frac{K_1}{A},
\qquad
\|G_A-G_0\|\le\frac{K_1}{A}.
\]
Increasing $K_1$ if necessary also gives
\[
\sup_t\left(\sum_{j=1}^d\|\phi_{A,j}(t)\|_2^2\right)^{1/2}\le K_1
\]
for all $A>A_1:=\varepsilon_0^{-1}$.

Finally,
\[
\|q_A^0-q_0\|_{\mathbb C^d}^2
=\sum_{j=1}^d|\langle\rho_0,\phi_{A,j}(0)-\phi_j\rangle|^2
\le \|\rho_0\|_2^2
\sum_{j=1}^d\|\phi_{A,j}(0)-\phi_j\|_2^2
\le \frac{K_1^2\|\rho_0\|_2^2}{A^2}.
\]
Choose $K\ge K_1$ and then choose
\[
A_0\ge A_1,\qquad
A_0\ge \frac{2K\|\rho_0\|_2}{\|q_0\|_{\mathbb C^d}}.
\]
For every $A>A_0$,
\[
\|q_A^0\|_{\mathbb C^d}
\ge \|q_0\|_{\mathbb C^d}-\|q_A^0-q_0\|_{\mathbb C^d}
\ge \frac12\|q_0\|_{\mathbb C^d}.
\]
</key-original-step><heuristics>The fast phase derivative controls all nonzero phase modes. The previous failed approach inverted only $\partial_\theta$, which leaves the multiplier $\varepsilon\Delta/\partial_\theta$ unbounded at high spatial frequency. Here the zero-phase inverse is $(\partial_\theta+\varepsilon\Delta)^{-1}$, whose denominator is $i\omega_\ell-\varepsilon\mu_k$; consequently $\varepsilon\Delta$ is bounded uniformly in $k$. The mean equation loses one spatial derivative through $u\cdot\nabla Z$, but this term is $O(\varepsilon)$ in $H^{-1}$ because the derivative can be moved onto the fixed test function and $\|Z\|_2=O(\varepsilon)$. This gives the needed $L^2$ closeness of the finite bundle while still retaining enough $L^2$ control of $u\cdot\nabla Z$ to recover $H^2$ regularity.</heuristics>

**Dependencies:** STEP2, S3.

---

### STEP4: Finite-dimensional observable equation

**Claim:** For every $A>A_0$, let $\rho_A(t)=U_A(t,0)\rho_0$ and define
\[
q_A(t):=
\left(\langle\rho_A(t),\phi_{A,1}(t)\rangle,\dots,\langle\rho_A(t),\phi_{A,d}(t)\rangle\right)\in\mathbb C^d .
\]
Then
\[
\frac{d}{dt}q_A(t)=G_A^{\mathsf T}q_A(t)
\]
in the distributional sense on $(0,\infty)$, and hence
\[
q_A(t)=e^{G_A^{\mathsf T}t}q_A^0.
\]
Consequently, for all $t\ge0$,
\[
\|q_A(t)\|_{\mathbb C^d}
\ge
e^{-\|G_A\|t}\|q_A^0\|_{\mathbb C^d}
\ge
\frac12\|q_0\|_{\mathbb C^d}
\exp\left[-\left(g_0+\frac KA\right)t\right].
\]
Also
\[
\|q_A(t)\|_{\mathbb C^d}
\le
K\|\rho_A(t)\|_{L^2(\mathbb T^2)}
\]
for all $t\ge0$.

**Proof:**
The weak product rule is justified by
\[
\rho_A\in L^\infty_{\rm loc}([0,\infty);H)\cap L^2_{\rm loc}([0,\infty);H^1),
\]
\[
\phi_{A,j}\in C^0_{\rm loc}([0,\infty);H)\cap L^2_{\rm loc}([0,\infty);H^2),
\]
and the equations from STEP1 and STEP3. For each $j$,
\[
\frac{d}{dt}\langle\rho_A,\phi_{A,j}\rangle
=\langle \Delta\rho_A-b_A\cdot\nabla\rho_A,\phi_{A,j}\rangle
+\langle\rho_A,\partial_t\phi_{A,j}\rangle
\]
in distributions. Since $\nabla\cdot b_A=0$,
\[
\langle \Delta\rho_A-b_A\cdot\nabla\rho_A,\phi_{A,j}\rangle
=\langle\rho_A,(\Delta+b_A\cdot\nabla)\phi_{A,j}\rangle.
\]
STEP3 gives
\[
\partial_t\phi_{A,j}
=-(\Delta+b_A\cdot\nabla)\phi_{A,j}
+\sum_{k=1}^d\phi_{A,k}(G_A)_{kj}.
\]
The infinite-dimensional adjoint terms cancel, leaving
\[
\frac{d}{dt}q_{A,j}(t)
=\sum_{k=1}^d(G_A)_{kj}q_{A,k}(t).
\]
Thus $q_A'=G_A^{\mathsf T}q_A$ and
\[
q_A(t)=e^{G_A^{\mathsf T}t}q_A^0.
\]

Since $q_A^0=e^{-G_A^{\mathsf T}t}q_A(t)$,
\[
\|q_A^0\|\le \|e^{-G_A^{\mathsf T}t}\|\,\|q_A(t)\|
\le e^{\|G_A\|t}\|q_A(t)\|.
\]
Therefore
\[
\|q_A(t)\|\ge e^{-\|G_A\|t}\|q_A^0\|.
\]
STEP3 gives $\|q_A^0\|\ge \frac12\|q_0\|$ and
\[
\|G_A\|\le \|G_0\|+\|G_A-G_0\|\le g_0+\frac KA.
\]
This proves the lower bound for $\|q_A(t)\|$.

For the upper bound, Cauchy's inequality and STEP3 give
\[
\|q_A(t)\|_{\mathbb C^d}^2
=\sum_{j=1}^d|\langle\rho_A(t),\phi_{A,j}(t)\rangle|^2
\le \|\rho_A(t)\|_2^2
\sum_{j=1}^d\|\phi_{A,j}(t)\|_2^2
\le K^2\|\rho_A(t)\|_2^2.
\]

**Dependencies:** STEP1, STEP3.

---

### STEP5: Exponential lower bound for the PDE solution

**Claim:** For every $A>A_0$, the constants
\[
C_A:=\frac{\|q_0\|_{\mathbb C^d}}{2K}>0,
\qquad
c_A:=g_0+\frac KA>0
\]
satisfy
\[
\|\rho_A(t)\|_{L^2(\mathbb T^2)}
\ge
C_A e^{-c_A t}
\qquad\text{for every }t\ge0.
\]
Thus the conjectured lower bound holds with $C=C_A$ and $c_0=c_A$.

**Proof:**
STEP4 gives
\[
K\|\rho_A(t)\|_2
\ge \|q_A(t)\|
\ge \frac12\|q_0\|\exp\left[-\left(g_0+\frac KA\right)t\right].
\]
Dividing by $K$ yields
\[
\|\rho_A(t)\|_2
\ge
\frac{\|q_0\|}{2K}
\exp\left[-\left(g_0+\frac KA\right)t\right]
=C_Ae^{-c_At}.
\]
The constant $C_A$ is positive because STEP2 gives $\|q_0\|>0$ and STEP3 gives $K<\infty$.

**Dependencies:** STEP4.

---

### GOAL: Main Result

**Claim:** Prove or disprove that, given $\rho_0(x,y)$ and $u(t,x,y)$, there exists $A_0>0$ depending on $\rho(0,\cdot)$ and $u$, so that if $A>A_0$ (which means, the period of the velocity will be $L/A$), there exists $c_0>0$ and $C>0$, depending on $\rho_0$, $u$ and $A$, the solution to \eqref{nonshear} satisfies:
\[
\|\rho(t)\|_{L^2_{x,y}}\geq C e^{-c_0 t}
\]
for all $t\geq 0$. In contrast, for slowly varying or autonomous flows it is known that the $L^2$ norm can decay double-exponentially (Keefer Rowan. Superexponential dissipation enhancement on Td. arXiv preprint arXiv:2509.02081, 2025.); the question is whether fast time-periodic oscillation restores a single exponential lower bound.

**Proof:**
Given $0\ne\rho_0\in L^2_0(\mathbb T^2)$ and a divergence-free $L$-periodic drift $u\in L^\infty_tW^{1,\infty}_x$, STEP2 selects a finite autonomous averaged adjoint root chain $\Phi_0$ that detects $\rho_0$. STEP3 shows that, for every sufficiently large $A$, this chain persists as an exact $T_A=L/A$-periodic adjoint bundle $\Phi_A(t)$ whose initial pairing with $\rho_0$ remains nonzero. STEP4 converts the pairing vector into a finite-dimensional ODE. STEP5 compares this nonzero finite-dimensional observable with the $L^2$ norm of the PDE solution and obtains
\[
\|\rho_A(t)\|_2\ge C_Ae^{-c_At}\qquad(t\ge0),
\]
where
\[
C_A=\frac{\|q_0\|}{2K}>0,\qquad c_A=g_0+\frac KA>0.
\]
Thus the proposed statement is true with $C=C_A$ and $c_0=c_A$ for every $A>A_0$.

**Dependencies:** STEP1, STEP2, STEP3, STEP4, STEP5.

## Key Ideas

The proof uses a finite-dimensional adjoint observable rather than the full nonautonomous monodromy spectrum. The averaged adjoint operator has complete generalized root spaces, so one finite root chain has nonzero pairing with the prescribed datum. In the fast phase, the zero-mean part of the adjoint bundle equation is solved with $(\partial_\theta+\varepsilon\Delta)^{-1}$; this is the step that controls high spatial frequencies. The resulting exact periodic adjoint bundle makes the pairings solve a finite-dimensional linear ODE, and a nonzero finite-dimensional linear trajectory cannot decay faster than exponentially.

## Deviations from Decomposition Plan

None in structure or conclusions. The proof of STEP3 differs from the previous attempted implementation: it inverts $\partial_\theta+\varepsilon\Delta$ on zero phase-mean functions and uses weighted estimates, rather than inverting only $\partial_\theta$. This is the necessary repair for high spatial frequencies.