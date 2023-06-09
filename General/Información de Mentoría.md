# ¿Cómo identificar fuga de ventas? Inteligencia artificial aplicada al sector comercial.

## Descripción

### Problema inicial
Una empresa de venta online de productos está sospechando que algunos vendedores están realizando ventas por fuera del canal de ecommerce. La empresa quiere detectar y predecir quiénes son esos vendedores, y cómo poder detectarlos a partir de los datos disponibles. 
En base a diferentes datos (registros internos, datos históricos, entrevistas a mandos medios), la empresa ha podido identificar a un grupo de vendedores que ha denominado “vendedores modelos”. Estos vendedores realizan el 100% de sus transacciones comerciales a través de la plataforma online, y por lo tanto, se comportan de acuerdo a las normas y acuerdos establecidos entre la empresa y los vendedores. Sin embargo, tal como se indicó antes, no todos los vendedores se comportan de la misma manera, sospenchando que hay algunos grupos que tienen ciertos comportamientos que se desvían del “ideal”.

### Problema actual
¿Cómo identificar grupos de vendedores, cuyo comportamiento de ventas se desvían del comportamiento del vendedor modelo?

### Necesidad
1. Predecir qué vendedores son los vendedores riesgosos que tendrían comportamientos sospechosos de realizar ventas por fuera de la plataforma de ventas online. 
2. Disponer de un  sistema de información que brinde una alerta para detectar vendedores que se desvíen del comportamiento deseado. A partir de esa información, la empresa espera poder diseñar estrategias que permitan retener a vendedores talentosos y que sus gestiones de ventas se realicen dentro de los canales de ventas establecidos. 
3. Proponer modelos que permitan identificar, clasificar y describir perfiles de vendedores. 
4. Verificar si el perfil del “vendedor modelo” identificado por la empresa con criterios cuantitativos y cualitativos se valida con los datos presentados en el dataset. 
5. Analizar las comisiones por ventas para realizar una predicción de las comisiones por ventas a pagar en futuros periodos. 
6. Incorporar datos externos al dataset para eliminar la incidencia de la inflación en las variables monetarias. 
7. Incorporar técnicas de fairness y prevención de riesgo sobre datos sensibles: ¿qué otros usos podrías darles a estos datos? ¿para qué los usarías, con qué fin? Usos alternativos de los datos.

## Este tema es interesante porque...
El desafío de los analistas de datos es convertir los datos en valor tangible para las organizaciones y para las personas. Este proyecto resulta relevante porque le brindará a los estudiantes la posibilidad de trabajar en un problema real donde aplicar herramientas de inteligencia artificial para resolver un problema del sector comercial de una empresa real. 

Para ello, se brindará una metodología de trabajo que permita desarrollar un modelo predictivo que alivie las problemáticas reales de la empresa. Estos modelos de ser puestos en producción (es decir, que sean usados en la empresa) tienen impacto en métricas de rendimiento del negocio, en este caso, una reducción de las pérdidas de las empresa por las ventas que realizan los vendedores por fuera de la plataforma.

## Preguntas a responder
Las principales preguntas que nos planteamos son:
1. Con los datos disponibles ¿se puede predecir cuáles serán los mejores vendedores de la empresa?
2. Con los datos disponibles, ¿ se puede validar el modelo de “vendedor ideal” propuesto por la empresa?
3. ¿Qué modelo podría predecir el comportamiento de los vendedores cuyo comportamiento de ventas se desvían del comportamiento del vendedor modelo?
4. ¿Se pueden identificar diferentes perfiles de vendedores?
5. ¿Qué predicción de pago de comisiones se pueden obtener para el próximo periodo?

## Datos

### Origen de los datos
Los datos fueron provistos y recopilados por el contador de la empresa. Los datos que identifican datos personas fueron anonimizados.

### Descripción de los datos
En general, el set de datos contiene información sobre ventas, comisiones por ventas correspondientes a un periodo de 5 años. 
Se identifican los vendedores, clasificados en vendedores mayoristas y minoristas 
Los datos de las ventas se pueden desmenuzar por subrubros de productos.
Se identifican también los vendedores que integran el grupo de “vendedores modelo”.
Se presenta un diccionario de datos, donde se incluyen las variables que integran el dataset y su descripción. https://github.com/git-lu/datos-kl-mentoria-2023/tree/main

## Hitos de la mentoría
* **Entrega 23/06**: Práctico 1 de análisis y visualización, que consistirá en observar el comportamiento a través del tiempo de los vendedores “modelo” en comparación al resto de los vendedores. Utilizaremos herramientas de visualización de series temporales.
* **Entrega 17/07**: Práctico 2 de análisis exploratorio y curación de datos, que consistirá en modelar a los contribuyentes de tal manera de poder crear un clasificador de contribuyentes, que asigne un riesgo de estar realizando ventas por fuera de la plataforma. Este modelo puede o no estar basado en series temporales. Es decir, a partir de los datos, basados en series temporales, se generarán variables tales como “promedio de venta mensual” que nos permitirá modelar a los contribuyentes de manera tabular.
* **Entrega 27/07**: Video de presentación intermedia del proyecto y dataset
* **Entrega 11/09**: Práctico 3 se aprendizaje supervisado o no supervisado, o ambos que consistirá en crear un clasificador de vendedores modelos, con el objetivo de ampliar la muestra. Este problema puede resolverse de manera supervisada o no supervisada, utilizando diferentes técnicas de clasificación y/o clustering a partir de las variables construidas en el práctico 2. Si se quisiera realizar el práctico aprendiendo series temporales, podemos trabajar con preguntas alternativas.
* **Entrega 23/09**: Video de presentación final de mentoría
* **Jornadas 10/11 y 11/11**: Presentación de mentorías