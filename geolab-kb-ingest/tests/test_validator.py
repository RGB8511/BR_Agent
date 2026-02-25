"""Tests for the validator module using real package data."""

from __future__ import annotations

import json
import os
from pathlib import Path

from geolab_kb_ingest.validator import validate_all, validate_package


class TestValidatePackage:
    def test_valid_package(self, sample_package):
        errors = validate_package(sample_package)
        assert errors == [], f"Unexpected errors: {errors}"

    def test_missing_file(self, tmp_path):
        """A directory with no files should report missing files."""
        errors = validate_package(tmp_path)
        assert len(errors) == 5  # all 5 required files missing

    def test_equation_count_mismatch(self, sample_package, tmp_path):
        """Copy a package but alter equation_count in manifest."""
        import shutil
        pkg = tmp_path / "test-pkg"
        shutil.copytree(sample_package, pkg)
        # Alter manifest
        manifest_path = pkg / "_manifest.json"
        with open(manifest_path, encoding="utf-8") as f:
            manifest = json.load(f)
        manifest["equation_count"] = 999
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(manifest, f)
        errors = validate_package(pkg)
        assert any("Equation count mismatch" in e for e in errors)


class TestValidateAll:
    def test_all_packages_valid(self, packages_dir):
        results = validate_all(packages_dir)
        if results:
            for pkg, errors in results.items():
                print(f"\n{pkg}:")
                for e in errors:
                    print(f"  - {e}")
        assert results == {}, f"Validation errors found in {len(results)} package(s)"

    def test_counts_all_packages(self, packages_dir):
        """Should discover all 32 packages."""
        manifests = list(packages_dir.rglob("_manifest.json"))
        assert len(manifests) == 32
