import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

df = pd.read_csv('reporte_ventas_limpio.csv')
ventas_por_producto = df.groupby('Producto')['Total_Venta'].sum().sort_values(ascending=True)

fig, ax = plt.subplots(figsize=(8, 5))
barras = ax.barh(ventas_por_producto.index, ventas_por_producto.values, color='#1f77b4', edgecolor='black')

ax.set_title('Ingresos Totales por Producto (USD)', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Ventas ($)', fontsize=11)
ax.set_ylabel('Producto', fontsize=11)

for bar in barras:
    width = bar.get_width()
    ax.text(width + 50, bar.get_y() + bar.get_height()/2, f'${width:,.2f}', 
            va='center', ha='left', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('dashboard_ventas.png', dpi=300)
print("📈 Dashboard generado y guardado como 'dashboard_ventas.png'")