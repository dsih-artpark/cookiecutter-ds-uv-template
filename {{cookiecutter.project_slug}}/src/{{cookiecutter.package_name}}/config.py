from pathlib import Path

import yaml

# Default path: config.yaml in project root (two levels above this file)
DEFAULT_CONFIG_PATH = Path(__file__).parent.parent / "config.yaml"

def load_config(path: Path | str | None = None) -> dict:
    """Load YAML config from given path or default project root config.yaml."""
    if path is None:
        path = DEFAULT_CONFIG_PATH
    else:
        path = Path(path)
    with open(path, "r") as f:
        return yaml.safe_load(f)

# Optional: load on import for convenience
CONFIG = load_config()
