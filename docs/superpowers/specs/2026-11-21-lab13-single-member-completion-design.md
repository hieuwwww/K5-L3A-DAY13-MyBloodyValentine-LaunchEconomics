# Lab 13 Single-Member Completion Design

## Intent and why

Complete the LogiX-VN Launch Economics lab submission as far as the repository data and supplied instructions allow, while accurately reflecting that the learner is working alone. The goal is a runnable analysis and coherent, rubric-aligned submission without fabricating independent judgments, identity details, or a cross-team review.

## Goals

- Implement `src/lab13.py` for A1, A2, A3, A4, B1–B4, and D1; derive reported data results from the provided CSV files.
- Complete the cost, metrics, pilot, and launch documents with explicit `simulated` labels wherever `_simulated` inputs contribute.
- Use one-person role assignments and document solo-work limitations transparently.
- Run code, YAML, and submission consistency checks.

## Non-goals and anti-goals

- Do not invent the learner's name, student ID, class, email, GitHub identity, or repository URL.
- Do not represent reference error labels as two independently produced label sets or claim independent agreement.
- Do not fabricate a review of another team's submission or a second team member's contributions.
- Do not use “production” in the submitted reports.

## Constraints

- Preserve both CSV files and the starter file.
- Follow `RULES.md`, `RUBRIC.md`, `CHECKPOINTS.md`, `SUBMISSION.md`, and the detailed guide in `docs/`.
- AI may assist with implementation, but all numeric results must be computed from the provided data or shown calculations.
- Keep required submission filenames and distinguish measured trace values from simulated time estimates.

## Approaches considered

1. Complete only the code and quantitative sections: safest but leaves most rubric evidence incomplete.
2. Complete code, reports, and pilot while marking evidence that cannot honestly be supplied by one person: selected, because it maximizes useful completion without misrepresenting group work.
3. Fill every field as if a four-person group existed: rejected because it would fabricate independent labels, identities, and peer review.

## Design decisions

- Implement the existing starter interfaces in `src/lab13.py`; keep calculations reproducible and print checkpoint outputs.
- Populate the report templates from the supplied instructions and code output; state the methodological limitation for single-person error classification.
- Complete the pilot using the documented staff-randomized design and explicitly state its sample-size/power trade-off.
- Record the learner as sole contributor where identity is known; leave identity-dependent filenames/fields clearly pending rather than guessing.
- Leave cross-team peer grading pending until the target team's actual submission is available.

## Left to the learner

Supply full name, student ID, class, and any repository/team naming details; review and explain the calculations; perform an independent second labeling pass only if a genuine independent rater becomes available; and complete peer grading against the assigned team's real submission.
