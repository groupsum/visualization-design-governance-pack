"""Find a specification and its downstream path in the installed manifest."""

from ssot_pack_visualization_design import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:visualization-data-and-coverage"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2001-visualization-data-and-coverage.yaml"
