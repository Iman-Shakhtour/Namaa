from __future__ import annotations

import hashlib
import json
import shutil
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = (ROOT / "output").resolve()
DEST = (OUTPUT / "Namaa-website-update-20260919").resolve()
ZIP_PATH = OUTPUT / "Namaa-website-update-20260919.zip"


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def main() -> None:
    if DEST.parent != OUTPUT or DEST.name != "Namaa-website-update-20260919":
        raise RuntimeError(f"Unsafe destination: {DEST}")
    if DEST.exists():
        shutil.rmtree(DEST)
    DEST.mkdir(parents=True)

    for name in ("index.html", "README.md", "DELIVERY.md", "favicon.ico", "apple-touch-icon.png"):
        shutil.copy2(ROOT / name, DEST / name)
    for name in ("assets", "css", "js"):
        shutil.copytree(ROOT / name, DEST / name)
    review = DEST / "review"
    review.mkdir()
    shutil.copy2(OUTPUT / "update-20260919-review" / "qa.json", review / "qa.json")

    files = []
    for path in sorted(item for item in DEST.rglob("*") if item.is_file()):
        files.append({
            "path": path.relative_to(DEST).as_posix(),
            "bytes": path.stat().st_size,
            "sha256": digest(path),
        })
    (DEST / "MANIFEST.json").write_text(
        json.dumps({"package": DEST.name, "files": files}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    if ZIP_PATH.exists():
        ZIP_PATH.unlink()
    with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(item for item in DEST.rglob("*") if item.is_file()):
            archive.write(path, Path(DEST.name) / path.relative_to(DEST))
    with zipfile.ZipFile(ZIP_PATH) as archive:
        bad = archive.testzip()
        if bad:
            raise RuntimeError(f"Corrupt archive entry: {bad}")
        names = archive.namelist()
        if any("/tmp/" in name or "/output/" in name for name in names):
            raise RuntimeError("Internal working files leaked into the package")

    print(json.dumps({
        "folder": str(DEST),
        "zip": str(ZIP_PATH),
        "zipBytes": ZIP_PATH.stat().st_size,
        "entries": len(names),
    }, indent=2))


if __name__ == "__main__":
    main()
