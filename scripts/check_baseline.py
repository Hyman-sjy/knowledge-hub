"""Verify immutable imported documents against the retained ZIP and manifest."""

import hashlib
import json
from pathlib import Path, PurePosixPath
import stat
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def safe_relative(value):
    path = PurePosixPath(value)
    if not value or path.is_absolute() or ".." in path.parts or "\\" in value:
        raise ValueError(f"Unsafe relative path: {value}")
    return path


def verify_baseline(root=ROOT):
    errors = []
    try:
        manifest = json.loads((root / "docs/sources/MANIFEST.json").read_text(encoding="utf-8"))
        if manifest["schema_version"] != 1:
            raise ValueError("Unsupported manifest schema")
        if manifest["baseline_root"] != "docs/baselines/v1.1":
            raise ValueError("Unexpected baseline directory")
        if manifest["archive_prefix"] != "quality-knowledge-hub-v1.1/":
            raise ValueError("Unexpected archive prefix")
        baseline = root / manifest["baseline_root"]

        def verify_bytes(label, data, record):
            if len(data) != record["bytes"] or hashlib.sha256(data).hexdigest() != record["sha256"]:
                errors.append(f"Size or SHA-256 mismatch: {label}")

        originals = {}
        for key in ("archive", "independent_prompt"):
            record = manifest[key]
            path = root / safe_relative(record["path"])
            data = path.read_bytes()
            verify_bytes(record["path"], data, record)
            originals[key] = data

        records = {}
        for record in manifest["files"]:
            path = str(safe_relative(record["path"]))
            if path in records or not path.endswith(".md"):
                raise ValueError(f"Duplicate or non-Markdown manifest path: {path}")
            records[path] = record
        actual = {str(p.relative_to(baseline).as_posix()) for p in baseline.rglob("*") if p.is_file()}
        if actual != set(records):
            errors.append(f"Baseline file set mismatch: missing={sorted(set(records)-actual)}, extra={sorted(actual-set(records))}")
        if any(p.is_symlink() for p in baseline.rglob("*")):
            errors.append("Symlink in baseline")

        with zipfile.ZipFile(root / manifest["archive"]["path"]) as archive:
            members = {}
            prefix = manifest["archive_prefix"]
            for info in archive.infolist():
                safe_relative(info.filename)
                if not info.filename.startswith(prefix) or info.is_dir() or stat.S_ISLNK(info.external_attr >> 16):
                    raise ValueError(f"Invalid archive member: {info.filename}")
                relative = info.filename[len(prefix):]
                safe_relative(relative)
                if relative in members or info.file_size > 1_000_000:
                    raise ValueError(f"Duplicate or oversized member: {relative}")
                members[relative] = info
            if sum(i.file_size for i in members.values()) > 10_000_000:
                raise ValueError("Archive exceeds intake size limit")
            if set(members) != set(records):
                errors.append("Archive and manifest file sets differ")
            for relative in sorted(set(members) & set(records)):
                data = archive.read(members[relative])
                data.decode("utf-8")
                verify_bytes(relative, data, records[relative])
                path = baseline / relative
                if path.is_file() and path.read_bytes() != data:
                    errors.append(f"Imported content differs from ZIP: {relative}")
            if archive.read(prefix + "CODEX_EXECUTION_PROMPT.md") != originals["independent_prompt"]:
                errors.append("Independent prompt differs from archived prompt")
        historical = sum(p.startswith("version-history/v1.0-baseline/") for p in records)
        expected = {"markdown_total": 74, "v1_1_current": 43, "v1_0_history": 31}
        actual_counts = {"markdown_total": len(records), "v1_1_current": len(records)-historical, "v1_0_history": historical}
        if manifest["counts"] != expected or actual_counts != expected:
            errors.append(f"Unexpected document counts: {actual_counts}")
        if manifest["independent_prompt"]["matches_archive"] is not True:
            errors.append("Manifest prompt comparison must be true")
    except (OSError, ValueError, KeyError, TypeError, zipfile.BadZipFile) as exc:
        errors.append(f"Baseline verification failed: {exc}")
    return errors


if __name__ == "__main__":
    failures = verify_baseline()
    if failures:
        raise SystemExit("\n".join(failures))
    print("PASS: retained ZIP, independent prompt and 74 unchanged documents (43 current + 31 historical).")
