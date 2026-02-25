"""Shared pytest fixtures for GeoLab KB Ingest tests."""

from __future__ import annotations

from pathlib import Path

import pytest

# Path to the real geolab_packages data (sibling of geolab-kb-ingest/)
PACKAGES_DIR = Path(__file__).resolve().parent.parent.parent / "geolab_packages"


@pytest.fixture
def packages_dir() -> Path:
    """Root path to geolab_packages/."""
    assert PACKAGES_DIR.exists(), f"Package data not found at {PACKAGES_DIR}"
    return PACKAGES_DIR


@pytest.fixture
def sample_package(packages_dir: Path) -> Path:
    """A single well-known package for testing."""
    pkg = packages_dir / "foundations" / "soil-classification"
    assert pkg.exists(), f"Sample package not found at {pkg}"
    return pkg


@pytest.fixture
def consolidation_package(packages_dir: Path) -> Path:
    pkg = packages_dir / "soil-mechanics" / "consolidation"
    assert pkg.exists()
    return pkg


@pytest.fixture
def sample_manifest(sample_package: Path) -> dict:
    import json
    with open(sample_package / "_manifest.json", encoding="utf-8") as f:
        return json.load(f)
