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