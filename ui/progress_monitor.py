"""File-system scanner and Streamlit renderer for decomposition-mode progress."""

import os
import re

import streamlit as st

from utils import (
    decomp_root,
    attempt_dir,
    revision_dir,
    proof_dir,
    list_attempt_dirs,
    list_revision_dirs,
    list_proof_dirs,
    parse_status_md,
    is_survey_complete,
    is_summary_complete,
    proof_succeeded,
    decomp_failed,
    parse_difficulty,
    parse_token_usage,
    read_file,
    file_nonempty,
)


# ---------------------------------------------------------------------------
# Scan
# ---------------------------------------------------------------------------

_PROOF_FILES = {
    "proof_md": "proof.md",
    "prover_response": "prover_response.md",
    "scratchpad": "scratchpad.md",
    "structural_verification": "structural_verification.md",
    "detailed_verification": "detailed_verification.md",
    "regulator_decision": "regulator_decision.md",
}


def _scan_proof(proof_path: str, num: int) -> dict:
    files = {key: file_nonempty(os.path.join(proof_path, name))
             for key, name in _PROOF_FILES.items()}
    error_files: list[str] = []
    if os.path.isdir(proof_path):
        for name in sorted(os.listdir(proof_path)):
            if name.startswith("error_") and name.endswith(".md"):
                if file_nonempty(os.path.join(proof_path, name)):
                    error_files.append(name)
    return {
        "num": num,
        "dir": proof_path,
        **files,
        "error_files": error_files,
    }


def _scan_revision(output_dir: str, n: int, m: int) -> dict:
    r_path = revision_dir(output_dir, n, m)
    decomp_yaml = os.path.join(r_path, "decomposition.yaml")
    decomp_resp = os.path.join(r_path, "decomposer_response.md")
    proofs = [
        _scan_proof(os.path.join(r_path, f"proof_{k}"), k)
        for k in list_proof_dirs(r_path)
    ]
    return {
        "num": m,
        "dir": r_path,
        "decomposition_yaml": decomp_yaml if file_nonempty(decomp_yaml) else None,
        "decomposer_response": decomp_resp if file_nonempty(decomp_resp) else None,
        "proofs": proofs,
    }


def _scan_attempt(output_dir: str, n: int) -> dict:
    a_path = attempt_dir(output_dir, n)
    revisions = [
        _scan_revision(output_dir, n, m) for m in list_revision_dirs(a_path)
    ]
    return {"num": n, "dir": a_path, "revisions": revisions}


def scan_progress(output_dir: str) -> dict:
    """Scan an output directory and return a snapshot of decomposition-mode progress."""
    result = {
        "exists": False,
        "survey_complete": False,
        "difficulty": "unknown",
        "summary_complete": False,
        "pipeline_complete": False,
        "proof_succeeded": False,
        "decomp_failed": False,
        "current_stage": "idle",
        "decomposition_state": {
            "state_label": "",
            "current_attempt": None,
            "current_revision": None,
            "current_proof": None,
            "last_updated": "",
            "recent_activity": "",
        },
        "attempts": [],
        "token_usage": None,
        "final_proof": "",
        "failure_analysis": "",
    }

    if not os.path.isdir(output_dir):
        return result

    result["exists"] = True
    result["survey_complete"] = is_survey_complete(output_dir)
    result["difficulty"] = parse_difficulty(output_dir)
    result["summary_complete"] = is_summary_complete(output_dir)
    result["pipeline_complete"] = result["summary_complete"]
    result["proof_succeeded"] = proof_succeeded(output_dir)
    result["decomp_failed"] = decomp_failed(output_dir)

    status = parse_status_md(output_dir)
    result["decomposition_state"] = {
        "state_label": status["state"],
        "current_attempt": status["attempt"],
        "current_revision": status["revision"],
        "current_proof": status["proof"],
        "last_updated": status["last_updated"],
        "recent_activity": status["recent_activity"],
    }

    result["attempts"] = [
        _scan_attempt(output_dir, n) for n in list_attempt_dirs(output_dir)
    ]

    result["token_usage"] = parse_token_usage(output_dir)
    result["final_proof"] = read_file(os.path.join(output_dir, "proof.md"))
    result["failure_analysis"] = read_file(
        os.path.join(decomp_root(output_dir), "failure_analysis.md")
    )

    # Stage classification
    if result["summary_complete"]:
        result["current_stage"] = "complete"
    elif result["decomp_failed"]:
        result["current_stage"] = "failed"
    elif result["proof_succeeded"]:
        result["current_stage"] = "summary"
    elif result["attempts"] or result["survey_complete"]:
        result["current_stage"] = "decomp_loop"
    elif result["exists"]:
        result["current_stage"] = "survey"
    else:
        result["current_stage"] = "idle"

    return result


