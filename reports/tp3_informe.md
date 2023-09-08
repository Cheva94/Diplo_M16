# Diplomatura en ciencia de datos, aprendizaje automático y sus aplicaciones - Edición 2023 - FAMAF (UNC)

## Mentoría 16 - ¿Cómo identificar fuga de ventas? Inteligencia artificial aplicada al sector comercial.

### Explorando Patrones de Datos a través de Clustering (TP3)

**Integrantes:**
- Canalis, Patricio.
- Chevallier-Boutell, Ignacio José.
- Villarroel Torrez, Daniel.

**Mentores:**
- Gonzalez, Lucía
- Lahoz, Nahuel

---
# Estructura de las notebooks

### **`tp3_clustering1.ipynb`** - Parte 1: Preparación y análisis de los datos
* Contiene todos los pasos necesarios para la curación, partiendo desde el dataset crudo (cada registro es una transacción) hasta llegar al dataset pivoteado (cada registro es un vendedor único por subrubro).
* El dataset pivoteado contiene las variaciones porcentuales intercuatrimestrales e interanuales.
* Son los mismos pasos que hicimos para el tp2, más el paso nuevo de mapear valores a 0 (ver paso 9.).
* Además, contiene un análisis detallado del dataset resultante luego de la curación y antes de hacer cualquier agregación y pivotearlo, *i.e.* antes de ejecutar el paso 11. 
    * Análisis de variables categóricas.
    * Análisis de variables numéricas.
    * Análisis de la serie temporal.
* Al final hay una comparación entre los dataset pivoteados (tp2 vs tp3): medias y desviaciones estándares

### **`tp3_clustering2.ipynb`** - Parte 2: Análisis e imputación de NaNs
* Identificamos los datos faltantes, tanto globales como por subrubro. 
* Clasificamos los subrubros para vendedores que participan en más de uno. En función de esto, definimos reglas para conservar, desechar o imputar registros. 
* Se descartan todos los registros cuya decisión fue `Tirar`. Esto lleva a perder el único modelo de `Comb. Reventa`, por lo que se decide descartar este subrubro y quedarnos con los otros 10.
* Tests de imputación: se imputa con ceros o mediante KNN. Luego se reescalea con `MinMaxScaler`. Finalmente se prueba aplicando un PCA de 12 componentes y de 40 componentes.
* Se hace un estudio de la varianza explicada de PCA para cada caso.
* Análisis de métricas para k-means: se estudia la cantidad de clusters según el método del codo y el coeficiente de silueta.


### **`tp3_clustering3.ipynb`** - Parte 3: Clusterización con K-means y DBSCAN
* Clusterizamos con K-means usando $K=5$ y luego grafiamos usando un PCA de 2 componentes.
* Determinamos el `eps` óptimo por subrubro para usar en DBSCAN.
* Clusterizamos usando DBSCAN con el `eps` óptimo para cada subrubro.

### **`tp3_clustering4.ipynb`** - Parte 4: Evaluación de resultados
* ñlkñlk

---
# Análisis de resultados

### Parte 1: Preparación y análisis de los datos
Cuando hacemos el análisis detallado del dataset resultante luego de la curación y antes de ejecutar el paso 11. , vemos que no hay cambios apreciables en respecto a sus resultados equivalentes del tp2. Sin embargo, cuando comparamos los datasets pivoteados entre el tp2 y el tp3, hay una clara variación tanto en las medais como en las desviaciones estándares gracias al nuevo paso de curación realizado. Ahora los datos son muchísimo menos ruidosos y presentan rangos de variación más acotados. Algunos subrubros presentan una mayor variación entre el tp2 y tp3 que otros: 'Farmacia', 'Comb.', 'Vehiculos', 'Tabaco' y 'Comb. Reventa' presentan las variaciones más leves. 

***Nota:*** Recordamos que la cantidad de subrubros con la que contamos es de 11: `Com. Varios`, `Comb.`. `Comb. Ley`, `Comb. Reventa`, `Farmacia`, `Gondola`, `Miscelaneo`, `Supermercados`, `Tabaco`, `Vehiculos` y `Venta Agrop.`.

### Parte 2: Análisis e imputación de NaNs
Al identificar los datos faltantes en el dataset pivoteado, vemos que hay de todo: desde 0 datos faltantes hasta casi la totalidad de datos faltantes. Incluso se presentan vendedores modelo con datos faltantes. Notamos que en muchos casos se debe a que dichos vendedores participan en más de un subrubro.

