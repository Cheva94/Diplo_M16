# TP1 - Visualización

Las principales preguntas de investigación que nos planteamos son:
1. Con los datos disponibles ¿se puede predecir cuáles serán los **mejores vendedores de la empresa**?
2. Con los datos disponibles, ¿ se puede validar el modelo de **“vendedor ideal”** propuesto por la empresa?
3. ¿Qué modelo podría predecir el comportamiento de los vendedores cuyo comportamiento de ventas se desvían del comportamiento del **vendedor modelo**?
4. ¿Se pueden identificar diferentes **perfiles** de vendedores?
5. ¿Qué predicción de venta y de pago de comisiones se pueden obtener para el próximo periodo?

## Introducción
Las series temporales son conjuntos de datos organizados en secuencia temporal. Estos datos pueden ser recolectados a intervalos regulares (por ejemplo, cada hora o cada día) o irregulares. El análisis de series temporales implica comprender y modelar los patrones, tendencias y comportamientos que se presentan en el tiempo.
En este trabajo práctico, vamos a trabajar con un conjunto de datos de una serie temporal y realizaremos un análisis básico para comprender sus características y obtener información relevante. Utilizaremos herramientas de estadística, visualización y probabilidades para lograr nuestros objetivos. Hay una librería muy util de python para series temporales `Statsmodels` (recomiendo que la vean y si les parece conveniente la usen).

## Pasos a seguir

### Paso 1 - Carga y exploración inicial de datos
1. Cargar los datos.
2. Explora la estructura de los datos: número de observaciones, variables disponibles, intervalo de tiempo entre observaciones, etc.
3. Observa las primeras y últimas filas de los datos para tener una idea general de su contenido.
4. Verifica si hay valores faltantes o atípicos en los datos y **propongan cómo manejarlos**.

### Paso 2 - Análisis estadístico descriptivo
1. Calcula estadísticas descriptivas básicas de la **serie temporal**, como la media, mediana, desviación estándar, mínimo y máximo.
2. Analiza la tendencia central y la dispersión de los **datos**. ¿Existen valores atípicos o extremos? ¿Cómo podrían afectar el análisis posterior?
3. **Grafica** la serie temporal en un gráfico de líneas para visualizar la evolución de los datos a lo largo del tiempo.
4. Calcula y grafica la función de autocorrelación para **identificar posibles patrones de autocorrelación en los datos**. (Es un término estadístico que **se utiliza para describir la presencia o ausencia de correlación en los datos de las series temporales, indicando, si las observaciones pasadas influyen en las actuales**.)

### Paso 3 - Análisis de variables
1. Si el conjunto de datos contiene múltiples variables, analiza las estadísticas descriptivas de cada una de ellas.
2. Explora la relación entre las variables y la serie temporal principal. ¿Hay alguna correlación aparente?
3. Calcula y visualiza la matriz de correlación entre las variables para identificar posibles relaciones significativas.

### Paso 4 - Distribución de frecuencias y probabilidades
1. Si los datos son continuos, crea un histograma para visualizar la distribución de frecuencias.
2. Calcula medidas como la asimetría y la curtosis para analizar la forma de la distribución.
3. Si los datos son discretos, crea una tabla de frecuencias y grafica un diagrama de barras para visualizar la distribución.

### Paso 5 - Conclusiones y recomendaciones
1. Resume las principales características y hallazgos del análisis realizado.
2. Proporciona interpretaciones sobre los patrones, tendencias o comportamientos identificados en los datos.
3. Sugiere posibles puntos de investigación o análisis más detallados en base a los resultados obtenidos.
4. Sugerir nuevas variables a crear a partir de otras del dataset.
5. Recomienda acciones o decisiones basadas en los hallazgos del análisis de la serie temporal.

## Preguntas disparadoras
1. ¿Cuáles son las principales estadísticas descriptivas de la serie temporal y qué información aportan?
2. ¿Qué patrones o tendencias puedes identificar al visualizar la serie temporal en un gráfico de líneas?
3. ¿Existen valores atípicos o extremos que podrían afectar el análisis? ¿Cómo podrías manejarlos?
4. ¿Cuál es la relación entre la serie temporal principal y otras variables presentes en el conjunto de datos?
5. ¿Cuáles son las posibles relaciones significativas entre las variables según la matriz de correlación?
6. ¿Cómo se distribuyen los datos en términos de frecuencia? ¿Qué forma tiene la distribución?
7. ¿Las variables analizadas son independientes o están condicionadas por otra variable?

> Recuerda que esta guía es solo una introducción al análisis y visualización de datos de series temporales. Para un análisis más completo y sofisticado, se pueden aplicar técnicas adicionales como modelos de series temporales, descomposición, análisis de estacionalidad, entre otros.

## Entrega
**Breve informe** en el cual desarrollen los puntos anteriores, el cual debe incluir:gráficos, resultados obtenidos y las conclusiones obtenidas (no agregar código al informe)

**Notebook** que refleje el trabajo realizado en Python. Puede ser la notebook aquí presentada e intervenida por ustedes o bien generar una nueva.

**Estructura del informe:** en formato pdf o markdown. El contenido del informe debe dar cuenta de una adecuada manipulación de las herramientas estadísticas para visualizar resultados de interés del estudiante en contextos de masividad. Incorporando elementos de Estadística descriptiva, Estadística inferencial y Visualización. El informe deberá mostrar la interpretación que surge del análisis realizado.