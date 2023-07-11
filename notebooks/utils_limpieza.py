## Funciones auxiliares de limpieza

def limpiar_basic(df, cols_drop):
    """
    Elimina las columnas que aparezcan en la lista
    
    'df' = dataframe para dropear
    'cols_drop' = lista de nombres de columns para dropear
    """
    df_limpio = df.drop(columns=cols_drop)
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
    
    df[columna] = df[columna].apply(lambda x: x if x in subcat_has_model else fill_otros)
    return df


def anonimizar():
    """
    Función para anonimizar los datos de las columnas que nos parezcan sensibles
    [dani] Sugiero que esta función tome una df y una lista de columnas,
    y a esa lista de columnas le aplique un hash.
    """
    return print('función vacía')