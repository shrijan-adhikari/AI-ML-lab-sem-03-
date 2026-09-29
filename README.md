# AI/ML Lab Semester 03

This repository contains the practical exercises and experiments for the AI/ML lab coursework for Semester 3. It includes Jupyter notebooks focused on core machine learning and data science workflows, along with supporting datasets.

## Folder structure and file purposes

- `experiment-01.ipynb` — Introduction to dataset exploration. Used to load CSV files, inspect rows/columns, and understand the basic structure and statistics of the data using methods such as `df.describe()` and `df.info()`.
- `experiment-02.ipynb` — Missing value analysis and data cleaning. Used to detect null entries, understand their impact, and prepare the dataset for further processing.
- `experiment-03.ipynb` — Exploratory data analysis and preprocessing workflow. Used for visualizing patterns, checking relationships in the dataset, and applying model-selection or preprocessing steps before training.
- `experiment-04.ipynb` — Customer churn prediction and business insight project. Used to train classification/regression models on the telecom dataset to predict churn and analyze business-related insights.
- `data/` — Contains raw and processed datasets used by the experiments. These files provide the input data for analysis, training, testing, and predictions.
- `data/telco_data.csv` — Telecom customer dataset used in the churn prediction project. It includes customer attributes and churn-related information.
- `data/train.csv` — Training split of the dataset used to train machine learning models.
- `data/test.csv` — Testing split used to evaluate model performance on unseen data.
- `data/Predictions.csv` — Output file containing model predictions generated from the trained model.
- `data/car_dataset.data` — A car-related dataset used for data analysis and model experimentation.
- `data/dataset_1.data` — Additional dataset file used for practice, experimentation, and general data analysis tasks.
- `.venv/` — Local Python virtual environment for installing and managing project dependencies.
- `README.md` — Project documentation explaining the purpose, files, and workflow of the lab exercises.

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
