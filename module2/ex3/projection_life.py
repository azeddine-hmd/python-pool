from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def plotting_le_gdp(le_df: pd.DataFrame, gdp_df: pd.DataFrame, year: str):
    """Plotting the gdp and life expectancy of the world"""

    try:
        # data
        gdp_sr = gdp_df[year]
        le_sr = le_df[year]

        # plot
        plt.scatter(gdp_sr, le_sr)
        plt.xlabel("Gross Domestic Product")
        plt.xscale("log")
        plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
        plt.ylabel("Life Expectancy")
        plt.title(year)
        plt.show()
    except KeyboardInterrupt:
        pass
    except AssertionError as e:
        print("AssertionError:", e)
    except Exception as e:
        print("Error:", e)


def main():
    """Plotting for GDP and Life expectancy for year 1900"""
    le_df = load("life_expectancy_years.csv")
    gdp_df = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

    try:
        assert le_df is not None and gdp_df is not None, "failed to load csv"
    except AssertionError as e:
        print("AssertionError:", e)

    plotting_le_gdp(le_df, gdp_df, "1900")


if __name__ == "__main__":
    main()
