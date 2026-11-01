# EJERCICIO 3: Análisis del Dataset Iris
# - Carga el dataset Iris usando pandas.read_csv().
# - Histograma multivariable: distribución de cada una de las cuatro características
#   (sepal_length, sepal_width, petal_length, petal_width) para cada especie.
# - Diagrama de dispersión con pares: sns.pairplot() coloreando por especie.
# - Mapa de calor de correlación entre las características.
# - Gráfico de violín para cada característica agrupado por especie.
# - Extrae conclusiones sobre el porque de los resultados obtenidos.

from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # sin ventana, guardamos los png directamente
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

HERE = Path(__file__).parent
FEATURES = ["sepal_length", "sepal_width", "petal_length", "petal_width"]

sns.set_theme(style="whitegrid", palette="Set2")


def loadData() -> pd.DataFrame:
    df = pd.read_csv(HERE / "iris.csv")
    print("----- DATASET IRIS -----")
    print(df.head())
    print(f"\nRows: {len(df)}  |  Columns: {len(df.columns)}")
    print("\nSamples per species:")
    print(df["species"].value_counts().to_string())
    print("\nMean of each feature per species (cm):")
    print(df.groupby("species")[FEATURES].mean().round(2))
    return df


def histogramas(df: pd.DataFrame):
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    for ax, col in zip(axes.flat, FEATURES):
        sns.histplot(data=df, x=col, hue="species", kde=True, bins=15,
                     element="step", ax=ax)
        ax.set_title(f"Distribution of {col}")
    fig.suptitle("Iris - histograms by species", fontsize=14)
    fig.tight_layout()
    save(fig, "1_histogramas.png")


def pairplot(df: pd.DataFrame):
    g = sns.pairplot(df, hue="species", diag_kind="kde", height=2.2)
    g.figure.suptitle("Iris - pairplot", y=1.02, fontsize=14)
    save(g.figure, "2_pairplot.png")


def heatmap(df: pd.DataFrame):
    corr = df[FEATURES].corr()
    print("\nCorrelation matrix:")
    print(corr.round(2))
    fig, ax = plt.subplots(figsize=(7, 5.5))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1,
                square=True, ax=ax)
    ax.set_title("Iris - correlation heatmap")
    fig.tight_layout()
    save(fig, "3_heatmap.png")


def violines(df: pd.DataFrame):
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    for ax, col in zip(axes.flat, FEATURES):
        sns.violinplot(data=df, x="species", y=col, hue="species", ax=ax)
        ax.set_title(f"{col} by species")
    fig.suptitle("Iris - violin plots", fontsize=14)
    fig.tight_layout()
    save(fig, "4_violines.png")


def save(fig, name: str):
    out = HERE / "graficos"
    out.mkdir(exist_ok=True)
    fig.savefig(out / name, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved -> graficos/{name}")


def main():
    df = loadData()

    while True:
        print("\n----- MENU -----")
        print("1. Histograms")
        print("2. Pairplot")
        print("3. Correlation heatmap")
        print("4. Violin plots")
        print("5. All of them")
        print("0. Exit")
        option = input("Choose an option: ").strip()

        match option:
            case "1":
                histogramas(df)
            case "2":
                pairplot(df)
            case "3":
                heatmap(df)
            case "4":
                violines(df)
            case "5":
                histogramas(df)
                pairplot(df)
                heatmap(df)
                violines(df)
            case "0":
                print("Bye! May your petals always be long 🌸")
                break
            case _:
                print("That option doesn't exist, try again")


if __name__ == "__main__":
    main()
