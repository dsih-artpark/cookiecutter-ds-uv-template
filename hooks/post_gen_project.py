import datetime
import os
import subprocess

import yaml

print("Project created successfully!")

# Optional: install packages automatically
subprocess.run("uv sync", shell=True, check=True)

# Add creation date to config.yaml
project_dir = os.getcwd()
config_path = os.path.join(project_dir, "config.yaml")

config = {}
if os.path.exists(config_path):
    with open(config_path, "r") as f:
        config = yaml.safe_load(f) or {}

if "created" not in config:
    config["created"] = datetime.datetime.now().strftime("%Y-%m-%d")

with open(config_path, "w") as f:
    yaml.safe_dump(config, f)

print("Creation date added to config.yaml")

print("Run the following commands to get started:")
print(f"  cd {os.path.basename(project_dir)}")
print("  source .venv/bin/activate on Linux/Mac  # or .\\.venv\\Scripts\\activate on Windows")
print(" uv add <package_name>  # to add a package")
print(" uv run python <script>  # to run a script")
print("Happy modelling! 🎉")