# ---------------------------------------------------------------------------
# Smoke test (reused from archived progress_monitor.py)
# ---------------------------------------------------------------------------

def parse_smoke_test_status(output_dir: str) -> dict:
    result = {
        "started": False,
        "finished": False,
        "passed": 0,
        "failed": 0,
        "ok": False,
        "log": "",
    }
    log_path = os.path.join(output_dir, "pipeline_stdout.log")
    content = read_file(log_path)
    if not content.strip():
        return result

    result["started"] = True

    match = re.search(
        r"SMOKE TEST RESULTS:\s*(\d+)\s*passed,\s*(\d+)\s*failed", content
    )
    if match:
        result["finished"] = True
        result["passed"] = int(match.group(1))
        result["failed"] = int(match.group(2))
        result["ok"] = result["failed"] == 0
        end_pos = content.find("=" * 20, match.end())
        if end_pos != -1:
            nl = content.find("\n", end_pos)
            result["log"] = content[: nl + 1 if nl != -1 else end_pos + 60]
        else:
            result["log"] = content[: match.end() + 100]
    else:
        result["log"] = content

    return result


def render_smoke_test(output_dir: str, run_active: bool) -> dict:
    status = parse_smoke_test_status(output_dir)
    if not status["started"]:
        if run_active:
            st.info("Starting pipeline...")
        return status

    if status["finished"]:
        if status["ok"]:
            st.success(
                f"Smoke test **passed** ({status['passed']} checks)"
            )
        else:
            st.error(
                f"Smoke test **failed** ({status['passed']} passed, "
                f"{status['failed']} failed)"
            )
            with st.expander("Smoke Test Log", expanded=True):
                st.code(status["log"], language="text")
    else:
        if run_active:
            st.info("Running smoke tests...")
            with st.expander("Smoke Test Output (live)", expanded=True):
                st.code(status["log"], language="text")

    return status


# ---------------------------------------------------------------------------
# Display helpers (reused shape from archived)
# ---------------------------------------------------------------------------

def _tail_file(path: str, max_bytes: int = 20_000, max_lines: int = 80) -> str:
    if not os.path.exists(path):
        return ""
    try:
        with open(path, "rb") as f:
            f.seek(0, 2)
            size = f.tell()
            read_from = max(0, size - max_bytes)
            f.seek(read_from)
            raw = f.read().decode("utf-8", errors="replace")
        lines = raw.splitlines()
        if read_from > 0:
            lines = lines[1:]
        return "\n".join(lines[-max_lines:])
    except OSError:
        return ""


def _file_link(path: str, output_dir: str) -> str:
    try:
        return os.path.relpath(path, output_dir)
    except ValueError:
        return path


def _show_file(
    label: str,
    path: str,
    output_dir: str,
    expanded: bool = False,
    as_code: bool = False,
    tail: bool = False,
) -> None:
    if tail:
        content = _tail_file(path)
    else:
        content = read_file(path)
    if not content.strip():
        return
    rel = _file_link(path, output_dir)
    with st.expander(f"{label}  `{rel}`", expanded=expanded):
        if as_code:
            st.code(content, language="text")
        else:
            st.markdown(content)


