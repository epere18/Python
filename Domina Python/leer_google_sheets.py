import pandas as pd

def leer_sheet_publica(sheet_id, sheet_name):
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    df = pd.read_csv(url)
    print("Primeras filas del archivo")
    print(df.head())

    df["Neto_Gravado"] = df["Neto_Gravado"].str.replace(",",".").astype(float)
    df["REP_Costo_s_Iva"] = df["REP_Costo_s_Iva"].str.replace(",",".").astype(float)
    

    filtrado = df[
        (df["REP_Costo_s_Iva"]>1000000) &
        (df["Unidad_Negocio"] == "Repuestos")
        ]
    print("\nFiltrado (montos > 1 millón y Unidad_Negocio == 'Repuestos'):")
    print("-----------------------------------------------------------------")
    print(filtrado)

    sumatoria_por_usuario = filtrado.groupby("Usuario.1")["REP_Costo_s_Iva"].sum().reset_index()

    sumatoria_por_usuario = sumatoria_por_usuario.sort_values(by="REP_Costo_s_Iva", ascending=False)
    print("\nSumatoria acumulada por Usuario.1:")
    print("-----------------------------------------------------------------")
    print(sumatoria_por_usuario)

sheet_id = "1DOhZxZLDi2MVq9YOTE2D-E3wZc4KRVQcTdwWjDM1wiY"
sheet_name = "FACTURACION_Febrero2024"
leer_sheet_publica(sheet_id, sheet_name)