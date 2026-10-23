# The Method — Operating Manual for Research Agents

**Purpose.** This document lets a fresh agent — one with no conversation
history — run the research methodology nearly agentically. Read it before
starting work, follow it while working, update the tree when done.

**Scope.** General to all research threads (prime program, CCC, others).
Examples are drawn from the prime-sieve-geometry decision tree, where the
method matured.

---

## 1. The core loop

The work proceeds as a **numbered decision tree**. Each node records:
date, question, options considered, decision, evidence, status
(open / closed / forked).

A verdict earned by theorem or clean computation is **permanent** and
forces the next move. The elimination is deterministic; designing the
discriminating test is the creative part.

*Example: 11g failed → 11h was forced; 11h proved the bare operator
trivial → 11i was forced; the three closed the xp branch → testing the
mechanism itself was forced.*

## 2. Epistemic labels

Every claim gets exactly one label:

- **exact theorem** — proved, no numerics needed
- **computationally verified** — computed live, rerunnable, with controls
- **conjectural** — precise statement, no proof yet
- **heuristic** — suggestive, not yet precise

Labels sit alongside the tree: labels say what kind of thing each claim
is, the tree says where the exploration has been. Never build on a claim
whose label cannot carry the weight.

## 3. Triadic forks

At each decision node, fork **three ways**:

1. **The claim** — the positive test.
2. **Its polar opposite** — the negation or alternative.
3. **The null** — the control.

The polar-opposite leg is load-bearing: without it you learn "it works";
with it you learn *what* works.

*Example: 11l (prime-log geometry) / 11n (random geometry — the polar
opposite) / GUE + shuffled (the null). The opposite leg turned 11l from
"prime mechanism" into "fully geometric mechanism."*

## 4. Backward touch

When a branch dies **or** succeeds, go back and touch the prior nodes it
bears on. Re-examine their interpretation in the new light; record what
changed and what didn't. **The tree is not append-only.**

*Example: the interference theorem reframed 11l's verdict — mechanism
confirmed, pattern explained — without changing 11p's gate verdict.
The 11n/11o root-finder correction bounded 11l's regime without
falsifying it.*

## 5. Branching identifiers

Every node carries two lines:

- **Why it ends here** — the primary objective completed (the verdict).
  No branch "just stops" or trails off.
- **Its own chain** — what the completion continues as: consequences,
  follow-ups, spawned questions. A terminated branch is **resumable
  inventory**, not a grave. Record enough that a future agent can pick
  the chain up without re-deriving it.

*Example: the xp branch ended because all three tested constructions
were exhausted (11h by exact analysis); its chain is that the
exhaustion forced the mechanism-first turn — its death is 11l's birth.*

## 6. Working rules

- **Derive, don't invent.** Observe in the work's own forms, combos,
  layouts, and vocabulary. Never insert a private taxonomy about the
  work. Formalize only in its terms, and only when asked.
- **Observe before asking.** Run the computation; look at the answer;
  make the observation. Do not lead with sequences of clarifying
  questions.
- **"Proceed" means decide and execute fully.** Do not route decisions
  back for confirmation. Handle the whole sequence the tree dictates.
- **Options are sequential, never menus.** One node explored at a time,
  in the order the tree dictates.
- **Compute live, never from memory.** Self-contained rerunnable
  scripts; captured output; plain-words verdicts including honest
  negatives. Never quote results from weights.
- **Do not guard against failures upfront.** Let them occur, catch
  them, absorb them into the method. What matters is that the method
  catches its own errors and continues stronger.
- **Controls are mandatory.** Every positive result needs its polar
  opposite and its null, run the same way.
- **Density-scaled root-finding.** When root-finding a spectrum whose
  density varies, scale the scan step with the density — a fixed step
  silently misses close pairs. Cross-check counts AND probe results
  until both stabilize.
- **Report plainly, same exchange.** Verdict first, weak points
  included, no sycophancy. Own instrument caveats unprompted.

## 7. Records to maintain

- **DECISION_TREE.md** — the numbered nodes (the tree itself).
- **Dead-end ledger** — each dead end with its failure mechanism.
  Dead ends to avoid are as valuable as open avenues.
- **Theorem notes** — when a mechanism is found, state what it
  predicts *before* computing (the "winner before it wins" rule).
- **This file** — if the method itself learns something new, record
  it here.

## 8. The shape to hold in mind

> The sieve never tests for primality — it eliminates what's composite,
> and what remains is prime. The decision tree never argues for a
> truth — it eliminates what's false, and what remains is the verdict.

The method and the subject are the same shape. That is not a metaphor;
it is why the method works on this subject.

---

*Written 2026-10-06. Drawn explicitly from the prime program's
decision tree so a subagent handed this file can run the method
without the conversation that produced it.*
