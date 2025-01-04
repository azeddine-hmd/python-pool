from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def normalize_nums(val: str) -> float | None:
    """convert values that have suffix of k, M, B back to million"""
    if 'k' in val:
        return float(val.replace('k', '')) / 1000
    elif 'M' in val:
        return float(val.replace('M', ''))
    elif 'B' in val:
        return float(val.replace('B', '')) * 1000
    raise AssertionError(f"val {val} could not be normalized")
    return None


def population_plotting(df: pd.DataFrame, c1: str, c2: str):
    """display plot of  two countries population"""
    try:
        # data
        c1_df = df[df["country"] == c1]
        c2_df = df[df["country"] == c2]
        years = [str(year) for year in range(1800, 2051)]
        pop1 = c1_df[years].map(normalize_nums) \
            .to_numpy().flatten()
        pop2 = c2_df[years].map(normalize_nums) \
            .to_numpy().flatten()

        # plotting
        plt.plot(years, pop1, label=c1)
        plt.plot(years, pop2, label=c2)
        plt.xlabel("Year")
        plt.xticks(['1800', '1840', '1880', '1920',
                    '1960', '2000', '2040'])
        plt.ylabel("Population")
        popticks = \
            [int(max(max(pop1), max(pop2)) // 8) * i for i in range(1, 9)]
        yticks = \
            [pop for i, pop in enumerate(popticks) if i % 2 == 0 and i != 7]
        plt.yticks(yticks, [str(pop) + "M" for pop in yticks])
        plt.title("Population Projections")
        plt.legend(loc="lower right")
        plt.show()

    except KeyboardInterrupt:
        pass
    except AssertionError as e:
        print("AssertionError:", e)
    except Exception as e:
        print("Error:", e)


def main():
    """display plot of two countries"""

    df = load("population_total.csv")

    try:
        assert df is not None, "failed to load data"
    except AssertionError as e:
        print("AssertionError:", e)
        return

    population_plotting(df, "Morocco", "Algeria")


if __name__ == "__main__":
    main()
