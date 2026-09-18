from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).parent
PROJECTS = [
    "knowledge-relay",
    "local-asset-navigator",
    "reconcile-agent",
    "packaging-preflight",
]

for project in PROJECTS:
    print(f"\n== {project} ==")
    subprocess.run([sys.executable, str(ROOT / project / "run.py")], check=True)

