# Exercise 3 - Iris dataset analysis

Exploratory analysis of the Iris dataset (150 flowers, 3 species) with pandas and seaborn.

## How to run

From the `codigo/` folder:

```bash
python3 -m venv .venv            # only if .venv is not there yet
source .venv/bin/activate
pip install -r requirements.txt
cd ejercicio3_iris
python main.py
```

Pick an option in the menu (5 = all the charts). The images are saved in `graficos/`:

| File | Chart |
|---|---|
| `1_histogramas.png` | Histogram of each feature by species |
| `2_pairplot.png` | `sns.pairplot()` coloured by species |
| `3_heatmap.png` | Correlation heatmap |
| `4_violines.png` | Violin plot of each feature by species |

The data is in `iris.csv` and it is loaded with `pandas.read_csv()`.
