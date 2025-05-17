import plotly.express as px
import pandas as pd

# Datos de ejemplo
df = pd.DataFrame({
    'Ciudad': ['Buenos Aires', 'Córdoba', 'Rosario', 'Mendoza'],
    'Población': [3000000, 1300000, 1200000, 1100000]
})

# Gráfico de barras
fig = px.bar(df, x='Ciudad', y='Población', title="Población por ciudad")
fig.show()