Debido a esta participación de varios vendedores en más de un subrubro, tanto modelos como no modelo, se decidió clasificar su participación de la siguiente manera:
* Se asigna que el subrubro es **Primario** cuando
    * Es el único en el que participa.
    * Es el que tiene la menor cantidad de valores faltantes cuando participa en más de uno. Si la cantidad de faltantes es la misma en dos o más de los subrubros que participa, se define como **Primario** aquel con mayor volumen de ventas.
* Se asigna que el subrubro es **Secundario** cuando no satisface lo recién dicho.

Estas decisiones se asignan a una nueva variable: `Tipo_subrubro`.

Posteriormente, se consideraron en conjunto las variables `Tipo_subrubro`, `Modelo` y `Vacios`, la cual cuenta la cantidad de datos faltantes, para establecer una decisión: `No hacer nada`, `Imputar` o `Tirar`. El sistema de decisiones funciona de la siguiente manera:

| Modelo | Tipo_subrubro | Vacíos         | Decisión       |
|--------|---------------|----------------|----------------|
| 1      | Primario      | 0              | No hacer nada  |
| 1      | Primario      | Hasta 68 (50%) | Imputar        |
| 1      | Primario      | Más de 68      | Tirar          |
| 1      | Secundario    | 0              | No hacer nada  |
| 1      | Secundario    | Hasta 34 (25%) | Imputar        |
| 1      | Secundario    | Más de 34      | Tirar          |
| 0      | Primario      | 0              | No hacer nada  |
| 0      | Primario      | Hasta 14 (10%) | Imputar        |
| 0      | Primario      | Más de 14      | Tirar          |
| 0      | Secundario    | 0              | No hacer nada  |
| 0      | Secundario    | Hasta 7 (5%)   | Imputar        |
| 0      | Secundario    | Más de 7       | Tirar          |

***Nota:*** a modo de referencia son 136 las variables que contienen la variación porcentual.

Se procede a descartar todos aquellos registros que fueron asignados con `Decision` = `Tirar`. Luego de esto nos quedamos con:
* 3180 registros >> 30% menos.
* 46 vendedores únicos modelo >> 15% menos.
* 1 subrubro menos >> descartamos el subrubro `Comb. Reventa` ya que tenía un único vendedor modelo, pero el mismo fue descartado al tener 70 valores faltantes. Se analizó la posibilidad de combinar los subrubros asociados al combustible, pero tenía comportamientos disímiles entre sí.

Dentro de los registros asociados a los 10 subrubros restantes, aún se tienen valores faltantes. Se evalúa entonces el efecto de imputar con un valor constante de 0 o utilizando KNN con $k=5$. En cada caso se realiza además un PCA con 12 componentes. Para cada una de estas 4 situaciones (sólo imputar con 0, imputar con 0 y hacer PCA de 12 componentes, sólo imputar con KNN, e imputar con KNN y hacer PCA de 12 componentes) se calculó la inercia. En la siguiente figura vemos comparadas las inercias resultantes para las 4 situaciones. Si bien no se ve un codo bien definido, no pudiendo utilizar el método del codo para seleccionar una cantidad adecuada de clusters, observamos que la menor inercia se obtiene cuando se imputa con KNN y además se hace una reducción con PCA para quedarnos con las 12 componentes principales. Esto es un indicio de que esta es la mejor opción dentro de las 4 planteadas.

![codo4](figures/tp3_codo4.png)

Respecto a la varianza, en la siguiente figura se muestra a modo de ejemplo los resultados obtenidos para la imputación con KNN y posterior uso de PCA sobre el total de variables disponibles. Vemos que, salvo para `Tabaco` que cumple casi con el 100%, la varianza explicada con 12 componentes es bastante pobre: va entre el 50 y el 75%. Sin embargo, al probar PCA con 40 componentes para asegurarnos de tener al menos el 80% de la varianza explicada en todos los subrubros, esto resulta en una clusterización aún más pobre: la inercia de este proceso es equivalente a la inercia obtenida cuando sólo se imputaba con 0. Esto se puede entender pensando en que el valor de 12 se adecua más a un proceso temporal (asociándolo a un año), mientras que con 40 comenzamos a conservar demasiado ruido. Esto último se puede observar al considerar las alturas de las barras en los histogramas de la figura.

![codo4](figures/tp3_varexp.png)

