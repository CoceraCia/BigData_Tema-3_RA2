# Exercise 4 - Sales dashboard with Power BI

`Ventas_Electronica_PowerBI_2022_2026.xlsx` is the Excel the teacher shared in the course forum: sales of 10 electronic
products from 01/01/2022 to 26/10/2026 (1,722 rows). Columns: `Fecha`, `Producto`, `Cantidad Vendida`, `Precio Unitario`
and `Ingresos` (= Cantidad Vendida * Precio Unitario).

Heads up: the file has two sheets with the same data. `Ventas` uses Excel formulas and `Ventas_Valores` has plain values.
Load **only** the table `TablaVentasValores` or every number will be doubled.

## Steps in Power BI Desktop

1. **Get data → Excel workbook** → `Ventas_Electronica_PowerBI_2022_2026.xlsx` → tick only `TablaVentasValores` → *Load*.
2. Check in the *Data* view that `Fecha` is a Date and the numbers are decimal/whole numbers.
3. Add a calculated column for the year (*Table tools → New column*):
   ```DAX
   Año = YEAR(TablaVentasValores[Fecha])
   ```
   And two measures:
   ```DAX
   Total Cantidad = SUM(TablaVentasValores[Cantidad Vendida])
   Total Ingresos = SUM(TablaVentasValores[Ingresos])
   ```
4. **a) Table**: *Matrix* visual → Rows: `Producto`, Columns: `Año`, Values: `Total Cantidad`.
5. **b) Line chart**: X axis: `Año`, Y axis: `Total Ingresos`. (Set the X axis type to *Categorical* so it shows 2022, 2023…)
6. **c) Heatmap**: copy the matrix from step 4 and in *Format → Cell elements → Background color* turn on the colour scale (light = few sales, dark = many).
7. **d) Filter**: *Slicer* visual with `Producto` (style *Dropdown* or *Tile*). Selecting a product filters the other visuals.
8. Add a title and save the report as `dashboard_ventas.pbix`.

## Expected results (to check the visuals)

Units sold per product and year:

| Producto | 2022 | 2023 | 2024 | 2025 | 2026* | Total |
|---|---|---|---|---|---|---|
| Altavoz Bluetooth | 315 | 273 | 315 | 324 | 253 | 1480 |
| Auriculares | 235 | 351 | 419 | 612 | 437 | 2054 |
| Impresora | 132 | 110 | 243 | 163 | 133 | 781 |
| Monitor | 168 | 197 | 283 | 334 | 340 | 1322 |
| Portátil | 159 | 262 | 368 | 313 | 270 | 1372 |
| Ratón | 226 | 319 | 329 | 382 | 324 | 1580 |
| Smartphone | 287 | 350 | 366 | 433 | 388 | 1824 |
| Smartwatch | 175 | 255 | 327 | 320 | 374 | 1451 |
| Tablet | 140 | 176 | 150 | 275 | 331 | 1072 |
| Teclado | 131 | 247 | 401 | 384 | 302 | 1465 |
| **Total** | 1968 | 2540 | 3201 | 3540 | 3152 | 14401 |

Total revenue per year: 2022 540,262.07 € · 2023 731,582.95 € · 2024 930,490.53 € · 2025 999,540.48 € · 2026* 949,010.58 €

\* 2026 only goes up to 26 October.
