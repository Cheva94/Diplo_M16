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

### **`tp3_clustering2.ipynb`** - Parte 2: Análisis e imputación de NaNs. Clusterización con k-means.
* Identificamos los datos faltantes, tanto globales como por subrubro. 
* Clasificamos los subrubros para vendedores que participan en más de uno. En función de esto, definimos reglas para conservar, desechar o imputar registros. 
* Se descartan todos los registros cuya decisión fue `Tirar`. Esto lleva a perder el único modelo de `Comb. Reventa`, por lo que se decide descartar este subrubro y quedarnos con los otros 10.
* Tests de imputación: se imputa con ceros o mediante KNN. Luego se reescalea con `MinMaxScaler`. Finalmente se prueba aplicando un PCA de 12 componentes y de 40 componentes.
* Se hace un estudio de la varianza explicada de PCA para cada caso.
* Análisis de métricas para k-means: se estudia la cantidad de clusters según el método del codo y el coeficiente de silueta.


### **`tp3_clustering3.ipynb`** - Parte 3: Clusterización con K-means y DBSCAN.
* Se prueba una clusterización con K-means con los coeficientes óptimos encontrados.

### **`tp3_clustering4.ipynb`** - Parte 4: Evaluación de resultados.

---
# Análisis de resultados

parte1 (ya corrido y listo):
* Análisis previo al 11: No hay cambios apreciables en estos gráficos respecto a sus equivalentes del tp2.
* pivoteados comparados: Hablar sobre la variación de medias y SD gracias al nuevo punto que agregamos. Los datos son muchísimo menos ruidosos ahora. Sin embargo, se ve que algunos subrubros presentan una mayor variación entre el tp2 y tp3 que otros: 'Farmacia', 'Comb.', 'Vehiculos', 'Tabaco' y 'Comb. Reventa' presentan las variaciones más leves.

parte2 (ya corrido y listo):
* id faltantes: Vemos que hay de todo: desde 0 datos faltantes hasta casi la totalidad de datos faltantes. Incluso hay modelos con datos faltantes, pero en muchos casos se debe a que participan en más de un subrubro.
* Poner cómo se clasificaba y qué resultó de esto. Las reglas también.
* Se descartan todos los registros cuya decisión fue `Tirar`. Esto lleva a perder el único modelo de `Comb. Reventa`, por lo que se decide descartar este subrubro y quedarnos con los otros 10.
* Tests de imputación: hablar de lo que se ve.
* Varianza explicada: porque 12 da mejor que 40.
* Faltaría hablar de
    * Análisis de métricas para k-means: se estudia la cantidad de clusters según el método del codo y el coeficiente de silueta.

parte3 (ya corrido y listo):
* Faltaría hablar de que se prueba una clusterización con K-means con los coeficientes óptimos encontrados.
* Faltaría hablar de dbscan.

---
# Conclusiones

---
# Accionables