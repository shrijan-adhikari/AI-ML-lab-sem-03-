# AI/ML Lab Semester 03

This repository contains the practical exercises and experiments for the AI/ML lab coursework for Semester 3. It includes Jupyter notebooks focused on core machine learning and data science workflows, along with supporting datasets.

## Folder structure

- `experiment-01.ipynb` — Experiment 1 notebook
- `experiment-02.ipynb` — Experiment 2 notebook
- `experiment-03.ipynb` — Experiment 3 notebook
- `experiment-04.ipynb` — Experiment 4 notebook
- `data/` — Input datasets and supporting files used by the experiments
- `.venv/` — Local virtual environment for project dependencies

## Getting started

1. Open the project folder in VS Code or your preferred Python environment.
2. Activate the virtual environment:
   - Windows PowerShell:
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
   - Command Prompt:
     ```cmd
     .\.venv\Scripts\activate.bat
     ```
3. Install any required dependencies if needed:
   ```bash
   pip install jupyter notebook numpy pandas matplotlib scikit-learn
   ```
4. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
5. Open any of the experiment notebooks and run the cells sequentially.

## Notes

- The notebooks are intended for learning and experimentation in AI/ML concepts.
- Keep the `data/` folder intact because the experiments may reference files from it by relative path.
- If a notebook fails because a dependency is missing, install the package in the active virtual environment and rerun the notebook.

## Suggested workflow

- Review the experiment notebook in order.
- Understand the objective, dataset, and model logic before running cells.
- Save outputs and notes for each experiment as needed.

## License

This project is for academic and learning purposes.
