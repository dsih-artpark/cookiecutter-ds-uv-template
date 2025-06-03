# Reproducible Data Science Project Template in Python

## Prerequisites

You will need:

- [Python ≥ 3.9](https://www.python.org/downloads/)
- [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/installation.html)
- [`uv`](https://github.com/astral-sh/uv)

Install them using pip:

```bash
pip install cookiecutter uv
```

## Installation

Create a new project from this template by running:

```bash
cookiecutter https://github.com/dsih-artpark/cookiecutter-ds-uv-template.git
```

## Best Practices for Reproducible Data Science Experiments

- **Version Control Everything:** Use Git to track changes not only in code but also in configuration files (`config.yaml`) and notebooks.
- **Single Source of Truth for Configuration:** Maintain one `config.yaml` file at the project root, which defines datasets, models, outputs, and experiment parameters. Load this config consistently in all code and notebooks.
- **Isolated Environments:** Use `uv` to create and manage a Python virtual environment per project, ensuring dependencies are isolated and reproducible.
- **Lock Dependencies:** Always use `uv`'s lock file to freeze exact package versions for future reproducibility.
- **Code and Notebooks Separation:** Keep core logic inside the `src/` package, while using notebooks primarily for exploration, experimentation, and reporting.
- **Naming and Versioning:** Use clear, descriptive filenames and directory structures that include semantic versioning and timestamps. For example, name files like `data_ingestion_raw_v1.0.ipynb` or organize models by version folders such as `models/random_forest/v1.2/`. Store dataset, model, and parameter versions centrally in a `config.yaml` to maintain reproducibility and traceability.
- **Dataset Version Tracking:** Clearly specify the dataset ID and version used for each experiment within the notebook or configuration.
- **Experiment Metadata and Logging:** Include creation timestamps and descriptive notes within configuration files or dedicated metadata logs for each experiment. This helps track when, how, and why experiments were run, supporting exact reproducibility over time.
- **Linting and Formatting:** Use tools like `ruff` integrated via `pyproject.toml` to maintain code quality and consistency.
- **Document Usage:** Maintain a clear `README.md` that explains how to setup, run, and extend the project to onboard collaborators quickly.

## Documentation Guidelines

- **Write Documentation in Markdown:**  
  All project documentation should be written in Markdown (`.md`) files. Place these files in the `docs/` directory, following the structure defined in `mkdocs.yml`.
- **MkDocs is Enabled:**  
  This project comes pre-configured with [MkDocs](https://www.mkdocs.org/) and the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme. You can build and serve the documentation locally with:
  ```bash
  mkdocs serve
  ```
  This will start a local server where you can preview your documentation.
- **Organize by Topic:**  
  Create new Markdown files for each major topic or section (e.g., `data/dataset-description.md`, `analysis/methodology.md`). Update the `nav` section in `mkdocs.yml` to include new pages.
- **Use Markdown Features:**  
  You can use all standard Markdown features, as well as advanced formatting like code blocks, tables, admonitions, and math equations (LaTeX) thanks to the enabled extensions.
---

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.