"""Generate deterministic SSOT manifests from the JSON-compatible YAML templates."""

import argparse
import hashlib
import json
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "src" / "ssot_pack_visualization_design"


def render(directory, version):
    entries = []
    for path in sorted(directory.glob("*.yaml")):
        payload = path.read_bytes()
        document = json.loads(payload)
        entry = {key: document[key] for key in ("id", "number", "slug", "title", "status")}
        entry.update(
            filename=path.name,
            target_path=f".ssot/{directory.name}/{path.name}",
            sha256=hashlib.sha256(payload).hexdigest(),
            origin="extension-pack",
            reservation_owner="extension-pack:visualization-design-governance-pack",
            immutable=True,
            minimum_schema_version=document["schema_version"],
            introduced_in=version,
            supersedes=document["supersedes"],
            superseded_by=document["superseded_by"],
            status_notes=[],
        )
        if directory.name == "specs":
            entry["kind"] = document["spec_kind"]
        entries.append(entry)
    return (json.dumps(entries, indent=2) + "\n").encode("utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    version = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))["project"]["version"]
    for name in ("adr", "specs"):
        directory = PACKAGE / "templates" / name
        path = directory / "manifest.json"
        expected = render(directory, version)
        if args.check:
            if not path.is_file() or path.read_bytes() != expected:
                raise SystemExit(f"Outdated manifest: {path}")
        else:
            path.write_bytes(expected)


if __name__ == "__main__":
    main()
