# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

def pregunta_01():
    ruta_docs = "docs"
    if not os.path.exists(ruta_docs):
        os.makedirs(ruta_docs)

    ruta_datos = os.path.join("files", "input", "shipping-data.csv")
    df_envios = pd.read_csv(ruta_datos)

    # Copia del DataFrame para el análisis de almacenes
    df_almacenes = df_envios.copy()
    plt.figure()
    conteo_almacenes = df_almacenes["Warehouse_block"].value_counts()

    conteo_almacenes.plot.bar(
        title="Envíos por almacén",
        xlabel="Bloque de almacén",
        ylabel="Cantidad de registros",
        color="tab:blue",
        fontsize=8,
    )

    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.savefig(os.path.join(ruta_docs, "shipping_per_warehouse.png"))

    # Copia del DataFrame para el análisis del modo de envío
    df_transporte = df_envios.copy()
    plt.figure()
    conteo_transporte = df_transporte["Mode_of_Shipment"].value_counts()

    conteo_transporte.plot.pie(
        title="Modo de Envío",
        wedgeprops={"width": 0.35},
        ylabel="",
        colors=["tab:blue", "tab:orange", "tab:green"],
    )

    plt.savefig(os.path.join(ruta_docs, "mode_of_shipment.png"))

    # Análisis de calificación del cliente
    df_calificaciones = df_envios.copy()
    plt.figure()

    df_calificaciones = (
        df_calificaciones[["Mode_of_Shipment", "Customer_rating"]]
        .groupby("Mode_of_Shipment")
        .describe()
    )

    df_calificaciones.columns = df_calificaciones.columns.droplevel()
    df_calificaciones = df_calificaciones[["mean", "min", "max"]]

    plt.barh(
        y=df_calificaciones.index.values,
        width=df_calificaciones["max"].values - 1,
        left=df_calificaciones["min"].values,
        height=0.9,
        color="lightgray",
        alpha=0.8,
    )

    colores_barras = [
        "tab:green" if promedio >= 3.0 else "tab:orange"
        for promedio in df_calificaciones["mean"].values
    ]

    plt.barh(
        y=df_calificaciones.index.values,
        width=df_calificaciones["mean"].values - 1,
        left=df_calificaciones["min"].values,
        color=colores_barras,
        height=0.5,
        alpha=1.0,
    )

    plt.title("Calificación Promedio de Clientes")
    plt.gca().spines["left"].set_color("gray")
    plt.gca().spines["bottom"].set_color("gray")
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)

    plt.savefig(os.path.join(ruta_docs, "average_customer_rating.png"))

    # Análisis de la distribución de peso de los envíos
    df_peso = df_envios.copy()
    plt.figure()

    df_peso.Weight_in_gms.plot.hist(
        title="Distribución del Peso de Envíos",
        color="tab:orange",
        edgecolor="white",
    )

    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)

    plt.savefig(os.path.join(ruta_docs, "weight_distribution.png"))
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
