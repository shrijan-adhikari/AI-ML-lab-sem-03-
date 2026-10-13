from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

DATA_PATH = Path(__file__).resolve().parent / "data" / "stock_data.csv"
MODEL_PATH = Path(__file__).resolve().parent / "prediction.pickle"


def load_stock_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    if df.empty:
        raise ValueError(f"Dataset is empty: {path}")

    # The CSV has a date-like first column and multiple stock columns.
    # Rename the first column to a usable name and use it as the index.
    df = df.rename(columns={df.columns[0]: "Date"})
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.dropna(subset=["Date"]).set_index("Date")

    # Use the first stock series as the prediction target.
    target_col = df.columns[0]
    df[target_col] = pd.to_numeric(df[target_col], errors="coerce")
    df = df.dropna(subset=[target_col]).copy()

    return df, target_col


def prepare_features(series: pd.Series):
    dates = np.arange(len(series)).reshape(-1, 1)
    values = series.to_numpy().reshape(-1, 1)
    return dates, values


def main():
    df, target_col = load_stock_data(DATA_PATH)
    prices = df[target_col]

    # Plot the original data.
    plt.figure(figsize=(12, 5))
    plt.plot(df.index, prices, label=f"{target_col} price history")
    plt.title(f"Stock Price History | {target_col}")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.tight_layout()
    plt.show()

    x, y = prepare_features(prices)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"Model: Linear Regression")
    print(f"Target column: {target_col}")
    print(f"Mean Absolute Error: {mae:.4f}")
    print(f"R^2 Score: {r2:.4f}")

    with MODEL_PATH.open("wb") as pickle_file:
        import pickle

        pickle.dump(model, pickle_file)

    plt.figure(figsize=(12, 5))
    plt.plot(df.index, prices, color="green", linewidth=1, label="Actual Price")
    plt.plot(df.index[x_test.ravel()], model.predict(x_test), color="blue", linewidth=3, label="Predicted Price")
    plt.title(f"Linear Regression | {target_col} Prediction")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