Como el método del codo no nos sirve como métrica para decidir cuántos clusters utilizar, se probó el coeficiente de silueta. Determinamos primero el valor promedio del coeficiente de silueta para cada subrubro. En términos generales, los mejores puntajes se obtienen usando entre 2 y 5 clusters. En función de esto, analizamos los diagramas de silueta para cada subrubro, tomando de 2 a 5 clusters. Lo primero que salta a la vista es que todos los subrubros están sumamnete desbalanceados: la gran mayoría de los datos cae dentro de un cluster, y los demás clusters están conformados por una cantidad muy pequeña de datos. Además, hay muchos casos que presentan scores negativos, indicando una mala asignación del cluster. Finalmente, en todos los casos se presentan clusters que se ubican por debajo del valor promedio del coeficiente de silueta (líneas punteadas rojas), lo cual indica en principio que dichas clusterizaciones no son buenas. Esto se puede ver en el siguiente ejemplo, donde se ven los resultados para `Comb. Ley`.

![codo4](figures/tp3_silueta.png)

A pesar de todo esto, los resultados tienen sentido si los enmarcamos en nuestro problema: el comportamiento fraudulento es raro y poco habitual, dando lugar a dataset extremadamente desbalanceados donde se presenta un grupo preponderante por sobre el resto.

### Parte 3: Clusterización con K-means y DBSCAN

Primero clusterizamos con K-means usando $K=5$ y, luego, grafiamos usando un PCA de 2 componentes. A modo de ejemplo, veamos el resultado para `Miscelaneo`. Vemos que todos los modelos (estrellas) pertenecen únicamente al cluster 1 (azul) y la mayor densidad de puntos se da en torno a éstos. Notamos que, al forzar 5 clusters, el algoritmo nos puede estar separando datos que en realidad no deberían separarse. Se pondría plantear que los clusters 1 y 3 (azul y violeta) son en realidad el mismo cluster. Incluso podría incluirse el cluster 0 (rojo), quedando como cluster outliers el 2 y 4 (verde y naranja). 

![codo4](figures/tp3_kmeans_misc.png)

Este patrón se repite para todos los subrubros. No consideramos que K-means sea el modelo adecuado debido a la necesidad de una intervención humana post clusterizado para realizar una inspección visual y determinar manualmente qué conjunto de clusters consideramos indicadores de buen comportamiento y cuáles son outliers, *i.e.* debemos marcarlos y evaluarlos. Por este motivo, probamos con DBSCAN. 

Para clusterizar utilizando DBSCAN, primero determinamos el `eps` óptimo para cada subrubro, utilizando una regla análoga al método del codo. Obtenidos estos valores, se procede a clusterizar con DBSCAN y, luego, grafiamos usando un PCA de 2 componentes. A modo comparativo, se muestra el resultado obtenido para `Miscelaneo`. Vemos ahora que volvemos a tener una región densa y puntos dispersos. Además, se forma un único cluster, el cual contiene a los modelo. Aquellos puntos que no pertenecen a este cluster son outliers. 

![codo4](figures/tp3_dbscan_Miscelaneo.png)

Este patrón se repite para todos los subrubros, salvo para el caso de `Tabaco`, donde no se encuentra ningún outlier: este rubro consta de 22 vendedores únicos, donde los datos están muy dispersos.

![codo4](figures/tp3_dbscan_Tabaco.png)

Observamos entonces que DBSCAN es más útil ya que no requiere de una intervención humana. Los resultados de este modelo para cada subrubro se tabulan a continuación. El valor de $N$ es la cantidad de vendedores únicos presentes en dicho subrubro, mientras que $R$ es la proporción de outliers.
    $$R = \frac{outliers}{N} * 100$$

|    Subrubro    |   N  | eps  | min_samples | outliers |    R    |
|----------------|------|------|-------------|----------|---------|
| Com. Varios    |  301 | 0.30 |      23     |    29    |  9.63 % |
| Comb.          |  189 | 0.25 |      23     |    15    |  7.94 % |
| Comb. Ley      |------|------|-------------|----------|---------|
| Farmacia       |  173 | 0.40 |      23     |    16    |  9.25 % |
| Gondola        |  409 | 0.25 |      23     |    22    |  5.38 % |
| Miscelaneo     | 1240 | 0.15 |      23     |    70    |  5.64 % |
| Supermercados  |  136 | 0.35 |      23     |    18    | 13.24 % |
| Tabaco         |   22 | 0.70 |      11     |     7    | 31.82 % |
| Vehiculos      |  221 | 0.30 |      23     |    18    |  8.14 % |
| Venta Agrop.   |  249 | 0.40 |      23     |    17    |  6.83 % |

### Parte 4: Evaluación de resultados
* sdasda

---
# Conclusiones

asdasdasda

---
# Accionables

asdasdas