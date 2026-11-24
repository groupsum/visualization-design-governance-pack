"""Inspect the installed pack identity."""

from ssot_pack_visualization_design import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:visualization-design"
print(metadata["origin"]["id"])
