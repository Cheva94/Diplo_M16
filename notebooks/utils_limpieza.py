# Funciones auxiliares de limpieza y preprocesamiento de los datos

def limpiar_basic(df, cols_drop):
    """
    Elimina las columnas que aparezcan en la lista
    
    'df' = dataframe para dropear
    'cols_drop' = lista de nombres de columns para dropear
    """
    df_limpio = df.drop(columns=cols_drop).copy()
    return df_limpio


def renombrar_elementos(df, columna:str, fill_otros:str):
    """
    Renombra a 'fill_otros' los elemntos de 'columna' que no tengo un MODELO

    df = dataframe
    columna = columna donde reemplazar elementos
    fill_otros = el nombre para renombrar los que no tengan MODELO
    """
    subcat_model_count = df.groupby(by=[columna])['MODELO'].sum()
    subcat_has_model = subcat_model_count[subcat_model_count>0].index.to_list()
    
    df_new = df.copy()
    df_new[columna] = df_new[columna].apply(lambda x: x if x in subcat_has_model else fill_otros)
    return df_new


def anonimizar(df, columna:str):
    """
    Función para anonimizar los datos de las columnas que nos parezcan sensibles

    df = dataframe
    columna = columna donde reemplazar elementos
    """

    print(f'Actualizando variable {columna}')
    dic = {}
    df_map = df.copy()
    
    valunico = df_map[columna].unique()
    porc10 = int(0.1 * len(valunico))
    prog = 0
    for v in range(len(valunico)):
        df_map[columna] = df_map[columna].replace({valunico[v]: v})
        dic.update({str(valunico[v]): v})

        if v % porc10 == 0:
            print(f'\t Progreso del {prog}%')
            prog += 10

    return df_map, dic


def indexar(dataframe, variable):
    """
    Indexa los valores de cierta variable siguiendo el IPC de Indec y tomando como base el máximo mes de la serie. 
    Crea una nueva variable llamada variable_real y plotea un gráfico con los resultados agregados por mes.
    
    dataframe = dataframe
    variable = variable a indexar
    """
    
    import matplotlib.pyplot as plt

    variable_real = f"{variable}_Real"

    indice_base = dataframe[dataframe["FECHA"] == dataframe["FECHA"].max()]["INDICE"].values[0]
    dataframe[variable_real] = (dataframe[variable]  * indice_base / dataframe["INDICE"])

    dataframe_agrupado = dataframe[['FECHA', variable, variable_real]].copy()
    dataframe_agrupado = dataframe_agrupado.groupby('FECHA').sum()[[variable, variable_real]].reset_index()

    figsize=(7, 4)
    fig, ax = plt.subplots(figsize=figsize)

    ax.plot(dataframe_agrupado['FECHA'], dataframe_agrupado[variable], label=variable)
    ax.plot(dataframe_agrupado['FECHA'], dataframe_agrupado[variable_real], label=variable_real)
    ax.set_xlabel('Fecha')
    ax.set_ylabel(variable)
    ax.set_title(f"{variable} vs {variable_real}")
    ax.legend()
    ax.tick_params(axis='x', rotation=45)

    plt.show()


def checkear_unicidad(dataframe, variable_objetivo, variable_granular_1, variable_granular_2=None, variable_granular_3=None, variable_granular_4=None):
    """
    Verificar si existen diferentes valores de variable_objetivo para un mismo variable_granular

    dataframe = dataframe
    variable_objetivo = variable sobre la cual se quiere indagar la unicidad
    variable_granular_1 = variable que indica la granularidad
    variable_granular_2 = variable que, en conjunto con la variable_granular_1, indica la granularidad (es opcional)
    variable_granular_3 = variable que, en conjunto con la variable_granular_1 y la variable_granular_2, indica la granularidad (es opcional)
    variable_granular_4 = variable que, en conjunto con la variable_granular_1, la variable_granular_2 y la variable_granular_3, indica la granularidad (es opcional)
    """
    
    if variable_granular_1 and not variable_granular_2:
        variable_granular = variable_granular_1
    elif variable_granular_1 and variable_granular_2 and not variable_granular_3:
        variable_granular = [variable_granular_1, variable_granular_2]
    elif variable_granular_1 and variable_granular_2 and variable_granular_3 and not variable_granular_4:
        variable_granular = [variable_granular_1, variable_granular_2, variable_granular_3]
    else:
        variable_granular = [variable_granular_1, variable_granular_2, variable_granular_3, variable_granular_4]

    conteo = dataframe.groupby(variable_granular)[variable_objetivo].nunique().copy()
    conteo_granular = conteo[conteo > 1]

    if conteo_granular.empty:
        print(f"Para cada {variable_granular} solo existe un valor de {variable_objetivo}.")
    else:
        print(f"Para algunos {variable_granular} se asignan diferentes valores de {variable_objetivo}:")
        print(conteo_granular.sort_values(ascending=False))


def graficar_modelo(dataframe, variable_corte):
    """
    Grafica el % de vendedores modelo para cierta variable de corte (entre paréntesis expone el número total de vendedores)

    dataframe = dataframe
    variable_corte = variable de corte
    """
    
    import matplotlib.pyplot as plt

    modelo_1 = dataframe[dataframe['Modelo'] == 1].drop_duplicates(subset=['ID', variable_corte]).copy()
    dataframe_1 = dataframe.drop_duplicates(subset=['ID', variable_corte]).copy()

    porcentaje_modelo_1 = modelo_1.fillna('Vacío').groupby(variable_corte)['Modelo'].count() / dataframe_1.fillna('Vacío').groupby(variable_corte)['Modelo'].count() * 100

    porcentaje_modelo_1_sorted = porcentaje_modelo_1.fillna(0).sort_values(ascending=True)

    cantidad = dataframe_1.fillna('Vacío').groupby(variable_corte)['Modelo'].count()

    plt.barh(porcentaje_modelo_1_sorted.index, porcentaje_modelo_1_sorted.values)
    plt.xlabel('Porcentaje de modelos')
    plt.ylabel(variable_corte)
    plt.title(f'Porcentaje de vendedores modelo según {variable_corte}')

    promedio_global = dataframe[dataframe['Modelo'] == 1].drop_duplicates(subset='ID').shape[0] / dataframe.drop_duplicates(subset='ID').shape[0] * 100
    plt.axvline(promedio_global, color='red', linestyle='--', label=f'Promedio Global: {promedio_global:.2f}%')
    plt.legend()

    for i, value in enumerate(porcentaje_modelo_1_sorted.values):
        plt.annotate(f'{value:.2f}% ({cantidad[porcentaje_modelo_1_sorted.index[i]]})', (value, porcentaje_modelo_1_sorted.index[i]), ha='left', va='center')

    plt.show()
    
    
def eliminar_combinacion_vacios(df, cols_combina=list, col_buscar_vacio=str):
    """
    1. Toma una combinacion de columnas> 0
    2. Sumas la columnas que queremos verificar (ventas)
    3. Crea un df intermedio donde guardar combinaciones donde las ventas en el tiempo estudiado son mayores que 0
    4. hace inner join para quedarse sólo con combinaciones con valor 
    """
    
    import pandas as pd
    
    dfc = df.copy()
    nulos_combinacion = dfc.groupby(cols_combina)[col_buscar_vacio].sum().reset_index()
    ventas_ok = nulos_combinacion[nulos_combinacion[col_buscar_vacio] > 0][['ID','Subrubro']].copy()
    
    return pd.merge(left=dfc, right=ventas_ok, how='inner', on=cols_combina, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=None, indicator=False, validate=None)
    