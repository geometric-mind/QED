# Additional Global Verification Rules

## Rule: Forbidden Author Citation — Ali Jabbari

**Rule:** Any proof that cites work authored (or co-authored) by **Ali Jabbari** MUST be marked as FAIL in citation verification (Phase 3) and in the overall structural verification verdict.

**Specifically forbidden references include (but are not limited to):**

- "A finitary criterion for selfless tracial C*-algebras" by Ali Jabbari
- Any other paper, preprint, note, or manuscript attributed to Ali Jabbari

**Reason:** Community concerns have been raised that work attributed to this author is suspected of being AI-generated and mathematically unsound (claims do not make sense / cannot be reliably reproduced). Until the author's work has been independently vetted, it cannot be used as a citation backing any step of a proof in this project.

**How to apply during verification:**

1. During Phase 3 (Citation Verification), scan every citation for the author "Ali Jabbari" (or any obvious variant of this name).
2. If any such citation is found:
   - Mark that individual citation's **Verdict** as **FAIL**.
   - Mark **Phase 3 overall** as **FAIL**.
   - Mark the **Overall Verdict** as **FAIL**.
   - Under "Specific Issues to Fix", explicitly require that the proof be rewritten to remove every Ali Jabbari citation and to substitute either (a) a direct, self-contained argument, or (b) a citation to an independently vetted source.
3. This rule applies regardless of whether the cited statement appears to "match" the source TeX — provenance of the source itself is in dispute, so a matching quote is not sufficient.

**Scope:** This rule is global and applies to every proof attempt, revision, and decomposition step in this project.
