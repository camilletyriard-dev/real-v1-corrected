#!/usr/bin/env python3
"""Copy the corrected REAL v1 task files over an installed agisdk.

agisdk scores episodes by reading its own task JSONs, so a correction only takes
effect once the files on disk are the corrected ones.

    python apply.py --dry-run     report what would change, write nothing
    python apply.py               back up, then apply
    python apply.py --restore     put the backed-up originals back
"""

import argparse
import filecmp
import json
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "tasks"
BACKUP = HERE / ".backup-v1-tasks"
REL = Path("REAL") / "browsergym" / "webclones" / "v1" / "tasks"


def find_agisdk(explicit: Path | None) -> Path:
    if explicit is not None:
        target = explicit / REL if (explicit / REL).is_dir() else explicit
        if not target.is_dir():
            sys.exit(f"no v1 task directory at {target}")
        return target
    try:
        import agisdk
    except ImportError:
        sys.exit("agisdk is not importable here; activate the right environment "
                 "or pass --agisdk-path")
    target = Path(agisdk.__file__).resolve().parent / REL
    if not target.is_dir():
        sys.exit(f"agisdk found at {target.parent}, but no v1 task directory in it")
    return target


def compare(target: Path) -> tuple[list[str], list[str]]:
    """(files that differ, files present here but missing there)."""
    differing, missing = [], []
    for path in sorted(SRC.glob("*.json")):
        installed = target / path.name
        if not installed.exists():
            missing.append(path.name)
        elif not filecmp.cmp(path, installed, shallow=False):
            differing.append(path.name)
    return differing, missing


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--agisdk-path", type=Path, default=None,
                    help="package root or the v1/tasks directory itself")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--restore", action="store_true")
    args = ap.parse_args()

    target = find_agisdk(args.agisdk_path)

    if args.restore:
        if not BACKUP.is_dir():
            sys.exit(f"no backup at {BACKUP}; nothing to restore")
        for path in sorted(BACKUP.glob("*.json")):
            shutil.copy2(path, target / path.name)
        print(f"restored {len(list(BACKUP.glob('*.json')))} original files to {target}")
        return

    differing, missing = compare(target)
    if missing:
        sys.exit(f"{len(missing)} task files are missing from {target}: "
                 f"{', '.join(missing[:5])}... this does not look like a v1 install")

    print(f"target: {target}")
    print(f"{len(differing)} of {len(list(SRC.glob('*.json')))} files would change")
    for name in differing:
        task_id = name[:-5]
        print(f"  {task_id}")
    if args.dry_run:
        return
    if not differing:
        print("already up to date")
        return

    BACKUP.mkdir(exist_ok=True)
    for name in differing:
        if not (BACKUP / name).exists():
            shutil.copy2(target / name, BACKUP / name)
    for path in sorted(SRC.glob("*.json")):
        shutil.copy2(path, target / path.name)
    print(f"\napplied. originals backed up to {BACKUP}")
    print("undo with: python apply.py --restore")


if __name__ == "__main__":
    main()
