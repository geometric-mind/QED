# Probability Problems (May 15, 2026)

There are two problems in this folder. Both problems are research-level open questions in probability theory contributed by **Minghao Pan**, PhD candidate at the Caltech Mathematics Department.

## QED Configuration

- **Prover mode:** Decomposition
- **Literature survey:** Codex, gpt-5.5-pro
- **Decomposer:** Codex, gpt-5.5-pro
- **Prover:** Codex, gpt-5.5-pro
- **Structural verifier:** Codex, gpt-5.5-pro
- **Detailed verifier:** Codex, gpt-5.5-pro
- **Regulator:** Codex, gpt-5.5-pro
- **Brainstorm:** Disabled

## Results

| Problem | Result |
|---------|--------|
| P1 | Proved |
| P2 | Proved |

Final proofs of P1 and P2 are human-verified by Minghao Pan.

## Problems

### P1 — Return probability asymptotics for lamplighter walk on $\mathbb{Z}_2 \wr T_d$

Let $d \ge 3$, let $T_d$ be the infinite $d$-regular tree. Consider the usual switch–walk–switch lamplighter random walk on the lamplighter graph $\mathbb{Z}_2 \wr T_d$ and let $p_n(x,y)$ denote its $n$-step transition probability. Then, as $n \to \infty$,
$$p_{2n}(e,e) = \rho_d^{2n} \exp\!\left[-\bigl(\pi^2(\log(d-1))^2 + o(1)\bigr)\frac{n}{\log^2 n}\right],$$
where
$$\rho_d = \frac{2\sqrt{d-1}}{d}.$$

### P2 — Total variation asymptotics for switch-walk-switch on $\mathbb{Z}_2 \wr \mathbb{Z}$

Let $P_t^x$ denote the law at time $t$ of the discrete-time switch-walk-switch walk on $\mathbb{Z}_2 \wr \mathbb{Z}$. For $x = (\mathbf{0}, 0)$ and $y = (\mathbf{0}, 2)$, one has the asymptotic behavior
$$\|P_t^x - P_t^y\|_{\mathrm{TV}} \asymp t^{-1/2},$$
where $\asymp$ denotes equality up to positive multiplicative constants.

## Workflow

- Minghao Pan provided two research-level open problems in probability theory to QED.
- QED ran on each problem with the configuration above.
- No human mathematical input was provided beyond the problem statements.
- QED generated correct proofs for both questions through multiple rounds of refinement, including substantial changes of proof plan by the decomposition agent.
- The proofs for P1 and P2 were sent back to Minghao Pan, who verified their correctness.

## Expert Comments from Minghao Pan

1. We evaluate QED on two research-level open questions in probability theory. Without human mathematical input beyond the problem statements, QED generated correct proofs for both questions through multiple rounds of refinement, including substantial changes of proof plan by the decomposition agent.

2. The first result (P1) is a solid specialized contribution. Its proof has real mathematical content as it cleverly combines probabilistic constructions with spectral analysis. Its significance appears comparable to work suitable for venues such as the *Electronic Journal of Probability* or *Proceedings of the American Mathematical Society*.

3. The second question (P2) is a technically nontrivial PhD-level problem.

4. Both questions are in the style of precise probabilistic calculations and estimates.
