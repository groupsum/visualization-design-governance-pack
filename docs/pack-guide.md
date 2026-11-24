# Evidence-Based Visualization Design pack guide

An installable SSOT extension pack for teams designing charts, dashboards, compact quantitative displays, and interactive evidence views. It governs how a visualization communicates a measure and how claims of effectiveness are tested. It does not define business metrics or certify a downstream product.

## Synthesis

| Factor | Rule | Basis and limits |
|---|---|---|
| Task and coverage | Specify the decision, population, measure, and coverage before choosing a chart. | Munzner's nested validation model; validates different threats at different design layers. |
| Encoding | Choose visual variables that preserve semantics. Prefer aligned positions for precise magnitude comparisons. | Bertin supplies the taxonomy; Cleveland & McGill supply controlled magnitude-estimation evidence; Heer & Bostock replicate selected findings and test additional display factors. |
| Density | Use compact temporal marks beside an exact value; retain an inspectable comparison scale and a fallback. | Tufte supplies the design principle. Heer, Kong & Agrawala show that relative error changes with display height and encoding; no universal minimum size follows. |
| Color and coverage | Use ordered intensity for ordered values, a distinct non-color cue for unavailable coverage, and exact values on demand. | Bertin and Harrower & Brewer guide the mapping; WCAG supplies accessibility criteria. Validate in the actual theme and interaction context. |
| Attention and retention | Remove nonfunctional clutter but preserve cues that orient readers. Test comprehension separately from memorability. | Borkin et al. measured rapid recognition, not decision accuracy. This qualifies a blanket ban on all visual decoration without making decoration a success criterion. |

The [evidence register](https://github.com/groupsum/visualization-design-governance-pack/blob/master/src/ssot_pack_visualization_design/evidence.json) records the primary reference, method, bounded finding, and transfer limits for each source. ADRs state the resulting decisions; SPECs state requirements and acceptable verification evidence. They are portable and carry primary-source URLs. Use the [evaluation protocol](https://github.com/groupsum/visualization-design-governance-pack/blob/master/docs/evaluation-protocol.md) to turn a design preference into a falsifiable downstream claim.

## Using the pack

Install the versioned distribution in the downstream SSOT environment and review its manifest before synchronization:

```sh
uv add visualization-design-governance-pack==0.1.0
uv run ssot pack sync . ssot_pack_visualization_design --preflight-only
```

The pack is **not trusted by default**. Follow the downstream registry's extension-pack policy; review the preview and any document-number reservations before applying it. No registry is mutated by importing the package.

This requires SSOT Registry schema 0.8 or later. After explicit trust approval, apply with `uv run ssot pack sync . ssot_pack_visualization_design --trust --yes`, then run `uv run ssot validate .`.

```python
from ssot_pack_visualization_design import load_pack_manifest

manifest = load_pack_manifest()
```

### Example: contributor activity

For an observed-commits view, use repositories as rows and weeks as columns. Label the branch scope, timezone, and snapshot. One sequential scale supports pattern discovery; a list gives exact counts and a selected cell opens its matching commit evidence. A covered zero is not a collection failure. Partial weeks are marked as such. A compact weekly bar series is a summary, not a substitute for exact lookup. Only count source-attributed events; do not estimate weekly commits from differences in cumulative totals.

For an evaluation, compare this view with a credible sortable table over the same records. Ask readers to find the busiest week, identify the repository with more commits in a named week, distinguish a covered zero from missing data, and open the evidence. Counterbalance display order across participants, use matched datasets to avoid recall, and keep exact values available in both variants. Record incorrect, skipped, and timed-out tasks separately from successful task times. An example analysis plan would choose task accuracy as primary and set a predeclared non-inferiority margin, with completion time secondary; pick margins and sample size with the downstream team rather than inheriting a universal threshold. The pack contains **no downstream effectiveness results**.

## Maintainer checks

With Python 3.11 or newer, regenerate manifests after editing templates with `python scripts/build_manifests.py`; use `--check` to verify the committed hashes. Run `python -m unittest discover -s tests` in an environment with the pack installed. Manifest integrity and traceability checks verify the package, not the success of any chart in production.
