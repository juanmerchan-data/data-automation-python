import pandas as pd

def procesar_reporte_ventas(archivo_entrada, archivo_salida):
    print("🔄 Procesando y limpiando datos...")
    
    # 1. Cargar datos
    df = pd.read_csv(archivo_entrada)
    
    # 2. Limpieza de duplicados
    df = df.drop_duplicates()
    
    # 3. Limpieza de texto (eliminar espacios extra)
    df['Producto'] = df['Producto'].str.strip()
    
    # 4. Formatear precios (quitar signo $ y convertir a flotante)
    df['Precio_Unitario'] = df['Precio_Unitario'].str.replace('$', '').astype(float)
    
    # 5. Manejo de valores nulos o inconsistentes
    df['Cantidad'] = pd.to_numeric(df['Cantidad'], errors='coerce').fillna(1)
    df = df[df['Cantidad'] > 0]  # Filtrar cantidades inválidas/negativas
    
    # 6. Cálculo de Total por Transacción
    df['Total_Venta'] = df['Cantidad'] * df['Precio_Unitario']
    
    # 7. Filtrar solo pagos completados
    df_completado = df[df['Estado_Pago'] == 'Completado']
    
    # 8. Guardar archivo limpio
    df_completado.to_csv(archivo_salida, index=False)
    
    # 9. Resumen Ejecutivo en Consola
    total_ingresos = df_completado['Total_Venta'].sum()
    producto_top = df_completado.groupby('Producto')['Cantidad'].sum().idxmax()
    
    print("✅ ¡Procesamiento Exitoso!")
    print(f"📊 Total Ingresos Procesados: ${total_ingresos:,.2f} USD")
    print(f"🏆 Producto más Vendido: {producto_top}")
    print(f"💾 Reporte limpio guardado en: {archivo_salida}")

if __name__ == "__main__":
    procesar_reporte_ventas('ventas_desordenadas.csv', 'reporte_ventas_limpio.csv')