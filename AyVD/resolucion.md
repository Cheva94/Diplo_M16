# Diplomatura en ciencia de datos, aprendizaje automático y sus aplicaciones - Edición 2023 - FAMAF (UNC)

## Mentoría 16 - ¿Cómo identificar fuga de ventas? Inteligencia artificial aplicada al sector comercial.

### Análisis y visualización de datos (TP1)

**Integrantes:**
- Canalis, Patricio.
- Chevallier-Boutell, Ignacio José.
- Villarroel Torrez, Daniel.

**Mentores:**
- Gonzalez, Lucía
- Lahoz, Nahuel

---

> Tamaño del dataset, nombres y tipo de variables

El dataset provisto consta de 431506 registros con información sobre las ventas realizadas por los vendedores dentro de la plataforma de ventas online del cliente. Dicha información viene caracterizada por 19 variables. La definición de cada una de estas variables se tiene en el data statement. En resumen, cada registro informa la suma total de las ventas efectuadas por cada uno de los depósitos de cada vendedor, para un mes y año dados. Por razones de sensibilidad de los datos y la confidencialidad necesaria, las variables que refieren a datos personales (`ID_VENDEDOR` y `NOMBRE`) fueron anonimizadas mediante hasheo.

> Cardinalidad: valores únicos de las variables

Se determinó cuántos valores únicos hay presentes en cada una de las 19 variables. Además, se analizó la contribución porcentual del valor mayoritario y, en de ser posible, la contribución porcentual de los 10 valores mayoritarios. Se tiene que:
* **ID_VENDEDOR**: tiene 3209 valores diferentes. El valor mayoritario (vendedor f679b20b02309cab33658571f0c8da237f57f732ab96978386a95c2776f07c21) contribuye en un 0.39% de los registros y los 10 primeros en conjunto contribuyen al 2.85%
* **NOMBRE**: tiene 3199 valores diferentes. El valor mayoritario (nombre b1ccd106f41645af33abb71ae22795538722ff64dfc00ba0648f08da873a7885) contribuye en un 0.39% de los registros y los 10 primeros en conjunto contribuyen al 2.85%.
* **MODELO**: tiene 2 valores diferentes: 0 y 1. Sólo el 0.32% de los registros (valor 1) es considerado **vendedor modelo** por parte del cliente.
* **DEPOSITO**: tiene 241 valores diferentes. El valor mayoritario (depósito 469090) contribuye en un 5.21% de los registros y los 10 primeros en conjunto contribuyen al 26.64%.
* **INSCRIPCION**: tiene 3345 valores diferentes. El valor mayoritario (inscripción 9043011028) contribuye en un 0.39% de los registros y los 10 primeros en conjunto contribuyen al 2.72%.
* **AÑO**: tiene 4 valores diferentes: desde 2019 hasta 2022. La contribución mayoritario es del 2021 (29.69%), mientras que el 2022 tiene la contribución minoritaria (15.02%).
* **MES**: tiene 12 valores diferentes: los 12 meses del año. Junio es el que más contribuye (9.56%). Los 10 meses con mayores contribuciones suman un total del 85.78% de registros, siendo Agosto y Julio los minoritarios (7.12% y 7.10%, respectivamente).
* **TOTAL_VENTAS**: tiene 248974 valores diferentes. El valor mayoritario (ventas por un monto total de $0) contribuye en un 41.96% de los registros, mientras que los 10 primeros en conjunto contribuyen al 42.06%.
* **PORCENTAJE_COMISION_EMPRESA**: tiene 89 valores diferentes. El valor mayoritario (comisión del 4.75%) contribuye en un 19.41% de los registros y los 10 primeros en conjunto contribuyen al 73.27%.
* **COMISION_EMPRESA**: tiene 244284 valores diferentes. El valor mayoritario (comisión de $0 para el cliente) contribuye en un 42.52% de los registros y los 10 primeros en conjunto contribuyen al 42.56%.
* **CATEGORIA**: tiene 5 valores diferentes, pero parece que en realidad son todas la misma categoría, con diferentes formatos de escritura.
* **CATEGORIA (Ajustado)**: tiene un único valor: "COMERCIO AL POR MAYOR Y AL POR MENOR; REPARACION DE VEHÍCULOS AUTOMOTORES Y MOTOCICLETAS". En efecto la variable `CATEGORIA` presentaba un único valor, escrito de formas diferentes.
* **DESCRIPCION_CATEGORIA**: tiene 245 valores diferentes. El valor mayoritario ("Venta al por mayor de mercancías n.c.p.") contribuye en un 5.21% de los registros y los 10 primeros en conjunto contribuyen al 26.64%.
* **SUB-CATEGORIA**: las 245 opciones de `DESCRIPCION_CATEGORIA` fueron reducidas a 21 valores diferentes. El valor mayoritario ("Venta de Artículos, productos, accesorios, etc de diversos materiales") contribuye en un 32.51% de los registros y los 10 primeros en conjunto contribuyen al 87.78%. 
* **DESC_TRATAMIENTO_FISCAL**: tiene 4 valores diferentes. El valor mayoritario (tratamiento fiscal Normal) contribuye en un 94.36% de los registros.
* **TRATAMIENTO_FISCAL**: tiene 17 valores diferentes: algunos numéricos y otros categóricos. El valor mayoritario (tratamiento fiscal Normal) contribuye en un 45.50% de los registros y los 10 primeros en conjunto contribuyen al 99.16%.
* **TRATAMIENTO_DIFERNCIAL**: tiene 11 valores diferentes. El valor mayoritario (Art. 21) contribuye en un 34.45% de los registros y los 10 primeros en conjunto contribuyen al 99.52%.
* **CM04**: tiene un único valor: "Sí".
* **OMEGA**: tiene un único valor: 1.

