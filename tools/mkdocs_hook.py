"""Hook do MkDocs: regenera docs/assets/escopo.js antes de cada build, serve ou gh-deploy."""
import subprocess, sys
from pathlib import Path

def on_pre_build(config):
    root = Path(config["config_file_path"]).resolve().parent
    subprocess.run([sys.executable, str(root / "tools" / "gen_escopo.py"), str(root)], check=True)
