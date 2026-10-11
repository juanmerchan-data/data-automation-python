# 📊 Automating Financial Data Cleaning & Executive Reporting (Python & Pandas)

## 📌 Business Case
Small and medium businesses often waste hours manually cleaning raw CSV or Excel files containing duplicate entries, formatting inconsistencies, negative quantities, and unformatted monetary values.

## 💡 Solution
This automated Python data pipeline takes messy transactional data and performs automated data cleaning, normalization, and executive visualization in seconds.

### Key Features:
- **Data Normalization:** Strips unwanted spaces and formats currency strings into float types.
- **Deduplication & Validation:** Removes duplicate records and filters out invalid or negative quantity rows.
- **Calculated Metrics:** Automatically computes transaction totals and aggregates net sales by product.
- **Executive Visual Dashboard:** Generates a high-resolution horizontal bar chart displaying revenue distribution across products.

## 🛠️ Tech Stack & Libraries
- **Language:** Python 3
- **Data Manipulation:** `pandas`
- **Data Visualization:** `matplotlib`

## 📁 Repository Structure
- `ventas_desordenadas.csv`: Raw, uncleaned input data.
- `limpieza_automatica.py`: Python script performing data cleaning and ETL pipeline.
- `reporte_ventas_limpio.csv`: Cleaned output dataset.
- `generar_dashboard.py`: Script generating the executive visual chart.
- `dashboard_ventas.png`: High-resolution visual chart output.

## 🚀 How to Run Locally

1. Clone the repository:
```bash
git clone https://github.com/juanmerchan-data/data-automation-python.git
cd data-automation-python
```

2. Install dependencies:
```bash
pip install pandas matplotlib
```

3. Run the cleaning script:
```bash
python limpieza_automatica.py
```

4. Generate the visual dashboard:
```bash
python generar_dashboard.py
```

---
*Created by Juan Diego Merchan | Data Automation & Python Analytics Specialist*