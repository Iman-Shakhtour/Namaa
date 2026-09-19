from __future__ import annotations

import hashlib
import json
import shutil
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = (ROOT / "output").resolve()
DEST = (OUTPUT / "Namaa-design-cleanup").resolve()
ZIP_PATH = OUTPUT / "Namaa-design-cleanup.zip"
REVIEW_SOURCE = ROOT / "output" / "design-cleanup-review"

PROJECT_FILES = [
    "index.html",
    "README.md",
    "DELIVERY.md",
    "favicon.ico",
    "apple-touch-icon.png",
]
PROJECT_DIRS = ["assets", "css", "js"]
REVIEW_FILES = [
    "DESIGN-CLEANUP-REVIEW.md",
    "changed-files.json",
    "full-desktop-1440.png",
    "full-mobile-390.png",
    "responsive-qa.json",
    "interaction-qa.json",
    "static-qa.json",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    if DEST.parent != OUTPUT or DEST.name != "Namaa-design-cleanup":
        raise RuntimeError(f"Unsafe package target: {DEST}")
    if DEST.exists():
        shutil.rmtree(DEST)
    DEST.mkdir(parents=True)

    for relative in PROJECT_FILES:
        shutil.copy2(ROOT / relative, DEST / relative)
    for relative in PROJECT_DIRS:
        shutil.copytree(ROOT / relative, DEST / relative)

    review_dest = DEST / "review"
    review_dest.mkdir()
    for relative in REVIEW_FILES:
        shutil.copy2(REVIEW_SOURCE / relative, review_dest / relative)

    manifest = []
    for path in sorted(item for item in DEST.rglob("*") if item.is_file()):
        manifest.append({
            "path": path.relative_to(DEST).as_posix(),
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        })
    (DEST / "MANIFEST.json").write_text(
        json.dumps({"package": DEST.name, "files": manifest}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    if ZIP_PATH.exists():
        ZIP_PATH.unlink()
    with zipfile.ZipFile(ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(item for item in DEST.rglob("*") if item.is_file()):
            archive.write(path, Path(DEST.name) / path.relative_to(DEST))

    with zipfile.ZipFile(ZIP_PATH) as archive:
        bad = archive.testzip()
        if bad:
            raise RuntimeError(f"Corrupt archive entry: {bad}")
        names = archive.namelist()
        if any("/tmp/" in name or "/output/" in name for name in names):
            raise RuntimeError("Package includes internal working files")

    print(json.dumps({
        "folder": str(DEST),
        "zip": str(ZIP_PATH),
        "zipBytes": ZIP_PATH.stat().st_size,
        "entries": len(names),
    }, indent=2))


if __name__ == "__main__":
    main()
