import json
import unittest
from importlib.resources import files

from ssot_pack_visualization_design import load_pack_manifest, read_packaged_document_text


class VisualizationDesignPackTests(unittest.TestCase):
    def setUp(self):
        self.manifest = load_pack_manifest()
        self.evidence = {
            item["id"]: item
            for item in json.loads(
                files("ssot_pack_visualization_design").joinpath("evidence.json").read_text(encoding="utf-8")
            )["sources"]
        }

    def test_portable_immutable_documents(self):
        metadata = self.manifest["metadata"]
        self.assertEqual(metadata["origin"]["id"], "pack:visualization-design")
        self.assertFalse(metadata["trust"]["trusted_by_default"])
        documents = self.manifest["documents"]
        self.assertEqual(len(documents["adr"]), 4)
        self.assertEqual(len(documents["spec"]), 7)
        adrs = {entry["id"] for entry in documents["adr"]}
        seen = set()
        for kind, entries in documents.items():
            for entry in entries:
                self.assertTrue(entry["immutable"])
                # The pack contract verifies the manifest hash on read.
                doc = json.loads(read_packaged_document_text(kind, entry["filename"]))
                self.assertEqual(doc["id"], entry["id"])
                self.assertNotIn(doc["id"], seen)
                seen.add(doc["id"])
                if kind == "spec":
                    self.assertTrue(set(doc["adr_ids"]) <= adrs)
                    self.assertTrue(doc["requirements"])
                    self.assertTrue(doc["evidence_expectations"])
                self.assertEqual(
                    doc["authority_sources"],
                    [self.evidence[key]["url"] for key in doc["evidence_refs"]],
                )

    def test_evidence_preserves_strength_and_limits(self):
        self.assertEqual(self.evidence["tufte"]["kind"], "design-principle")
        self.assertEqual(self.evidence["bertin"]["kind"], "design-framework")
        self.assertEqual(self.evidence["cleveland-mcgill"]["kind"], "controlled-experiment")
        self.assertEqual(self.evidence["heer-bostock"]["kind"], "replication-and-extension")
        for row in self.evidence.values():
            for field in ("method", "finding", "limits"):
                self.assertTrue(row[field].strip())
            self.assertTrue(row["url"].startswith("https://"))


if __name__ == "__main__":
    unittest.main()
