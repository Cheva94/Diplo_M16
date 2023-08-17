# TP3 - Explorando Patrones de Datos a través de Clustering

## Objetivo
Aplicar técnicas de clustering para identificar patrones y grupos en el conjunto de datos.

## Pasos a seguir

1. Preparación de Datos:
    * Realiza la limpieza y preprocesamiento básico necesario, como manejo de valores faltantes y normalización de características si es necesario.
    * El modelo toma vectores

2. Selección del Número de Clusters:
    - Explora el método del codo (elbow method) y el método de la silueta para determinar el número óptimo de clusters.
    - Implemente gráficos y elija un valor. Justifique

3. Aplicación de Modelos de Clustering:
    - Decida si hara un cluster por subrubro o uno general. Explique por qué ha tomado esa decisión.
    - Implementa el algoritmo K-means para clustering. Utiliza al menos dos valores diferentes para el número de clusters. Tener en cuenta las categorías de riesgo que se quiere analizar.
    - Implementa otro algoritmo de clustering, como DBSCAN o alguno que conozca o le interese.

4. Visualización de Resultados:
    - Utiliza gráficos (como gráficos de dispersión) para visualizar los resultados del clustering en función de las características más relevantes (Usar PCA o TSNE para poder visualizar).
    - Etiqueta los puntos de datos con el cluster al que pertenecen y utiliza diferentes colores para cada cluster.

5. Interpretación y Evaluación:
    - Interpreta los resultados de los diferentes algoritmos de clustering.
    - Discute las diferencias y similitudes entre los clusters generados por los distintos algoritmos.
    - Evalúa la coherencia interna de los clusters utilizando medidas como la inercia en K-means o la puntuación de silueta.
    - Defina cuales van a ser el o los grupos riesgosos.

6. Confianza en los Resultados:
    - Discute cómo la elección del número de clusters influye en la confianza de los resultados.

7. Preguntas finales
    - ¿Qué valor le da esto al negocio? ¿Cuales son los beneficios de utilizar ML en la industria y en este caso de negocio en particular?
    - ¿Soluciona o nos acerca a una solucion?
    -¿Que se podria mejorar o agregar?

## Entrega

- Informe que incluya una descripción de los pasos realizados.
- Gráficos y visualizaciones pertinentes que respalden la interpretación y evaluación de los resultados.
- Discusión sobre la confianza en los resultados y las consideraciones al elegir el número de clusters.