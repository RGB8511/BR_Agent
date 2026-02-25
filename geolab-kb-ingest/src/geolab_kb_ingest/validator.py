"""Package structure validation."""

from __future__ import annotations

import json
from pathlib import Path

REQUIRED_FILES = ["_manifest.json", "theory.md", "equations.json", "tables.json", "standards.md"]


def validate_package(package_dir: Path) -> list[str]:
    """Validate a single package directory. Returns list of error strings."""
    errors: list[str] = []

    # Check required files exist
    for fname in REQUIRED_FILES:
        if not (package_dir / fname).exists():
            errors.append(f"Missing file: {fname}")

    # Try to parse JSON files
    manifest = None
    manifest_path = package_dir / "_manifest.json"
    if manifest_path.exists():
        try:
            with open(manifest_path, encoding="utf-8") as f:
                manifest = json.load(f)
        except json.JSONDecodeError as e:
            errors.append(f"Invalid JSON in _manifest.json: {e}")

    eq_path = package_dir / "equations.json"
    equations = None
    if eq_path.exists():
        try:
            with open(eq_path, encoding="utf-8") as f:
                equations = json.load(f)
        except json.JSONDecodeError as e:
            errors.append(f"Invalid JSON in equations.json: {e}")

    tbl_path = package_dir / "tables.json"
    tables = None
    if tbl_path.exists():
        try:
            with open(tbl_path, encoding="utf-8") as f:
                tables = json.load(f)
        except json.JSONDecodeError as e:
            errors.append(f"Invalid JSON in tables.json: {e}")

    # Validate counts match manifest
    if manifest and equations is not None:
        expected = manifest.get("equation_count", 0)
        actual = len(equations)
        if expected != actual:
            errors.append(
                f"Equation count mismatch: manifest says {expected}, file has {actual}"
            )

    if manifest and tables is not None:
        expected = manifest.get("table_count", 0)
        actual = len(tables)
        if expected != actual:
            errors.append(
                f"Table count mismatch: manifest says {expected}, file has {actual}"
            )

    return errors


def validate_all(packages_dir: Path) -> dict[str, list[str]]:
    """Validate all packages. Returns {package_path: [errors]}.

    Also checks that all dependency IDs exist in the package set.
    """
    results: dict[str, list[str]] = {}

    # Discover packages
    package_dirs: list[Path] = []
    for manifest_path in sorted(packages_dir.rglob("_manifest.json")):
        package_dirs.append(manifest_path.parent)

    # Collect all package IDs
    all_ids: set[str] = set()
    manifest_map: dict[str, dict] = {}
    for pkg_dir in package_dirs:
        try:
            with open(pkg_dir / "_manifest.json", encoding="utf-8") as f:
                manifest = json.load(f)
            pkg_id = manifest.get("id", "")
            all_ids.add(pkg_id)
            manifest_map[str(pkg_dir)] = manifest
        except (json.JSONDecodeError, OSError):
            pass  # Will be caught in per-package validation

    # Validate each package
    for pkg_dir in package_dirs:
        key = str(pkg_dir.relative_to(packages_dir))
        errors = validate_package(pkg_dir)

        # Check dependencies exist (support both exact and suffix match,
        # since some packages use short-form IDs like "soil-mechanics.compaction"
        # while the full ID is "geotechnical.soil-mechanics.compaction")
        manifest = manifest_map.get(str(pkg_dir))
        if manifest:
            for dep_id in manifest.get("dependencies", []):
                found = dep_id in all_ids or any(
                    full_id.endswith(f".{dep_id}") for full_id in all_ids
                )
                if not found:
                    errors.append(f"Missing dependency: {dep_id}")

        if errors:
            results[key] = errors

    return results
