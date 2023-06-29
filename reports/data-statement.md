# Diplomatura en ciencia de datos, aprendizaje automático y sus aplicaciones - Edición 2023 - FAMAF (UNC)

## Mentoría 16 - ¿Cómo identificar fuga de ventas? Inteligencia artificial aplicada al sector comercial.

**Integrantes:**
- Canalis, Patricio.
- Chevallier-Boutell, Ignacio José.
- Villarroel Torrez, Daniel.

**Mentores:**
- Gonzalez, Lucía
- Lahoz, Nahuel

---

## Data statement

> Motivación

El cliente es una empresa que provee una plataforma de compra-venta online de cierto tipo de productos: los vendedores que forman parte, participan ofertando sus productos en dicha plataforma. Una de las obligaciones que tienen los vendedores es que, si un comprador inicia el contacto a través de la plataforma, el proceso debe progresar exclusivamente dentro de la misma. Aquellos vendedores que cumplen esta norma en la totalidad de sus transacciones comerciales a través de la plataforma se conocen como ***vendedores modelo***. Por algún motivo, el cliente sospecha que hay fuga de ventas: existen vendedores que concretan ventas por fuera de la plataforma, a pesar de haber iniciado el contacto dentro de ésta. En este sentido, nos contrata para detectar y predecir quiénes son estos vendedores que se alejan del comportamiento ideal, proveyéndonos este dataset recopilado por el contador del cliente.

---

> Composición

El dataset provisto consta de 431506 registros con información sobre las ventas realizadas por los vendedores dentro de la plataforma. Dicha información viene caracterizada por 19 variables:
* **ID_VENDEDOR:** identificación del vendedor, asociada a su CUIT. Tipo: string. Cantidad de valores únicos: 3209.
* **NOMBRE:** identificación del vendedor, asociada al nombre *real* (persona física o jurídica) del mismo. Tipo: string. Cantidad de valores únicos: 3199.
* **MODELO:** código de identificación de vendedores considerados modelo por parte del cliente. Tipo: entero. Cantidad de valores únicos: 2 (0 categoriza los que no son vendedores modelo, mientras que 1 los posiciona como tales).
* **DEPOSITO:** identificación del depósito de stock desde el cual se efectúan las ventas. Tipo: entero. Cantidad de valores únicos: 241.
* **INSCRIPCION:** código de inscripción a la plataforma del cliente. Tipo: entero. Cantidad de valores únicos: 3345.
* **AÑO:** año de imputación del registro. Tipo: entero. Cantidad de valores únicos: 4 (desde 2019 hasta 2022).
* **MES:** mes de imputación del registro. Tipo: entero. Cantidad de valores únicos: 12 (desde Enero hasta Diciembre).
* **TOTAL_VENTAS:** monto total de ventas (base imponible). Tipo: flotante. Cantidad de valores únicos: 248974.
* **PORCENTAJE_COMISION_EMPRESA:** comisión por las ventas en la plataforma (alícuota). Tipo: flotante. Cantidad de valores únicos: 89.
* **COMISION_EMPRESA:** comisión por las ventas en la plataforma (valor). Tipo: flotante. Cantidad de valores únicos: 244284.
* **CATEGORIA:** descripción del Código de Actividad Codiguero NAES Año 2018 y siguientes. Tipo: string. Cantidad de valores únicos: 5.
* **CATEGORIA (Ajustado):** variable `CATEGORIA` limpia, *i.e.* se redujo el número de valores posibles. Tipo: string. Cantidad de valores únicos: 1 ("COMERCIO AL POR MAYOR Y AL POR MENOR; REPARACION DE VEHÍCULOS AUTOMOTORES Y MOTOCICLETAS").
* **DESCRIPCION_CATEGORIA:** subrubro definido por la DGR (dato Interno, no declarado por el contribuyente). Tipo: string. Cantidad de valores únicos: 245.
* **SUB-CATEGORIA:** variable `DESCRIPCION_CATEGORIA` limpia, *i.e.* se redujo el número de valores posibles. Tipo: string. Cantidad de valores únicos: 21.
* **DESC_TRATAMIENTO_FISCAL:** indica qué tratamiento fiscal se le da a la operación, especialmente respecto a la alícuota a cobrarle. Tipo: string. Cantidad de valores únicos: 4.
* **TRATAMIENTO_FISCAL:** análogo a `DESC_TRATAMIENTO_FISCAL`, pero desglosado. Tipo: string. Cantidad de valores únicos: 17.
* **TRATAMIENTO_DIFERNCIAL:** indica el artículo de alguna reglamentación aplicado para dar tratamiento fiscal especial. Tipo: string. Cantidad de valores únicos: 11.
* **CM04:** identifica operaciones que se ejecutan bajo un Convenio Multilateral (CM), el cual tiene lugar cuando las operaciones se dan entre provincias diferentes. Tipo: string. Cantidad de valores únicos: 1 ("Sí").
* **OMEGA:** identifica contribuyentes de interés fiscal especial. Tipo: entero. Cantidad de valores únicos: 1 (valor 1).

En resumen, cada registro informa la suma total de las ventas efectuadas por cada vendedor en alguno de los depósitos donde tiene stock de sus productos, para un mes y año dados. Por razones de sensibilidad de los datos y la confidencialidad necesaria, las variables que refieren a datos personales (`ID_VENDEDOR` y `NOMBRE`) fueron anonimizadas mediante hasheo.

Todos los montos se asumen en pesos.

---

> Recopilación y uso

Los datos disponibles contienen información sobre las ventas realizadas entre enero de 2019 y junio de 2022. Recomendamos tener en cuenta factores como inflación y la pandemia de COVID-19, entre otros. Asimismo, conviene incorporar conocimientos del ámbito de las series temporales: aunque no se hagan modelos temporales, los datos están intrínsecamente organizados de alguna manera particular a lo largo del tiempo.

Los vendedores clasificados como **modelo** por parte del cliente, son un grupo de vendedores preseleccionados y deliberadamente monitoreados: los vendedores eran concientes de que estaban siendo monitoreados. Observamos entonces que su honestidad puede haber sido forzada. Además, los parámetros utilizados por el cliente para esta clasificación se desconocen.

El dataset provisto resulta en realidad ser un filtro de un dataset más grande: se filtraron los datos, reteniendo aquellos donde `OMEGA` era igual a 1. Aconsejamos tener esto presente al momento de aplicar los modelos resultantes en producción.

Las ventas registradas son tanto mayoristas como minoristas, lo cual repercute diferente en las comisiones y demás cuestiones asociadas a la recaudación de fondos. Advertimos considerar esto a la hora de ponderar quiénes son vendedores modelo y quiénes realizan fugas.