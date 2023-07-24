# Diplomatura en ciencia de datos, aprendizaje automático y sus aplicaciones - Edición 2023 - FAMAF (UNC)

## Mentoría 16 - ¿Cómo identificar fuga de ventas? Inteligencia artificial aplicada al sector comercial.

### Curación de datos (TP2)

**Integrantes:**
- Canalis, Patricio.
- Chevallier-Boutell, Ignacio José.
- Villarroel Torrez, Daniel.

**Mentores:**
- Gonzalez, Lucía
- Lahoz, Nahuel

---

## Introducción

El objetivo de esta etapa de curación de datos es generar variables que discriminen vendedores "modelos" de "no modelos". 

En esencia, la forma en que lo llevamos a cabo fue tomando información temporal explícita (ventas para cada fecha para cada vendedor) y aplicando transformaciones para poder obtener información nueva que sea comparable a otros usuarios dentro del mismo rubro. 

Consideramos que la información de ventas totales mensuales no es muy informativa ya que no es comparable entre vendedores con distinto volumen. Por esta razón, decidimos explorar formas de generar nueva información a partir de éstas. Es necesario tener en cuenta que no todas las variables serán útiles para el objetivo de discriminar usuarios en todos los subrubros. 

Durante el proceso de curación se tomaron las siguientes decisiones:

- Eliminar las siguientes variables: Inscripción, Categoría, Descripción categoría, Categoría Ajustada y Nombre. La variable "Nombre" se eliminó por ser de carácter sensible. "Inscripción" se eliminó por ser redundante, y las variables referentes a la categoría se eliminaron ya que existe otra llamada "Subcategoría" (de aquí en adelante Subrubro) que aporta más información.
- Todos aquellos subrubros sin usuario "modelo" fueron categorizados como "Otro" y posteriormente fueron eliminados sus registros.
- Se anonimizó el identificador de vendedor para mantener los registros pero evitar tener datos sensibles en el dataset.
- Se descartó del dataset al único vendedor con valor de 1 en el campo CM04, ya que representa el 0.01% de los casos y no es modelo.
- Se eliminaron las variables fiscales (En primer lugar, "Descripción tratamiento fiscal" y "Tratamiento diferencial", ya que "Tratamiento fiscal" ofrece más información. En segunda instancia también se descartó esta última, por no aportar información relevante a la hora de separar Modelos).
- Cuando un vendedor participa en distintos subrubros se toma como si fuese un vendedor distinto, por lo tanto aparecerá en otro registro.


## Resultados

El resultado principal de esta etapa de curación fue la obtención de un dataset muy parecido a lo que podría servir como datos para prácticamente cualquier modelo de aprendizaje automático. Esto quiere decir, que cada registro de este nuevo dataset representa a un solo vendedor y su comportamiento en términos de ventas en el tiempo.

De forma esquemática, pasamos de un dataset que se ve como éste:

| año-mes 	| subrubro 	| vendedor 	| ventas 	|
|---------	|----------	|----------	|--------	|
| 2022-01 	| A        	| 1        	| 42     	|
| 2022-02 	| A        	| 1        	| 999    	|
| 2022-03 	| A        	| 1        	| 666    	|
| 2022-04 	| A        	| 1        	| 69     	|

A un dataset que se ve como este:

| subrubro 	| vendedor 	| dif_12_1 	| dif_12_2 	| ... 	| dif_12_n 	| dif_4_1 	| dif_4_2 	| ... 	| dif_4_n 	| dif_12_mean 	| dif_12_var 	| dif_4_mean 	| dif_4_var 	|
|----------	|----------	|----------	|----------	|-----	|----------	|---------	|---------	|-----	|---------	|-------------	|------------	|------------	|-----------	|
| A        	| 1        	| N        	| N        	| N   	| N        	| N       	| N       	| N   	| N       	| N           	| N          	| N          	| N         	|

Vale la pena aclarar que al agrupar las ventas únicamente por vendedor y por subrubro estamos perdiendo la capacidad de ver diferencias en otras categorías, como "Tratamiento fiscal" o "Depósito". Sin embargo es el compromiso que estamos dispuestos a asumir por el momento, y quedará registrado. En caso de avanzar con el análisis y tener la necesidad a futuro de desagregar por estas otras variables podremos hacerlo.

## Hechos estilizados

* Ventas y comisiones:
    - Durante el confinamiento obligatorio (primera mitad de 2020) las caídas fueron muy fuertes para algunos rubros.
    - Hay menos dispersión de datos para vendedores no-modelo: parecieran ser más consistentes.
    - Los valores de venta en Modelos son menores en todos los Subrubros, con la excepción de tres: "Góndola", "Comb." y "Comb. Ley".
* Variación de ventas y comisiones:
    - En promedio, en todos los rubros los modelos tienen variaciones de menor magnitud y variabilidad. Es decir, mantienen un comportamiento estable a lo largo del tiempo.


## Trabajo a futuro

El dataset que generamos tiene muchas variables fabricadas que caracterizan el comportamiento temporal de cada vendedor en cada subrubro. Sin embargo no todas estas características aportarán mucho valor "predictivo" que nos permita diferenciar entre modelos y no modelos. 

Los próximos pasos que se deben seguir será por un lado: explorar nuevas variables, y por otro lado discriminar entre todas las variables generadas para conseguir combinaciones de ellas que ofrezcan la mayor información. Algunas técnicas que podríamos utilizar pordrían incluir la reducción la dimensionalidad mediante análisis de componentes principales o el uso de embeddings.

Por otra parte, teniendo en cuenta que la mayor parte de los vendedores son no modelo, vamos a tener que realizar algún tratamiento para corregir ese desbalance o tenerlo en cuenta.


## Accionables

Con la información que tenemos, ya podemos comenzar a explorar diversos modelos de aprendizaje automático, supervisado o no, teniendo en cuenta que además de "modelos" y "no modelos", dentro de los "no modelos" deberíamos poder diferenciar entre vendedores con comportamiento "normal" y aquello que efectivamente representan fugas.