Algunas observaciones que podemos hacer al respecto son:
* `INSCRIPCION` tiene 136 valores únicos más que `ID_VENDEDOR`, pero porcentajes similares entre los 10 primeros: puede existir una relación entre ambas, la cual no necesariamente es biyectiva.
* Hablar sobre que hay muchísimos menos valores únicos que id_vendedor
* La cantidad de valores en `DESCRIPCION_CATEGORIA` es similar al de la variable `DEPOSITO` y, además, las contribuciones porcentuales son simialres. Puede existir una relación entre ambas variables. Si existía una relación con `DEPOSITO` ¿se sigue apreciando en esta nueva variable (cuando se ajustó)?
* Hablar sobre ventas de $0. Correlación entre este cero y la comisión.
* Tratamiento_fiscal: Hay que unificar cosas como 0 y 0.0. Además ¿existe alguna relación entre ser 1 y ser especial 1? (o similares)
* ¿Qué relación hay entre esta variable (desc) y `TRATAMIENTO_FISCAL`?
* Tratamiento diferencial: ¿Cómo tratar a los casos "Art. 19", "Art. 20" y "Art. 19 y 20"?
* Esta variable tenía casi el 100% de registros vacíos: ¿estar vacío implica un "No"?
* Nombre:  Si bien los porcentajes son similares a aquellos encontrados para `ID_VENDEDOR`, los hashs son diferentes y, además, hay 10 nombres menos.
* Omega: como habíamos dicho, por lo que no aporta nada de información relevante.

> Datos faltantes

Vemos que tenemos un total de 431.506 registros. Entre las variables disponibles tenemos 5 con valores faltantes:
* **CM04:** sólo hay 42 registros (menos del 0.01% del total de registros).
* **TRATAMIENTO_DIFERNCIAL:** tiene 83.058 reigstros (cerca del 20% del total de registros).
* **DESC_TRATAMIENTO_FISCAL:** tiene 117.841 registros (cerca del 30% del total de registros).
* **TRATAMIENTO_FISCAL:** tiene 403.538 registros (más del 90% del total de registros).
* **NOMBRE:** tiene 430.857 registros (casi el total de registros).