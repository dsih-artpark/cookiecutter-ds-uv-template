import os
import subprocess
import datetime
import yaml

def run_cmd(cmd, silent=False):
    try:
        if silent:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            subprocess.run(cmd, shell=True, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def ensure_git_repo():
    if not os.path.exists(".git"):
        print("🔧 Git repository not found. Initializing git...")
        if run_cmd("git init"):
            print("✅ Git repository initialized.")
        else:
            print("⚠️ Git init failed. Please initialize git manually.")
    else:
        print("✅ Git repository found.")

def install_dependencies():
    print("📦 Installing project dependencies using `uv sync`...")
    if run_cmd("uv sync"):
        print("✅ Dependencies installed.")
    else:
        print("⚠️ Failed to install dependencies. Please run `uv sync` manually.")

def update_config_created_date():
    config_path = os.path.join(os.getcwd(), "config.yaml")
    config = {}
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            config = yaml.safe_load(f) or {}

    if "created" not in config:
        config["created"] = datetime.datetime.now().strftime("%Y-%m-%d")
        with open(config_path, "w") as f:
            yaml.safe_dump(config, f)
        print("🗓️  Added project creation date to config.yaml.")

def print_final_instructions():
    project_dir_name = os.path.basename(os.getcwd())
    print(f"""
    🎉 Project setup complete! Here’s how to get started:

    1. Change directory into your project (if you aren’t already):
        cd {project_dir_name}

    2. Activate your virtual environment:
        On Linux/macOS: source .venv/bin/activate
        On Windows:    .\\.venv\\Scripts\\activate

    3. Install Git hooks for automatic linting and formatting on commit:
        pre-commit install

    4. To add packages, use:
        uv add <package_name>

    5. To run scripts, use:
        uv run python <script.py>

    Happy modelling! 🚀
    """)


def main():
    print("🚀 Setting up your new project...")
    ensure_git_repo()
    install_dependencies()
    update_config_created_date()
    print_final_instructions()

if __name__ == "__main__":
    main()