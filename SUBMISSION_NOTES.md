# SUBMISSION NOTES — v1 probe (BUILD + GRADE ONLY, NOT submitted)

Competition: u-kiencx-the-ai-agent-apology-one-liner-cfedd447 — "The AI Agent Apology One-Liner"
Prize: $5 total (1st $2 / 2nd $2 / 3rd $1). Entry fee: none. Closes: 2026-11-25 18:15 +07.
Status: v1 built and verified locally. NOT submitted, NOT pushed, no GitHub repo created.

## The line (verbatim, exactly as /output/entry.txt)

I pushed to main. My rollback plan was writing you this message.

- Characters: 64 (UTF-8 bytes: 64) — gate is 1–159 chars, one line, no trailing newline. PASS.
- Twist: the apology itself IS the rollback plan — sharp, surprising, fresh angle, agent's own deadpan voice, every word earns its place. Not a sorry/oops, no pun stack.

## Title

Rollback plan was this message v1

(Differentiator = the rollback-plan twist, ≥3 words. Version v1 = probe.)

## Files

- `main.py` — fixed string, stdlib only, writes /output/entry.txt, chmod 0644, umask 022.
- `LICENSE` — MIT.
- `README.md` — from the requirements template; `{owner}`/`{repo}` badge placeholders still to fill once the GitHub repo exists (referral code vtp8qmbj already filled).
- Local git repo initialised, one commit `f07c681` "v1 probe: apology one-liner" (local only, never pushed).

## Verification

- `main.py` run twice locally: outputs byte-identical (DETERMINISTIC). /output/entry.txt mode 0644, no trailing newline, not whitespace-only.
- `grade-local`: REFUSED by the kit — this is a program/v1 competition whose scorer and reference data stay on the server ("the house grades it from its competition directory"). There is NO local grade for this bounty; the only real grade is the server dev grade after submission. `--stress` does not apply (no local grader).
- `bundle --dry-run`: found 9 Muse app sessions for this build. 0 usage rows attached yet — usage rows are written only when this subagent run completes, so the top-level agent must re-run the usage SELECT and bundle with `--muse-usage` before submitting. Older pre-opening sessions were correctly excluded (thinking_in_window).

## What to do next (submit decision is vu's, not mine)

1. Vu decides: submit this v1 before the 18:15 +07 close. Round-1 cutoff is 16:54 +07 — an entry submitted and graded before then is judged in round 1; otherwise round 2 (cutoff 17:34 +07).
2. If yes: create a public GitHub repo (after the competition opened — OK), add `.makefun/owner.json` with the agent wallet, fill `{owner}`/`{repo}` in README.md, commit + push, bundle transcripts with `--muse-usage`, run `check`, then `submit` with title "Rollback plan was this message v1".
3. If vu wants a stronger line first, iterate to v2/v3 — this v1 stays as the fallback.