def _badge(done: bool, label: str) -> str:
    return f":green[{label}: Yes]" if done else f":orange[{label}: No]"


def _render_run_config(output_dir: str) -> None:
    """Show the config snapshot that was active when this run started.

    The pipeline copies the YAML it was invoked with to
    ``<output>/config_used.yaml`` so the user can verify what was actually used
    (UI form state can be edited mid-run; this file is the source of truth).
    """
    path = os.path.join(output_dir, "config_used.yaml")
    content = read_file(path)
    if not content.strip():
        return
    rel = _file_link(path, output_dir)
    with st.expander(f"Configuration used  `{rel}`", expanded=False):
        st.caption(
            "This is the config snapshot the pipeline read at startup. "
            "Edits made in the sidebar after the run started are NOT reflected here."
        )
        st.code(content, language="yaml")


# ---------------------------------------------------------------------------
# Stage indicator + metrics
# ---------------------------------------------------------------------------

def _render_stage_indicator(scan: dict) -> None:
    """Three-column indicator: Survey | Decomp Loop | Summary."""
    stage = scan["current_stage"]
    cols = st.columns(3)
    stages = [
        ("Survey",       "survey",      scan["survey_complete"]),
        ("Decomp Loop",  "decomp_loop", bool(scan["attempts"]) or scan["proof_succeeded"]),
        ("Summary",      "summary",     scan["summary_complete"]),
    ]
    for col, (label, key, done) in zip(cols, stages):
        with col:
            if stage == "complete":
                st.success(f"**{label}** — Done")
            elif stage == "failed" and key == "decomp_loop":
                st.error(f"**{label}** — Failed")
            elif stage == key:
                st.info(f"**{label}** — Running...")
            elif done or (stage in ("summary", "complete") and key != "summary"):
                st.success(f"**{label}** — Done")
            else:
                st.markdown(f"**{label}** — Pending")


def _render_metrics(scan: dict) -> None:
    token = scan["token_usage"]
    cols = st.columns(4)
    cols[0].metric("Attempts", len(scan["attempts"]))
    cols[1].metric("Difficulty", scan["difficulty"].capitalize())
    if token:
        cols[2].metric(
            "Input Tokens",
            f"{token.get('total_input_tokens', 0):,}",
        )
        cols[3].metric(
            "Output Tokens",
            f"{token.get('total_output_tokens', 0):,}",
        )
    else:
        cols[2].metric("Input Tokens", "--")
        cols[3].metric("Output Tokens", "--")


# ---------------------------------------------------------------------------
# Status + history
# ---------------------------------------------------------------------------

def _render_status_and_history(output_dir: str) -> None:
    decomp_status_path = os.path.join(decomp_root(output_dir), "STATUS.md")
    decomp_status = read_file(decomp_status_path).strip()
    if decomp_status:
        rel = _file_link(decomp_status_path, output_dir)
        with st.expander(f"Decomposition Current State  `{rel}`", expanded=True):
            st.markdown(decomp_status)

    for sf in (
        os.path.join(output_dir, "literature_survey_log", "AUTO_RUN_STATUS.md"),
        os.path.join(output_dir, "summary_log", "AUTO_RUN_STATUS.md"),
    ):
        content = read_file(sf).strip()
        if content:
            rel = _file_link(sf, output_dir)
            with st.expander(f"Stage Status  `{rel}`", expanded=False):
                st.markdown(content)

    history_files = [
        os.path.join(output_dir, "literature_survey_log", "AUTO_RUN_STATUS.md.history"),
        os.path.join(output_dir, "summary_log", "AUTO_RUN_STATUS.md.history"),
    ]
    parts: list[str] = []
    for hf in history_files:
        content = read_file(hf).strip()
        if content:
            parts.append(f"# {_file_link(hf, output_dir)}\n{content}")
    if parts:
        with st.expander("Event History", expanded=False):
            st.code("\n\n".join(parts), language="text")


