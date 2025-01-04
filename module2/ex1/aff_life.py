from matplotlib import pyplot as plt
from load_csv import load
import pandas as pd


def plot_life_expectancy(df: pd.DataFrame, country: str):
    """plot life expectancy for a country"""
    try:
        country_data = df[df["country"] == country]
        years_cols = df.columns[1:]
        life_expectancy_rows = country_data.iloc[0, 1:]
    except Exception as e:
        print(e)

    plt.plot(years_cols, life_expectancy_rows)
    plt.xlabel("Year")
    plt.xticks(["1800", "1840", "1880", "1920",
                "1960", "2000", "2040", "2080"])
    plt.ylabel("Life Expectancy")
    plt.title(f"{country} Life Exceptancy Projections")
    plt.show()


def main():
    """loading and plotting the life expectancy for Morocco"""

    df = load("life_expectancy_years.csv")

    try:
        assert df is not None, "failed to load data"
    except AssertionError as e:
        print("AssertionError:", e)
        return

    plot_life_expectancy(df, "Morocco")


if __name__ == "__main__":
    main()
