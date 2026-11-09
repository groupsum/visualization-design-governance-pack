# Downstream visualization evaluation

Use this protocol for a claim that a chart improves a task, not for routine screenshot approval. Store the completed record beside the downstream implementation and reference the applicable SPEC.

| Claim layer | Question | Evidence |
|---|---|---|
| Domain | Do readers need this comparison or decision? | Observe or interview representative users; document rejected questions and scope. |
| Data and task | Does the measure answer that question for the intended population? | Reconcile eligibility, aggregation, coverage, exact values and drill-down against independent source queries. |
| Encoding and interaction | Can users read and act on the display accurately? | Compare equivalent variants using controlled tasks, then test realistic workflows and accessible alternatives. |
| Implementation | Does the actual surface preserve the semantics and stay usable? | Render fixtures and check input parity, contrast, zoom, layout, and latency on supported devices. |

## Before the comparison

- Write a directional claim with a task, audience and comparator. Example: the grid helps developers locate their busiest week faster than a sortable table, without a meaningful loss of accuracy.
- Choose a primary outcome, decision margin, error definition, sample plan, and stopping rule. Use pilot work to calibrate difficulty and timing, not to declare success. Record secondary outcomes and how multiple comparisons will be handled.
- Freeze dataset, stimuli and expected answers. Give variants the same underlying data, labels, and equivalent access to exact values. Include sparse data, ties, outliers, zero and missing coverage. Randomize assignment or counterbalance within-participant order and use matched tasks to reduce carryover.
- Record screen sizes, input methods, participant familiarity, and permitted assistance. Avoid public disclosure of identifiable participant data.

## Analyze and decide

- Keep one row per anonymized participant/task attempt: variant, task and dataset IDs, order, correct/incorrect, time, timeout/abandonment and failure reason. For numerical estimates retain the estimate and answer in declared units.
- Report accuracy denominators, task failures, estimation error when relevant, and time for successful tasks alongside failure rates. Do not silently discard slow failures. Respect repeated measurements: use participant-level paired effects or participant-clustered uncertainty rather than treating every click as independent.
- Report effect estimates and intervals against the predeclared margin. If the result crosses the decision margin, label it inconclusive. Explain conflicting outcomes instead of averaging accuracy, time and recall into a single score.
- Record what the evidence supports, the tested conditions and transfer limits. A literature-based rationale is not a passed downstream trial. A rendering or accessibility pass is not an effectiveness result.

## Worked literature trace

Heer & Bostock's 2010 paper, [Experiment 1A, Figures 3–4](https://idl.cs.washington.edu/files/2010-MTurk-CHI.pdf#page=3), compared proportional-estimation judgments across encodings. It replicated the broad ordering of the tested spatial judgments and used bootstrap 95% intervals for log absolute error; position still outperformed length in the tested comparison. This is evidence for aligned position in a **magnitude-estimation task**, not proof that a specific contributor heatmap improves discovery.

Heer, Kong & Agrawala's [height comparison, Figures 8–9](https://hci.stanford.edu/publications/2009/heer-horizon-chi09.pdf) shows why compactness needs its own test: the relative error of the tested designs changed as chart height decreased. A downstream sparkline should be assessed at the smallest shipped size, with an exact-value alternative, rather than borrowing a universal pixel threshold from the study.