# ---------------------------------------------------------------------------
# Stage 0: Survey
# ---------------------------------------------------------------------------

def _render_survey(output_dir: str, scan: dict) -> None:
    ri_dir = os.path.join(output_dir, "related_info")
    log_dir = os.path.join(output_dir, "literature_survey_log")
    if not (os.path.isdir(ri_dir) or os.path.isdir(log_dir)):
        return

    st.subheader("Stage 0: Literature Survey")
    _show_file("Difficulty Evaluation",
               os.path.join(ri_dir, "difficulty_evaluation.md"), output_dir)
    _show_file("Related Work",
               os.path.join(ri_dir, "related_work.md"), output_dir)
    _show_file("Survey Error",
               os.path.join(ri_dir, "error_literature_survey.md"), output_dir,
               as_code=True)
    _show_file("Survey Log (tail)",
               os.path.join(log_dir, "AUTO_RUN_LOG.txt"),
               output_dir, as_code=True, tail=True)


# ---------------------------------------------------------------------------
# Stage 1: Attempt → Revision → Proof tree
# ---------------------------------------------------------------------------

def _proof_label(proof: dict, is_current: bool) -> str:
    if is_current:
        return f"Proof {proof['num']} — current"
    if proof["detailed_verification"]:
        return f"Proof {proof['num']} — detailed verified"
    if proof["structural_verification"]:
        return f"Proof {proof['num']} — structural verified"
    if proof["proof_md"]:
        return f"Proof {proof['num']} — written"
    return f"Proof {proof['num']} — empty"


def _render_proof(proof: dict, output_dir: str, is_current: bool) -> None:
    label = _proof_label(proof, is_current)
    rel = _file_link(proof["dir"], output_dir)
    with st.expander(f"{label}  `{rel}/`", expanded=is_current):
        c1, c2, c3 = st.columns(3)
        c1.markdown(_badge(proof["proof_md"], "Proof"))
        c2.markdown(_badge(proof["structural_verification"], "Structural"))
        c3.markdown(_badge(proof["detailed_verification"], "Detailed"))

        _show_file("Proof",
                   os.path.join(proof["dir"], "proof.md"), output_dir)
        _show_file("Prover Response",
                   os.path.join(proof["dir"], "prover_response.md"), output_dir)
        _show_file("Scratchpad",
                   os.path.join(proof["dir"], "scratchpad.md"), output_dir)
        _show_file("Structural Verification",
                   os.path.join(proof["dir"], "structural_verification.md"), output_dir)
        _show_file("Detailed Verification",
                   os.path.join(proof["dir"], "detailed_verification.md"), output_dir)
        _show_file("Regulator Decision",
                   os.path.join(proof["dir"], "regulator_decision.md"), output_dir)
        for name in proof["error_files"]:
            _show_file(name.replace(".md", "").replace("_", " ").title(),
                       os.path.join(proof["dir"], name),
                       output_dir, as_code=True)


def _render_revision(revision: dict, output_dir: str,
                     current_revision: int | None,
                     current_proof: int | None) -> None:
    is_current_rev = (current_revision is not None
                      and current_revision == revision["num"])
    rel = _file_link(revision["dir"], output_dir)

    label = f"Revision {revision['num']}"
    if is_current_rev:
        label += " — current"
    elif revision["proofs"]:
        label += f" — {len(revision['proofs'])} proof(s)"

    with st.expander(f"{label}  `{rel}/`", expanded=is_current_rev):
        if revision["decomposition_yaml"]:
            _show_file("Decomposition YAML",
                       revision["decomposition_yaml"], output_dir,
                       as_code=True)
        if revision["decomposer_response"]:
            _show_file("Decomposer Response",
                       revision["decomposer_response"], output_dir)
        if not revision["proofs"]:
            st.caption("No proofs yet.")
            return
        for proof in revision["proofs"]:
            is_current_proof = (
                is_current_rev
                and current_proof is not None
                and current_proof == proof["num"]
            )
            _render_proof(proof, output_dir, is_current_proof)


