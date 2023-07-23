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

    indice_base = dataframe[dataframe["Fecha"] == dataframe["Fecha"].max()]["INDICE"].values[0]
    dataframe[variable_real] = (dataframe[variable]  * indice_base / dataframe["INDICE"])

    dataframe_agrupado = dataframe[['Fecha', variable, variable_real]].copy()
    dataframe_agrupado = dataframe_agrupado.groupby('Fecha').sum()[[variable, variable_real]].reset_index()

    figsize=(7, 4)
    fig, ax = plt.subplots(figsize=figsize)

    ax.plot(dataframe_agrupado['Fecha'], dataframe_agrupado[variable], label=variable)
    ax.plot(dataframe_agrupado['Fecha'], dataframe_agrupado[variable_real], label=variable_real)
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
    1. Toma una combinacion de columnas
    2. Sumas la columnas que queremos verificar (ventas)
    3. Crea un df intermedio donde guardar combinaciones donde las ventas en el tiempo estudiado son mayores que 0
    4. hace inner join para quedarse sólo con combinaciones con valor > 0
    """
    
    import pandas as pd
    
    dfc = df.copy()
    nulos_combinacion = dfc.groupby(cols_combina)[col_buscar_vacio].sum().reset_index()
    ventas_ok = nulos_combinacion[nulos_combinacion[col_buscar_vacio] > 0][['ID','Subrubro']].copy()
    
    return pd.merge(left=dfc, right=ventas_ok, how='inner', on=cols_combina, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=None, indicator=False, validate=None)
    

def crear_diferencia_porcentual(data, variable, periodo):
    """
    Crea una diferencia porcentual en la variable teniendo en cuenta un periodo
    
    data = data
    variable = variable sobre la cual hacer diferencia porcentual
    periodo = periodo de tiempo sobre el cual hacer diferencia porcentual.
              Solo puede asumir 6 valores:  1 (Monthly)
                                            2 (Bimonthly)
                                            3 (Quarterly)
                                            4 (Four-monthly/Quadrimestral)
                                            6 (Semiannual)
                                           12 (Yearly)
    """
    import numpy as np

    if periodo == 1:
        prefijo = "M"
    elif periodo == 2:
        prefijo = "B"
    elif periodo == 3:
        prefijo = "Q"
    elif periodo == 4:
        prefijo = "F"
    elif periodo == 6:
        prefijo = "S"
    elif periodo == 12:
        prefijo = "Y"

    variable_diferencia = f"{prefijo}_pct_{variable}"

    data[variable_diferencia] = data.groupby(['ID', 'Subrubro'])[variable].pct_change(periods=periodo)

    subset_mask = ((data[variable_diferencia] == np.inf) & (data.groupby(['ID', 'Subrubro'])['Dato_original'].shift(periodo) == 0)) | (data['Dato_original'] == 0)

    data.loc[subset_mask, variable_diferencia] = np.nan


def graficar_var(data, sr, time):
    """
    Crea 4 plots de ventas y comisiones, separados según modelo y no modelo
    
    data = data
    sr = subrubro
    time = periodo de tiempo de interés
           Solo puede asumir 2 valores: 'F' (Four-monthly/Quadrimestral)
                                        'Y' (Yearly)
    """

    import matplotlib.pyplot as plt
    import numpy as np

    subrub = data[data['Subrubro'] == sr].copy()
    subrub_mod = subrub[subrub['Modelo'] == 1]
    subrub_nomod = subrub[subrub['Modelo'] == 0]
    subrub_mod = subrub_mod.T
    subrub_nomod = subrub_nomod.T

    if time == 'F':
        piv = np.arange('2019-05', '2022-07', dtype='datetime64[M]')
        sub = 'Intercuatrimestral'
        ven_mod = subrub_mod.iloc[42:80, :]
        ven_nomod = subrub_nomod.iloc[42:80, :]
        com_mod = subrub_mod.iloc[4:42, :]
        com_nomod = subrub_nomod.iloc[4:42, :]
    elif time == 'Y':
        piv = np.arange('2020-01', '2022-07', dtype='datetime64[M]')
        sub = 'Interanual'
        ven_mod = subrub_mod.iloc[110:140, :]
        ven_nomod = subrub_nomod.iloc[110:140, :]
        com_mod = subrub_mod.iloc[80:110, :]
        com_nomod = subrub_nomod.iloc[80:110, :]

    fig, axs = plt.subplots(2, 2, figsize=(50, 20))

    fig.suptitle(f"{sr} - {sub}", fontsize='x-large')

    ###### Ventas
    axs[0, 0].set_ylabel(r'$\Delta$Ventas')
    axs[0, 0].set_title(f'Modelos (n={len(subrub_mod.columns)})')
    axs[0, 0].plot(piv, ven_mod, label=subrub_mod.columns,  marker='o')#, ls=' ')
    axs[0, 0].set_xlabel('Fecha')

    axs[0, 1].set_ylabel(r'$\Delta$Ventas')
    axs[0, 1].set_title(f'No modelos (n={len(subrub_nomod.columns)})')
    axs[0, 1].plot(piv, ven_nomod, label=subrub_nomod.columns, ls=' ',  marker='o')
    axs[0, 1].set_xlabel('Fecha')

    ###### Comision
    axs[1, 0].set_ylabel(r'$\Delta$Comision')
    axs[1, 0].set_title(f'Modelos (n={len(subrub_mod.columns)})')
    axs[1, 0].plot(piv, com_mod, label=subrub_mod.columns,  marker='o')#, ls=' ')
    axs[1, 0].set_xlabel('Fecha')

    axs[1, 1].set_ylabel(r'$\Delta$Comision')
    axs[1, 1].set_title(f'No modelos (n={len(subrub_nomod.columns)})')
    axs[1, 1].plot(piv, com_nomod, label=subrub_nomod.columns, ls=' ',  marker='o')
    axs[1, 1].set_xlabel('Fecha')

    plt.show()


def graficar_var_zoom(data, sr, time, ven_liminf=None, ven_limsup=None, com_liminf=None, com_limsup=None):
    """
    Crea 2 plots de ventas y comisiones no modelo (pero siguiendo los límites de los modelo)
    
    data = data
    sr = subrubro
    time = periodo de tiempo de interés
           Solo puede asumir 2 valores: 'F' (Four-monthly/Quadrimestral)
                                        'Y' (Yearly)
    ven_liminf = indica el límite inferior del eje "y" para ventas (es opcional)
    ven_limsup = indica el límite superior del eje "y" para ventas (es opcional)
    com_liminf = indica el límite inferior del eje "y" para comision (es opcional)
    com_limsup = indica el límite superior del eje "y" para comision (es opcional)
    """

    import matplotlib.pyplot as plt
    import numpy as np

    subrub = data[data['Subrubro'] == sr].copy()
    subrub_mod = subrub[subrub['Modelo'] == 1]
    subrub_nomod = subrub[subrub['Modelo'] == 0]
    subrub_mod = subrub_mod.T
    subrub_nomod = subrub_nomod.T

    if time == 'F':
        piv = np.arange('2019-05', '2022-07', dtype='datetime64[M]')
        sub = 'Intercuatrimestral'
        ven_mod = subrub_mod.iloc[42:80, :]
        ven_nomod = subrub_nomod.iloc[42:80, :]
        com_mod = subrub_mod.iloc[4:42, :]
        com_nomod = subrub_nomod.iloc[4:42, :]
    elif time == 'Y':
        piv = np.arange('2020-01', '2022-07', dtype='datetime64[M]')
        sub = 'Interanual'
        ven_mod = subrub_mod.iloc[110:140, :]
        ven_nomod = subrub_nomod.iloc[110:140, :]
        com_mod = subrub_mod.iloc[80:110, :]
        com_nomod = subrub_nomod.iloc[80:110, :]

    if ven_liminf is None:
        ven_liminf = np.min(ven_mod.min())
    if ven_limsup is None:
        ven_limsup = np.max(ven_mod.max())
    if com_liminf is None:
        com_liminf = np.min(com_mod.min())
    if com_limsup is None:
        com_limsup = np.max(com_mod.max())

    # Hago zoom sobre el rango de los modelos, pero para los no modelo
    fig, axs = plt.subplots(1, 2, figsize=(50, 10))

    fig.suptitle(f"{sr} - {sub}", fontsize='x-large')

    ###### Ventas
    axs[0].set_ylabel(r'$\Delta$Ventas')
    axs[0].set_title(f'No modelos (n={len(subrub_nomod.columns)})')
    axs[0].plot(piv, ven_nomod, label=subrub_nomod.columns, ls=' ',  marker='o')
    axs[0].set_xlabel('Fecha')
    axs[0].set_ylim(ven_liminf, ven_limsup)

    ###### Comision
    axs[1].set_ylabel(r'$\Delta$Comision')
    axs[1].set_title(f'No modelos (n={len(subrub_nomod.columns)})')
    axs[1].plot(piv, com_nomod, label=subrub_nomod.columns, ls=' ',  marker='o')
    axs[1].set_xlabel('Fecha')
    axs[1].set_ylim(com_liminf, com_limsup)

    plt.show()