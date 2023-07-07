# TP2 - Análisis exploratorio y curación de datos

## Objetivo
Generar variables que discriminen vendedores ‘modelos’ de ‘no modelos’.

## Pasos a seguir

1. Eliminar las siguientes variables: Inscripción, Categoría, Descripción categoría, Categoría Ajustada y Nombre. ¿Por qué cree que deberían eliminarlas?

2. Revise todos aquellos subrubros que tengan representación de usuarios modelos. Va a notar que algunos no están representados. Todos aquellos en esta condición deben de modificar su subrubro y tomarlo como ‘Otros’. En total deberían quedar 13 subrubros. 12 con sus categorías correspondientes y una ultima con el label ‘Otros’.

3. Anonimizar los datos que se consideran sensibles. (Aunque ya estén anonimizados). ¿Por qué es importante hacer esto?

4. Investigar la incidencia del CM04. ¿Los modelos participan de este régimen? ¿Que tamaño de la muestra representa esto? ¿Qué haría con este o estos vendedores?

5. Tome una decisión de qué hacer con respecto a las columnas de tratamientos fiscal, descripcion_tratamiento_fiscal y Tratamiento_diferencial, según lo analizado en práctico anterior.

6. Modifique la columna de año y cuota para su uso según su conveniencia.

7. Grafique por subrubro 3 la variación en el tiempo del Total de ventas, diferenciando modelos de no modelos.

8. Genere una representación vectorial para cada contribuyente que represente el comportamiento del mismo en los últimos (periodo de tiempo a elección)(Preste atencion a la estacionalidad de la serie de tiempo). Con la comisión y otro con comisiones promedio. ¿Conviene tomar los valores absolutos o relativos? Decida. Hay algunos vendedores que participan en mas de un sub rubro ¿Que hará con ellos? ¿Analizara para cada subrubro que participe? ¿Se quedara con el de mayor aporte? Decida.
¿Que hacer con lo que tienen muchos depositos?

9. Genere una nueva columna que represente la varianza de este vector. ¿Que información representa esta variable?

10. Genere una nueva columna que represente la media o promedio del vector. ¿Que información representa esta variable?

11. Analice estos vectores. ¿Nos brindan alguna información? ¿Que cree que se puede hacer con ellos?