def _render_attempt(attempt: dict, output_dir: str,
                    state: dict) -> None:
    is_current = (state["current_attempt"] is not None
                  and state["current_attempt"] == attempt["num"])

    n_rev = len(attempt["revisions"])
    label = f"Attempt {attempt['num']}"
    if is_current:
        label += f" — current ({state['state_label'] or 'in progress'})"
    elif n_rev:
        label += f" — {n_rev} revision(s)"

    rel = _file_link(attempt["dir"], output_dir)
    with st.expander(f"{label}  `{rel}/`", expanded=is_current):
        if not attempt["revisions"]:
            st.caption("No revisions yet.")
            return
        for revision in attempt["revisions"]:
            _render_revision(
                revision, output_dir,
                state["current_revision"] if is_current else None,
                state["current_proof"] if is_current else None,
            )


def _render_decomposition_tree(scan: dict, output_dir: str) -> None:
    if not (scan["attempts"]
            or os.path.isdir(decomp_root(output_dir))):
        return

    st.subheader("Stage 1: Decomposition Loop")

    state = scan["decomposition_state"]
    if not scan["attempts"]:
        st.caption("Decomposition directory exists but no attempts have been written yet.")
    else:
        for attempt in scan["attempts"]:
            _render_attempt(attempt, output_dir, state)

    decomp_dir = decomp_root(output_dir)
    _show_file("Decomposition Log (tail)",
               os.path.join(decomp_dir, "log.txt"), output_dir,
               as_code=True, tail=True)
    _show_file("Plan History",
               os.path.join(decomp_dir, "plan_history.md"), output_dir)


# ---------------------------------------------------------------------------
# Final outputs
# ---------------------------------------------------------------------------

def _render_final(output_dir: str, scan: dict) -> None:
    st.subheader("Final Outputs")
    if scan["final_proof"].strip():
        proof_path = os.path.join(output_dir, "proof.md")
        rel = _file_link(proof_path, output_dir)
        with st.expander(f"Final Proof  `{rel}`", expanded=scan["pipeline_complete"]):
            st.markdown(scan["final_proof"])
    _show_file("Proof Effort Summary",
               os.path.join(output_dir, "proof_effort_summary.md"),
               output_dir, expanded=scan["pipeline_complete"])
    _show_file("Summary Error",
               os.path.join(output_dir, "error_proof_effort_summary.md"),
               output_dir, as_code=True)
    if scan["failure_analysis"].strip():
        rel = _file_link(
            os.path.join(decomp_root(output_dir), "failure_analysis.md"),
            output_dir,
        )
        with st.expander(f"Failure Analysis  `{rel}`", expanded=True):
            st.markdown(scan["failure_analysis"])
    _show_file("Summary Log (tail)",
               os.path.join(output_dir, "summary_log", "AUTO_RUN_LOG.txt"),
               output_dir, as_code=True, tail=True)
    _show_file("Token Usage",
               os.path.join(output_dir, "TOKEN_USAGE.md"),
               output_dir)


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def render_progress(output_dir: str, run_active: bool = False) -> dict:
    """Render the full progress view and return the scan dict."""
    scan = scan_progress(output_dir)

    if not scan["exists"]:
        if run_active:
            st.info("Starting pipeline...")
        else:
            st.info("Output directory does not exist yet. Click **Run** to start.")
        return scan

    smoke = render_smoke_test(output_dir, run_active)
    if not smoke["finished"]:
        return scan
    if not smoke["ok"]:
        return scan

    _render_run_config(output_dir)
    _render_stage_indicator(scan)
    _render_metrics(scan)
    _render_status_and_history(output_dir)
    _render_survey(output_dir, scan)
    _render_decomposition_tree(scan, output_dir)
    _render_final(output_dir, scan)

    return scan
